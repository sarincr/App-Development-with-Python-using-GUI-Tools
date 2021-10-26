from flask import Flask
from pyfladesk import init_gui
from routes import *

app = Flask(__name__)




@app.route("/")
def index():
    return "Hello World!"



if __name__ == '__main__':
    init_gui(app)
