from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!' 

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    
    app.run(host='127.0.0.1', port=8080, debug=True)
