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

@app.route("/item_list")
def item_list():
    return render_template("CSS_temp/item_list.html")

@app.route("/page_item_list")
def page_item_list():
    return render_template("CSS_temp/page_item_list.html")

@app.route("/content_switcher")
def content_switcher():
    return render_template("CSS_temp/content_switcher.html")


@app.route("/cutting_calc")
def cutting_calc():
    return render_template("CSS_temp/cutting_calc.html")

@app.route("/linergradient")
def linergradient():
    return render_template("CSS_temp/linergradient.html")

@app.route("/empty_page")
def empty_page():
    return render_template("CSS_temp/empty_page.html")

@app.route("/cutting_parameters")
def cutting_parameters():
    return render_template("CSS_temp/cutting_parameters.html")

@app.route("/drop_menu")
def drop_menu():
    return render_template("CSS_temp/drop_menu.html")

@app.route("/calculator_label")
def calculator_label():
    return render_template("CSS_temp/calculator_label.html")
    
@app.route("/graph")
def graph():
    return render_template("CSS_temp/graph.html")
        
@app.route("/formulas")
def formulas():
    return render_template("CSS_temp/formulas.html")