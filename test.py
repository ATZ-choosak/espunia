import fluidsynth
import time
import pygame

fs = fluidsynth.Synth()
fs.start()
sfid = fs.sfload("/home/pi/Desktop/espunia/Arachno.sf2")


fs.setting('synth.gain', 1.00)
fs.program_select(0, sfid, 0, 10)

def play_note(note):
    fs.noteon(0, note, 127)
    
def stop_note(note):
    fs.noteoff(0, note)

Running = True

pygame.init()

pygame.display.set_mode((1280 , 720))

while Running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Running = False
			
		if event.type == pygame.KEYDOWN:
			play_note(ord(event.unicode))
			
		if event.type == pygame.KEYUP:
			stop_note(ord(event.unicode))
			
	
	
pygame.quit()
