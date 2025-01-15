from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/data',methods =['GET'])
def get_data():
    return jsonify({'key':'value'})
if __name__ == '__main__':
    app.run(debug=True)