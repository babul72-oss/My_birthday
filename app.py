from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "main":
    # Render automatically assigns PORT environment variable
    port = int(os.environ.get("PORT", 10000))  # default 10000 if PORT not set
    app.run(host="0.0.0.0", port=port)