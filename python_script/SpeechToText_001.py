import speech_recognition as sr
r = sr.Recognizer()

import librosa
sample_wav, rate = librosa.core.load('./001.wav')

korean_audio = sr.AudioFile('./001.wav')

with korean_audio as source:
    audio = r.record(source)
output = r.recognize_google(audio_data = audio, language = 'ko-KR')
print(output)
