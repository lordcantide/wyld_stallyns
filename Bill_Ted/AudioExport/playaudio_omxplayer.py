import subprocess
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import glob

#Set Play directories and track counter to loop
tracks = 0
dirnum = 0
playnow = 0
playdir = ['shortriff', 'expertriff', 'freebird']
trackloop = glob.glob(playdir[dirnum]+'/*.wav')

trackloops = map(lambda d: glob.glob(d + '/*.wav'), playdir)

#Set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN)

print "Soundboard Ready."

while True:
    #Load track and pause it (essentially preloading track)
    if (playnow == tracks):
        playprocess = subprocess.Popen(['omxplayer','-o','local','-w',trackloop[tracks-1]],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, close_fds=True)
        playprocess.stdin.write('p')
        playnow = tracks + 1
    try:
        if (GPIO.input(22) == False):
            print tracks
            print trackloop[tracks-1]
            playprocess.stdin.write('p')
            tracks += 1
            if (tracks >= len(trackloop)):
                tracks = 0
                playnow = 0
            sleep(3)
        if (GPIO.input(24) == False):
            print "Changing Play Directory"
            playprocess.stdin.write('q')
            dirnum += 1
            tracks = 0
            playnow = 0
            if (dirnum >= len(playdir)):
                dirnum = 0
            trackloop = glob.glob(playdir[dirnum]+'/*.wav')
            print playdir[dirnum]
            sleep(3)
        #if (GPIO.input(25) == True):
            #soundChannelC.play(sndC)
        sleep(0.1)
    except KeyboardInterrupt:
        exit()
