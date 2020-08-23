from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diet', methods=['GET'])
def read_diets():
   diets = list(db.kcal.find({}, {'_id': False}))
# 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
   return jsonify({'result': 'success', 'diets_list': diets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



