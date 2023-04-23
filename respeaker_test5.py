import pyaudio
import numpy as np

# configure a PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=4, rate=16000, input=True)

# leia continuamente blocos de áudio do stream
while True:
    data = stream.read(1024)
    frames = np.frombuffer(data, dtype=np.int16).reshape(-1, 4)
    
    # faça algo com os dados dos canais de áudio...
