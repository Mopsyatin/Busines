import random
from flask import Flask, render_template

app = Flask(__name__)
airs = ["selfair.html","selfair2.html","selfair3.html"]

qiymet = 0
def result():
    global qiymet
    qiymet = str(qiymet)
    return qiymet

@app.route("/Self_air")
def selfair():
    return render_template(f"{random.choice(airs)}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    return render_template('products.html')

@app.route("/Alp_fresh")
def alp_fresh():
    return render_template("alpfresh.html")

@app.route("/rates")
def rates():
    return render_template("rates.html")

@app.route("/Pug's_fart")
def pugsfart():
    return render_template("pugsfart.html")

@app.route("/Sea_breaze")
def seabreaze():
    return render_template("seabreaze.html")



if __name__ == "__main__":
    app.run(debug=True)