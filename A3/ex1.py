from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def hello():
    return "Hello World!"

@app.route('/suma', method=['GET'])
def suma():
    numero1 = request.args.get ('a')
    print( numero1)
    numero2 = request.args.get ('b')
    print( numero2)
    return "La suma de ", numero1, " +", numero2, " es= ", (numero1+ numero2)

if __name__ == '__main__':
    app.run(debug=True)

