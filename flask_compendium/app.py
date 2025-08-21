from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/selector_page")
def text_page():
    return render_template("selector.html")

@app.route("/blocks")
def block_page():
    return render_template("blocks.html")

@app.route("/flex")
def flex():
    return render_template("flex.html")

@app.route("/grid")
def grid():
    return render_template("grid.html")    

@app.route("/position")
def position():
    return render_template("position.html") 

@app.route("/inline")
def inline():
    return render_template("inline.html") 