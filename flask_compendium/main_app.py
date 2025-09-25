from flask import Flask, render_template

app = Flask(__name__)

@app.route("test_comp")
def test_comp():
    return render_template("Compendium/main_base.html")