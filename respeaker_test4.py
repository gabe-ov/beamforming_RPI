import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# configure a PyAudio
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=4, rate=16000, input=True)

# configure o gráfico
fig, axs = plt.subplots(4, 2, figsize=(8, 8))
fig.suptitle('Áudio em tempo real do ReSpeaker')

# crie um objeto Line2D para cada canal
lines = []
for i in range(4):
    line, = axs[i][0].plot([], [], lw=2)
    axs[i][0].set_xlim(0, 1024)
    axs[i][0].set_ylim(-32768, 32767)
    axs[i][0].set_title('Canal {}'.format(i))
    lines.append(line)

# crie um objeto Line2D para o espectro de cada canal
spectral_lines = []
for i in range(4):
    spectral_line, = axs[i][1].plot([], [], lw=2)
    axs[i][1].set_xlim(0, 8000)
    axs[i][1].set_ylim(0, 10)
    axs[i][1].set_title('Canal {} (espectro)'.format(i))
    spectral_lines.append(spectral_line)

# leia continuamente blocos de áudio do stream e atualize o gráfico
while True:
    data = stream.read(1024)
    frames = np.frombuffer(data, dtype=np.int16).reshape(-1, 4)

    # atualize os dados para cada canal
    for i in range(4):
        lines[i].set_data(np.arange(1024), frames[:, i])
        fft = np.fft.fft(frames[:, i])
        freqs = np.fft.fftfreq(len(fft)) * 16000
        spectral_lines[i].set_data(freqs[:len(freqs)//2], np.abs(fft)[:len(fft)//2])

    # atualize o gráfico
    plt.pause(0.01)

plt.show()
