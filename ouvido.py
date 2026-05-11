
import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer


# Carregar o modelo grande
model = Model(r"vosk_models/vosk-model-pt-fb-v0.1.1-20220516_2113")
rec = KaldiRecognizer(model, 16000)
q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

def escuta():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Fale algo...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                resultado = json.loads(rec.Result())
                texto = resultado["text"]

                if texto != "":
                    return texto




