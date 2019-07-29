# wyld_stallyns
Want your own personal air guitar? Be Excellent with this exceptional python sound board. This script is designed to run on a Raspberry Pi with at least 2 available GPIO inputs. Security system trip sensors (normally closed circuit) are attached to the GPIO.
Once the circuit is opened, the loaded soundfile will begin playing until the sample ends or the contact closes again. The player will pause mid-play if the contact closes, but the soundfile has not finished.
Multiple soundfiles can be looped so long as they are in the same directory.

A few important notes
-This python player depends on OMXPlayer, a native Rasbperry player. Make sure to apt-get prior to use
