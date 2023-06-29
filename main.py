import random
from flask import Flask, render_template

app = Flask(__name__)
airs = ["selfair.html","selfair2.html","selfair3.html"]

def cost(price,v,name,shit):
    name=name
    shit=shit
    return price * v

@app.route("/Self_air")
def selfair():
    return render_template(f"{random.choice(airs)}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    return render_template('products.html')

@app.route("/Alp_Fresh/<price>")
def alp_fresh(price):
    return render_template("alpfresh.html", price=price)

@app.route("/rates")
def rates():
    return render_template("rates.html")

@app.route("/Pug's_Fart/<price>")
def pugsfart(price):
    return render_template("pugsfart.html", price=price)

@app.route("/Sea_Breaze/<price>")
def seabreaze(price):
    return render_template("seabreaze.html", price=price)

@app.route("/Alp_Fresh/<price>/V")
def alpfreshv(price):
    return render_template("v.html", price=price)

@app.route("/Pug's_Fart/<price>/V")
def pugsfartv(price):
    return render_template("v.html", price=price)

@app.route("/Sea_Breaze/<price>/V")
def seabreazev(price):
    return render_template("v.html", price=price)

@app.route("/<name>/<shit>/<price>/<v>")
def v(name,shit,price,v):
    return render_template("total.html", result=cost(int(price), float(v), name=0, shit=0))

if __name__ == "__main__":
    app.run(debug=True)