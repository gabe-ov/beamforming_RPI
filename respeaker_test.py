import time
import numpy as np
import matplotlib.pyplot as plt
import respeaker

# configure o gráfico
plt.ion()
fig, axs = plt.subplots(4, 1, figsize=(8, 8))
lines = [ax.plot(np.arange(0, 1000), np.zeros(1000))[0] for ax in axs]

# configure o microfone
mic = respeaker.Microphone()
mic.rate = 16000
mic.channels = 4

mic.start()

while True:
    # leia um bloco de áudio de todos os 4 canais
    frames = mic.read()

    # atualize os valores de amplitude do gráfico
    for i in range(4):
        lines[i].set_ydata(frames[:, i])
        axs[i].relim()
        axs[i].autoscale_view()

    # atualize o gráfico
    fig.canvas.draw()
    fig.canvas.flush_events()

    # espere um pouco antes de ler o próximo bloco de áudio
    time.sleep(0.01)

mic.stop()
