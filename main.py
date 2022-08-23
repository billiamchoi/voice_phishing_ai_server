from flask import Flask
from flask import request
import pymysql
from settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
import uuid
import scripts.text_lstm_model as text_model

db = pymysql.connect(host='localhost', port=3306, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, charset="utf8")
cursor = db.cursor()
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
def upload_file():
	if 'file' not in request.files:
		return "No file found"
	file = request.files['file']
	file_name = uuid.uuid4()
	file.save("""voice_files/%s.wav""" % file_name)
	return "file successfully saved"

if __name__ == "__main__":
	app.run(debug=True)

