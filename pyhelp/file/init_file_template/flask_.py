def flask_1():
    return """import flask\n\n"""
def flask_2():
    return """app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello,Flask!"
"""
def flask_3():
    return """
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5000',debug=True)"""