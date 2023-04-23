import pyaudio

# Definir parâmetros de gravação
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 4
RATE = 16000
RECORD_SECONDS = 5

# Inicializar o PyAudio
p = pyaudio.PyAudio()

# Abre um stream de gravação
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Grava o áudio
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Para o stream de gravação
stream.stop_stream()
stream.close()
p.terminate()

# Inicializa o PyAudio novamente para reproduzir o áudio gravado
p = pyaudio.PyAudio()

# Abre um stream de reprodução
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)

# Reproduz o áudio gravado
for data in frames:
    stream.write(data)

# Para o stream de reprodução
stream.stop_stream()
stream.close()
p.terminate()
