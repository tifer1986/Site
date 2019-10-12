from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == 'GET':
        if request.args.get('name') is not '':
           print(f"Nome: {request.args.get('name')} \nSobrenome: {request.args.get('lastName')}\n\
Fone: {request.args.get('fone')}")
        print(request.args.to_dict)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, load_dotenv=True)
