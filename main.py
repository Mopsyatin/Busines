from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/products.html')
def products():
    return render_template('products.html')

if __name__ == "__main__":
    app.run(debug=True)