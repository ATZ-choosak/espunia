from flask import Flask, request, render_template
import fluidsynth
from flask_cors import CORS
from config import *
import json
from ooled import *
import subprocess
from config import *

preset = 0
octave = 3

def read_config():
    with open('/home/pi/Desktop/espunia/config.json', 'r') as file:
        data = json.load(file)
        preset = int(data["preset"])
        octave = int(data["octave"])
    return [preset, octave]

def write_preset(data):
  with open('/home/pi/Desktop/espunia/config.json', 'w') as file:
    save = {
      "preset" : data,
      "octave" : octave
    }
    json.dump(save, file, indent=4)

def write_octave(data):
  with open('/home/pi/Desktop/espunia/config.json', 'w') as file:
    save = {
      "preset" : preset,
      "octave" : data
    }
    json.dump(save, file, indent=4)



fs1 = fluidsynth.Synth()
fs1.start()
sfid1 = fs1.sfload(F"/home/pi/Desktop/espunia/{soundfont}")

preset_get = []

app = Flask(__name__,
            static_url_path='', 
            static_folder='/home/pi/Desktop/espunia/templates',
            template_folder='/home/pi/Desktop/espunia/templates')
CORS(app)

@app.route("/")
def home():
  return app.send_static_file('index.html')

@app.route('/preset' , methods=['GET'])
def get_preset():
    for i in range(127):
        p = fs1.sfpreset_name(sfid1, 0, i)
        preset_get.append(p)
    
    return {"preset" : preset_get} , 200

@app.route('/preset_now')
def get_current_preset():
    data = read_config()
    return {"now" : data[0]} , 200

@app.route("/preset" , methods=['POST'])
def change_preset():
    body = request.get_json()
    write_preset(int(body["preset"]))
    p = int(body["preset"])
    PREDIS(F"Preset : {fs1.sfpreset_name(sfid1, 0, p)}") 
    return { "message ": "OK" }, 200

@app.route("/vol" , methods=['GET'])
def get_volume():
  data = subprocess.Popen("amixer sget 'Master'", shell=True, stdout=subprocess.PIPE).stdout.read()
  split_data = str(data).split(" ")
  get_data = split_data[len(split_data) - 2]
  raw_data = get_data.replace("[" , "").replace("]" , "").replace("%" , "")
  print(raw_data)
  return { "volume": raw_data }, 200

@app.route("/vol" , methods=['POST'])
def set_volume():
  body = request.get_json()
  data = int(body["value"])
  subprocess.Popen(F"amixer sset 'Master' {data}%", shell=True, stdout=subprocess.PIPE)
  return { "message ": "OK" }, 200


def runAPI():
    print("API running")
    app.run(debug=True, use_reloader=False,host="0.0.0.0", port=9000)
