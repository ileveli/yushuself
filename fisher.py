from flask import Flask


app = Flask(__name__)

app.run()

@app.route('/hello')
def Hello():
    return 'Hello,Qiyue'