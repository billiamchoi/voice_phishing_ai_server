import scripts.text_preprocessing as text_preprocessing
import numpy as np
import pandas as pd
from keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import StandardScaler

scaled_X = None

def scale(X, scaler):
    global scaled_X
    for i in range(X.shape[0]):
        scaled_X = scaler.transform(X[:, :])
    return scaled_X

autoencoder = load_model(filepath='models/text_lstm_ae_model.h5')

with open('pickles/ae_tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict_text(user_input):

    user_input = text_preprocessing.okt_test(user_input)
    X_input = []
    x_input_preprocessed = str(user_input)
    token = []
    words = x_input_preprocessed.split(",")
    for word in words:
        token.append(word.lower())
    X_input.append(token)

    tokenizer.fit_on_texts(X_input)
    X_input_encoded = tokenizer.texts_to_sequences(X_input)
    max_len = 85
    X_input_padded = pad_sequences(X_input_encoded, maxlen=int(max_len), padding = 'post', truncating='post')
    X_train = np.load('npys/X_train_post.npy')

    scaler = StandardScaler().fit(X_train)
    X_input_scaled = scale(X_input_padded, scaler)
    # x_train 기준으로 정규화
    input_X_predictions = autoencoder.predict(X_input_scaled, batch_size=64)

    mse = np.mean(np.power(X_input_scaled - input_X_predictions, 2), axis=1)
    error_df = pd.DataFrame({'Reconstruction_error': mse})

    threshold_fixed = 3.6004519942431243 #현재 데이터 그대로 사용할 경우
    y_pred = [1 if e > threshold_fixed else 0 for e in error_df['Reconstruction_error'].values]
    if y_pred == [1]:
        return 1
    else:
        return 0