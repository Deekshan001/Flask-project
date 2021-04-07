from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def stack():
    return render_template("stack.html")

@app.route("/queue")
def queue():
    return render_template("queue.html")

@app.route("/stackArr")
def stackArr():
    return render_template("stackArr.html")

@app.route("/queueLL")
def queueLL():
    return render_template("queueLL.html")

@app.route("/queueArr")
def queueArr():
    return render_template("queueArr.html")

@app.route("/stackLL")
def stackLL():
    return render_template("stackLL.html")

if __name__ == "__main__":
    app.run(debug=True)

