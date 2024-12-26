from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def root():
    f = open("../frontend/index.html")
    return f.read()

@app.route('/gps')
def gps():
    f = open("../frontend/gps/index.html")
    return f.read()
@app.route('/gps/')
def gpss():
    f = open("../frontend/gps/index.html")
    return f.read()

@app.route('/options')
def options():
    f = open("../frontend/options/index.html")
    return f.read()
@app.route('/options/')
def optionss():
    f = open("../frontend/options/index.html")
    return f.read()

@app.route('/account')
def account():
    f = open("../frontend/account/index.html")
    return f.read()
@app.route('/account/')
def accountt():
    f = open("../frontend/account/index.html")
    return f.read()

@app.route('/world.svg')
def world():
    f = open("../frontend/world.svg")
    return Response(f.read(), mimetype='image/svg+xml')

@app.route('/boundries.svg')
def boundries():
    f = open("../frontend/boundries.svg")
    return Response(f.read(), mimetype='image/svg+xml')

@app.route('/originalworld.svg')
def originalworld():
    f = open("../frontend/originalworld.svg")
    return Response(f.read(), mimetype='image/svg+xml')

if __name__ == '__main__':
    app.run()