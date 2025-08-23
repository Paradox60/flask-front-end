from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("CSS_temp/index.html")

@app.route("/selector_page")
def text_page():
    return render_template("CSS_temp/selector.html")

@app.route("/blocks")
def block_page():
    return render_template("CSS_temp/blocks.html")

@app.route("/flex")
def flex():
    return render_template("CSS_temp/flex.html")

@app.route("/grid")
def grid():
    return render_template("CSS_temp/grid.html")    

@app.route("/position")
def position():
    return render_template("CSS_temp/position.html") 

@app.route("/inline")
def inline():
    return render_template("CSS_temp/inline.html") 

@app.route("/js_home")
def js_start():
    return render_template("JS_temp/js_index.html") 


@app.route("/js_first_lesson")
def js_fl():
    return render_template("JS_temp/lessons/js_fl.html") 