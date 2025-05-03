
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, from Flask in Wasmer Edge"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
