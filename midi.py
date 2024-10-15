import fluidsynth
import I2C
import api
from buttonControl import *
from ooled import *
import threading
import json
from config import *

preset = 0
octave = 3

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

running = True

fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload(F"/home/pi/Desktop/espunia/{soundfont}")
fs.program_select(0, sfid, 0, preset)

fs.setting("audio.period-size", 64)

fs.setting('synth.gain', 1.0)

# Enable reverb and set parameters
#fs.set_reverb(1.0,1.0,100,1.0)  # (roomsize, damping, width, level)

# Enable chorus and set parameters
#fs.set_chorus(3 , 10.0, 1.0, 8.0, 1)  # (nr, level, speed, depth_ms, type)

def readDB():
  with open('/home/pi/Desktop/espunia/config.json', 'r') as file:
    data = json.load(file)
    preset = int(data["preset"])
    octave = int(data["octave"])
  fs.program_select(0, sfid, 0, preset)

readDB()

def play_note(note):
    fs.noteon(0, note, 127)


def stop_note(note):
    fs.noteoff(0, note)

def stopAllNote():
    fs.delete()


once_key1 = [False, False, False, False, False, False, False, False]
once_key2 = [False, False, False, False, False, False, False, False]
once_key3 = [False, False, False, False, False, False, False, False]

#button
presetup_btn = DebouncedButton(17)
presetdown_btn = DebouncedButton(27)

octaveup_btn = DebouncedButton(22)
octavedown_btn = DebouncedButton(23)

#LED

status_on = LED(24)

print("started")

def main_loop():

  try:
    
    FirstDis()

    while running:

      global octave
      global preset

      readDB()
    
      key = I2C.readAllBus()
      status_on.on()
      #button action
      #preset

      if presetup_btn.is_pressed():
        preset += 1
        write_preset(preset)
        if preset > 127:
          preset = 0
          write_preset(preset)
    
        PREDIS(F"Preset : {fs.sfpreset_name(sfid, 0, preset)}") 
        print(F"Preset : {fs.sfpreset_name(sfid, 0, preset)}")

      if presetdown_btn.is_pressed():
        preset -= 1
        write_preset(preset)
        if preset < 0:
          preset = 127
          write_preset(preset)
        
        PREDIS(F"Preset : {fs.sfpreset_name(sfid, 0, preset)}") 
        print(F"Preset : {fs.sfpreset_name(sfid, 0, preset)}")

      #octave
      if octaveup_btn.is_pressed():

    

        if octave < 8:
          octave += 1
         
          PREDIS(F"Octave : {octave}")
          print(F"Octave : {octave}")

      if octavedown_btn.is_pressed():

      

        if octave > 0:
          octave -= 1
         
          PREDIS(F"Octave : {octave}")
          print(F"Octave : {octave}")

      #bus 1
      for i in range(len(key[0])):
        note = 24 + (12 * octave)
        if not key[0][i]:
          if not once_key1[i]:
            play_note(note + i)
            once_key1[i] = True
        else:
          if once_key1[i]:
            stop_note(note + i)
            once_key1[i] = False
    
      #bus2
      for i in range(len(key[1])):
        note = 32 + (12 * octave)
        if not key[1][i]:
          if not once_key2[i]:
            play_note(note + i)
            once_key2[i] = True
        else:
          if once_key2[i]:
            stop_note(note + i)
            once_key2[i] = False

      #bus3
      for i in range(len(key[2])):
        note = 40 + (12 * octave)
        if not key[2][i]:
          if not once_key3[i]:
            play_note(note + i)
            once_key3[i] = True
        else:
          if once_key3[i]:
            stop_note(note + i)
            once_key3[i] = False

  except KeyboardInterrupt:
    I2C.closeAllBus()
    status_on.off()


t1 = threading.Thread(target=main_loop)
t2 = threading.Thread(target=api.runAPI)
t1.start()
t2.start()

t1.join()
t2.join()
