from keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

with open('pickles/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('models/text_lstm_model.h5')

stop_words = ['이', '있', '하', '것', '들', '그', '되', '수', '이', '보', '않', '없', '나', '사람', '주', '아니', '등', '같', '우리', '때', '년', '가', '한', '지', '대하', '오', '말', '일', '그렇', '위하', '때문', '그것', '두', '말하', '알', '그러나', '받', '못하', '일', '그런', '또', '문제', '더', '사회', '많', '그리고', '좋', '크', '따르', '중', '나오', '가지', '씨', '시키', '만들', '지금', '생각하', '그러', '속', '하나', '집', '살', '모르', '적', '월', '데', '자신', '안', '어떤', '내', '내', '경우', '명', '생각', '시간', '그녀', '다시', '이런', '앞', '보이', '번', '나', '다른', '어떻', '여자', '개', '전', '들', '사실', '이렇', '점', '싶', '말', '정도', '좀', '원', '잘', '통하', '소리', '놓']

max_len = 450

def predict_text(input_text):
    user_input = input_text.split()


    user_data = [[]]
    for word in user_input:
        if word not in stop_words:
            user_data[0].append(word.lower())

    user_data = tokenizer.texts_to_sequences(user_data)
    user_data = pad_sequences(user_data, maxlen=max_len)

    if (model.predict(user_data) > 0.5):
        return print(model.predict(user_data), '이것은 보이스피싱입니다')
    else:
        return print(model.predict(user_data), '이것은 보이스피싱이 아닙니다')


