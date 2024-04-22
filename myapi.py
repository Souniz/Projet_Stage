from flask import Flask, request, jsonify
from chat import reponse_chat
from flask_cors import CORS
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
@app.route('/myapi',methods=['POST'])

def my_api():
    question = request.json['question']
    reponsee = reponse_chat(question)
    return jsonify({"reponse": reponsee})

if __name__ == '__main__':
    app.run(debug=True)