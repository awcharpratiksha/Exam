from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return """
    <h1>Welcome to ITIL exam</h1>
    <p>PRN number = 230344223006</p>
    <p>Name = Pratiksha Awchar</p>
    <p>Phone number = 9096373619</p>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)


