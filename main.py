from flask import Flask

app = Flask(__name__)

@app.route("/")


app.run(debug=True)