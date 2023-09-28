import fluidsynth
import I2C

running = True

preset = 0
reverb = 0.1

fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload("/home/odroid/Desktop/Midi/4.2 ST_Old.sf2")
fs.program_select(0, sfid, 0, preset)

octave = 3


def play_note(note):
    fs.noteon(0, note, 80)


def stop_note(note):
    fs.noteoff(0, note)


once_key1 = [False, False, False, False, False, False, False, False]
once_key2 = [False, False, False, False, False, False, False, False]
once_key3 = [False, False, False, False, False, False, False, False]


while running:

    key = I2C.readAllBus()
    
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

I2C.clseAllBus()
