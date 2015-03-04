#subprocess.Popen(['omxplayer','airrif1_goodcut.wav'], stdout = True)
import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import glob

#Set Play directories and track counter to loop
tracks = 0
dirnum = 0
playdir = ['shortriff', 'expertriff', 'freebird']
trackloop = glob.glob(playdir[dirnum]+'/*.wav')

#Set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN)

#Activate PyGame
pygame.mixer.init(44100, -16, 2, 1024)
pygame.mixer.Sound.set_volume(1)

#Set initial Mixer Directory
sndA = pygame.mixer.Sound(trackloop[tracks-1])
#sndB = pygame.mixer.Sound("clap.wav")
#sndC = pygame.mixer.Sound("laugh.wav")
soundChannelA = pygame.mixer.Channel(1)
#soundChannelB = pygame.mixer.Channel(2)
#soundChannelC = pygame.mixer.Channel(3)

print "Sound Volume"
print pygame.mixer.Sound.get_volume()
print "Channel Volume"
print pygame.mixer.Channel.get_volume()
print "Soundboard Ready."

while True:
    try:
        if (GPIO.input(22) == False):
            print tracks
            print trackloop[tracks-1]
            soundChannelA.play(sndA)
            tracks += 1
            if (tracks >= len(trackloop)):
                tracks = 0
            sndA = pygame.mixer.Sound(trackloop[tracks-1])
            #subprocess.call("omxplayer -o local airrif1_goodcut.wav")
            sleep(3)
        #if (GPIO.input(24) == False):
            print "Chaning Play Directory"
            playdir += 1
            tracks = 0
            trackloop = glob.glob(playdir[dirnum]+'/*.wav')
            sndA = pygame.mixer.Sound(trackloop[tracks-1])
        #if (GPIO.input(25) == True):
            #soundChannelC.play(sndC)
        sleep(0.1)
    except KeyboardInterrupt:
        exit()
