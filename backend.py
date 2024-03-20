# python file

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This is the index"


app.run(host="0.0.0.0", port=80)

