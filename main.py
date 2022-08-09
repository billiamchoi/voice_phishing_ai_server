from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='voice_ai', charset="utf8")
cursor = db.cursor()

@app.route("/api", methods=["GET"])
def get_text():
	sql = "select * from stt_text"
	cursor.execute(sql)
	results = cursor.fetchall()
	db.commit()
	# print(results)
	# results = ((1, '안녕하세요'), (2, 'Hello'))
	stts = []
	for result in results:
		stts.append({
			'id': result[0],
			'stt_text': result[1]
		})
	return jsonify(stts)

@app.route("/api", methods=["POST"])
def save_text():
	server_text = request.json["stttext"]
	sql = "insert into stt_text (stttext) values ('%s')" %(server_text)
	cursor.execute(sql)
	db.commit()
	return "save OK"

if __name__ == "__main__":
    app.run(debug=True)