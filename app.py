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







@app.route("/comment/save", methods=["POST"])
def team_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    password_receive = request.form['password_give']

    doc = {
        'name' : name_receive,
        'comment' : comment_receive,
        'password' : password_receive
    }
    db.team.insert_one(doc)

    return jsonify({'msg': '저장완료'})

@app.route("/comment/delete", methods=["POST"])
def team_delete_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    obj_id = ObjectId(id_receive)
    # id = "ObjectId('"+id_receive+"')"
    # print(id)
    # print(password_receive)
    ori_pass = list(db.team.find({'_id' : obj_id}))[0]['password']
    # print(ori_pass)
    # return jsonify({'msg': '응답'})
    print(ori_pass)

    if ori_pass == password_receive:
        
        doc = {
            '_id' : obj_id
        }
        # print(doc)
        db.team.delete_one(doc)
        return jsonify({'msg': '삭제완료'})
    else:
        return jsonify({'msg': '비밀번호가 틀립니다'})
    

@app.route("/comment/edit", methods=["POST"])
def team_edit_post():
    id_receive = request.form['id_give']
    password_receive = request.form['password_give']
    comment_receive = request.form['comment_give']


    obj_id = ObjectId(id_receive)
    # id = "ObjectId('"+id_receive+"')"
    # print(id)

    ori_pass = list(db.team.find({'_id' : obj_id}))[0]['password']
    # print(ori_pass)
    # return jsonify({'msg': '응답'})

    if ori_pass == password_receive:
        db.team.update_one({'_id': obj_id}, {"$set":{'comment':comment_receive}})

        # doc = {
        #     '_id' : obj_id
        # }
        # print(doc)
        # db.fan.delete_one(doc)
        return jsonify({'msg': '수정완료'})
    else:
        return jsonify({'msg': '비밀번호가 틀립니다'})


    

@app.route("/comment/get", methods=["GET"])
# def guestbook_get():
#     all_fans = list(db.fan.find({}))
#     json_all_fans = json.dumps(str(all_fans), ensure_ascii=False)
#     return jsonify({'result': json_all_fans})

def team_get():
    all_teams = list(db.team.find({}))
    # print(dumps(all_teams))
    return jsonify({'result': dumps(all_teams)})



if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
