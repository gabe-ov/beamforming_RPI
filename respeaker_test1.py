import time
import respeaker

mic = respeaker.Microphone()
mic.rate = 16000
mic.channels = 4

mic.start()


while True:
    frames = mic.read()
    print(frames)

mic.stop()
