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


@app.route("/float")
def float():
    return render_template("CSS_temp/float.html") 

@app.route("/game")
def mini_game():
    return render_template("JS_temp/lessons/js_minigame.html") 

@app.route("/text")
def text():
    return render_template("CSS_temp/text.html") 

@app.route("/droplist")
def droplist():
    return render_template("CSS_temp/droplist.html") 

@app.route("/transform")
def transform():
    return render_template("CSS_temp/transform.html") 

@app.route("/test")
def test():
    return render_template("CSS_temp/test.html") 

@app.route("/test1")
def test1():
    return render_template("CSS_temp/test1.html") 

@app.route("/type_size")
def type_size():
    return render_template("CSS_temp/type_size.html")    

@app.route("/cards")
def cards():
    return render_template("CSS_temp/cards.html")  

@app.route("/calculators")
def calc_page():
    return render_template("JS_temp/lessons/calculators.html") 

@app.route("/space")
def space():
    return render_template("CSS_temp/space.html")      

@app.route("/switcher")
def switcher():
    return render_template("CSS_temp/lang_switch.html")     