from keras.models import load_model
import librosa
import numpy as np

model = load_model(filepath='models/model4.h5')

def padding(mel_spec, sr, second):
    #501 이해하고 dynamic 하게 짜야됨 ## mfcc_array -> mel_spec으로 수정
    if(len(mel_spec[0])<= 3001): # 500->3001로 수정
        z = np.zeros((len(mel_spec), 3001-(len(mel_spec[0]))), dtype=int)
        result = np.append(mel_spec, z, axis=1)
    else:
        # 여기 501도 mfcc 조합에 따라 다 바뀌어야 함
        result = mel_spec[:,0:501]
    return result

def predict_voice_mfcc(wav_file, sr, n_mfcc, second):
    sr = int(sr)
    second = int(second)
    data, sr = librosa.load(wav_file, sr=sr)
    mfcc = librosa.feature.mfcc(np.array(data), sr=sr, n_fft=400, hop_length=160, n_mfcc=n_mfcc)
    result_mfcc = padding(mfcc, sr, second)
    result_mfcc = np.expand_dims(result_mfcc, axis=0)
    return np.mean(model.predict(result_mfcc)[0])

def predict_voice_mel(wav_file, sr, n_mels, second):
    sr = int(sr)
    second = int(second)
    data, sr = librosa.load(wav_file, sr=sr)
    mel = librosa.feature.melspectrogram(y=np.array(data), sr=sr, hop_length=160, n_mels=n_mels)
    # parameters중 "n_fft=400"은 삭제(모델에 없는 param)
    result_mel = padding(mel, sr, second)
    result_mel = np.expand_dims(result_mel, axis=0)
    return np.mean(model.predict(result_mel)[0]) # mean, 왜?
    # mfcc를 mel로 바꾸긴 했다. 잘 동작하는가를 알아보려면 테스트가 필요하다.
