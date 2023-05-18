from flask import Flask, render_template, request, jsonify, Response
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.prmf9xh.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta



@app.route("/", methods=["GET"])
def MBTI_get():
    return render_template('index.html')


@app.route("/data", methods=["GET"])
def MBTI_data():
    all_people = list(db.Introduction.find({}, {'_id': False}))
    return jsonify({'result': all_people})





if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
