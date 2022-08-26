from keras.models import load_model
import librosa
import numpy as np

model = load_model(filepath='models/voice_lstm_model.h5')

def padding(mfcc_array, sr, second):
    #501 이해하고 dynamic 하게 짜야됨
    if(len(mfcc_array[0])<= 501):
        z = np.zeros((len(mfcc_array),501-(len(mfcc_array[0]))), dtype = int)
        result = np.append(mfcc_array, z, axis = 1)
    else:
        # 여기 501도 mfcc 조합에 따라 다 바뀌어야 함
        result = mfcc_array[:,0:501]
    return result

def predict_voice(wav_file, sr, n_mfcc, second):
    sr = int(sr)
    second = int(second)
    data, sr = librosa.load(wav_file, sr=sr)
    mfcc = librosa.feature.mfcc(np.array(data), sr=sr, n_fft=400, hop_length=160, n_mfcc=n_mfcc)
    result_mfcc = padding(mfcc, sr, second)
    result_mfcc = np.expand_dims(result_mfcc, axis=0)
    return np.mean(model.predict(result_mfcc)[0])

