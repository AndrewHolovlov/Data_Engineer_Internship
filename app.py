from flask import Flask

from main import run_parse

app = Flask(__name__)


@app.route("/")
def run():
    run_parse()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
