from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def root():
    f = open("../frontend/index.html")
    return f.read()

@app.route('/world.svg')
def world():
    f = open("../frontend/world.svg")
    return Response(f.read(), mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run()