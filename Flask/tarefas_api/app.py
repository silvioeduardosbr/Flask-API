from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/res')
def responsavel():
    return jsonify({'nome':'Silvio'})

if __name__ == '__main__':
    app.run()