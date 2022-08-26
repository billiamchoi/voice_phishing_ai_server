from flask import Flask
from flask import request
import pymysql
from settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import os
import scripts.text_lstm_model as text_model
import scripts.voice_lstm_model as voice_model

db = pymysql.connect(host='localhost', port=3306, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset="utf8")
cursor = db.cursor()
db.autocommit(True)
UPLOAD_DIRECTORY = "./voice_files"
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def main():
	return "ok"

@app.route("/api/stt_text", methods=["POST"])
def create_stt_text():
	text = request.json["text"]
	first_sql = """ insert into stt_text (text) values ('%s') """ % text
	cursor.execute(first_sql)
	stt_text_id = cursor.lastrowid
	db.commit()
	second_sql = """ update stt_text_seg set stt_text_id = '%s' where stt_text_id is null """ % stt_text_id
	cursor.execute(second_sql)
	db.commit()
	score = str(text_model.predict_text(text)[0][0])
	return score

@app.route("/api/stt_text_seg", methods=["POST"])
def create_stt_text_seg():
	text = request.json["text"]
	sql = """ insert into stt_text_seg (text) values ('%s') """ % text
	cursor.execute(sql)
	db.commit()
	score = str(text_model.predict_text(text)[0][0])
	return score

@app.route("/api/stt_voice", methods=["POST"])
def create_stt_voice():
	if 'file' not in request.files:
		return "No file found"
	file = request.files['file']
	file_name = request.form['file_name']
	file.save("""voice_files/whole/%s.wav""" % file_name)
	return "file successfully saved"

@app.route("/api/stt_voice_seg", methods=["POST"])
def create_stt_voice_seg():
	if 'file' not in request.files:
		return "No file found"
	file = request.files['file']
	file_name = request.form['file_name']
	directory_name = request.form['directory_name']
	sr = request.form['sr']
	second = request.form['second']
	file_path = """voice_files/segment/%s/%s.wav""" % (directory_name, file_name)
	file.save(file_path)
	score = str(voice_model.predict_voice(file_path, sr, 40, second))
	return score

@app.route("/api/start_record", methods=["POST"])
def start_record():
	file_name = request.json['file_name']
	os.mkdir("""voice_files/segment/%s""" % file_name)
	return "ok"


if __name__ == "__main__":
	app.run(debug=True)

