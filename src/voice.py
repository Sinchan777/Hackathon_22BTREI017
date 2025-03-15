import sounddevice as sd
import numpy as np
from ctranslate2 import Translator
from whisper.audio import log_mel_spectrogram
from TTS.api import TTS

class VoiceEngine:
    def __init__(self):
        self.stt_model = Translator("medium", device="cpu")
        self.sample_rate = 16000
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", gpu=False)

    def listen(self) -> str:
        audio = sd.rec(int(10 * self.sample_rate), 
                      samplerate=self.sample_rate,
                      channels=1,
                      dtype=np.float32)
        sd.wait()
        mel = log_mel_spectrogram(audio.flatten()).numpy().astype(np.float32)
        return self.stt_model.generate({"input_features": [mel]})[0].hypotheses[0]

    def speak(self, text: str):
        audio = self.tts.tts(text)
        sd.play(audio, samplerate=22050)
        sd.wait()