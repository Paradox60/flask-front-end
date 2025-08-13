from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")

def text_page():
    return render_template("text.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
