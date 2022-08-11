from flask import Flask
from flask import request
import pymysql
from settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB


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
	sql = """ insert into stt_text (text) values ('%s') """ % text
	cursor.execute(sql)
	db.commit()
	return "OK"

@app.route("/api/stt_voice", methods=["POST"])
def upload_file():
	if 'file' not in request.files:
		return "No file found"
	file = request.files['file']
	file_name = request.form['file_name']
	file.save("""voice_files/%s.wav""" % file_name)
	return "file successfully saved"

if __name__ == "__main__":
	app.run(debug=True)

