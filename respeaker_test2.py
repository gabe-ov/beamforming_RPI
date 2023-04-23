import pyaudio
import numpy as np

# configure a PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=4, rate=16000, input=True)

# leia continuamente blocos de áudio do stream e imprima as aquisições dos 4 canais
while True:
    data = stream.read(1024)
    frames = np.frombuffer(data, dtype=np.int16).reshape(-1, 4)

    # imprima as aquisições de cada canal
    for i in range(4):
        print("Canal {}: {}".format(i, frames[:, i]))
