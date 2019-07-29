import subprocess
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import glob

#Set Play directories and track counter to loop
tracks = 0
dirnum = 0
#playnow = 0
playdir = ['shortriff', 'expertriff', 'freebird']
trackloop = glob.glob(playdir[dirnum]+'/*.wav')
#trackloops = map(lambda d: glob.glob(d + '/*.wav'), playdir)

#Set GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN)

print "Soundboard Ready."

shouldPlay = False
isPlaying = False
print trackloop[tracks-1]

playprocess = ''
def loadTrack():
    global playprocess
    playprocess = subprocess.Popen(['omxplayer', '-o','local','-w',trackloop[tracks-1]],stdin=subprocess.PIPE)
    playprocess.stdin.write('p')

def pauseTrack():
    global playprocess
    playprocess.poll()
    print "pauseTrack"
    print playprocess.returncode
    if playprocess.returncode is None:
        playprocess.stdin.write('p')

def quitTrack():
    global playprocess
    print "quitTrack"
    playprocess.poll()
    print playprocess.returncode
    if playprocess.returncode is None:
        playprocess.stdin.write('q')

loadTrack()
while True:
    try:
        # Should start playing
        if (GPIO.input(22) == False):
            print "should play"
            shouldPlay = True
            #sleep(3)
        else:
            # print "should not play"
            shouldPlay = False

		# Air Guitar activated! 
        if shouldPlay and isPlaying is False:
            print "start playing!"
            isPlaying = True
            print tracks
            print trackloop[tracks-1]
            pauseTrack()
            sleep(1)
            tracks += 1
            if (tracks >= len(trackloop)):
                tracks = 0
                #playnow = 0
			loadTrack()
        if shouldPlay is False and isPlaying:
            print "stop playing!"
            isPlaying = False
            pauseTrack()
            sleep(1)

        if (GPIO.input(24) == False):
            print "Changing Play Directory"
            quitTrack()
            sleep(0.5)
            dirnum += 1
            tracks = 0
            #playnow = 0
            if (dirnum >= len(playdir)):
                dirnum = 0
            trackloop = glob.glob(playdir[dirnum]+'/*.wav')
            print playdir[dirnum]

            # load up next song
            quitTrack()
            sleep(1)
            loadTrack()
        #if (GPIO.input(25) == True):
            #soundChannelC.play(sndC)
        sleep(0.1)
    except KeyboardInterrupt:
        exit()
