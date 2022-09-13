from keras.models import load_model
import librosa
import numpy as np

model = load_model(filepath='models/model3.h5')

def padding(mel_spec, sr, second):
    #501 이해하고 dynamic 하게 짜야됨
    if(len(mel_spec[0])<= 501):
        z = np.zeros((len(mel_spec), 501-(len(mel_spec[0]))), dtype=int)
        result = np.append(mel_spec, z, axis=1)
    else:
        # 여기 501도 mfcc 조합에 따라 다 바뀌어야 함
        result = mel_spec[:,0:501]
    return result.reshape(-1,20040)

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
    result_mel = padding(mel, sr, second)
    result_mel = np.expand_dims(result_mel, axis=0)
    pre_result_mel = model.predict(result_mel)
    mse = np.mean(np.power(result_mel - pre_result_mel, 2))
    error_df = pd.DataFrame({'Reconstruction_error': mse})
    vo_threshold_fixed = 267
    ab_pred = [1 if e > vo_threshold_fixed else 0 for e in error_df['Reconstruction_error'].values]
    if y_pred == [1]:
        return 1
    else:
        return 0
    return pre_result_mel 
