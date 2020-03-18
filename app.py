#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! test dummyProjec 2"
	
@app.route('/test')
def indexx():
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)