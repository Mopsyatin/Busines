from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/products')
def products():
    return render_template('products.html')

@app.route("/Alp_fresh")
def alp_fresh():
    return render_template("alpfresh.html")

if __name__ == "__main__":
    app.run(debug=True)