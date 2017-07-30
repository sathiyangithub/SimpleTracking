from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route('/invokeClick.html', methods=['POST'])
def invokeClick():
    print(' IdVar ',request.args.get("IdVar"));
    print(' useragent ',request.args.get("useragentStr"));
    print(' cookie ', request.args.get("cookie"));
    print(' location ', request.args.get("location"));
    print(' event ', request.args.get("event"));

    # persist this attribute info into database

@app.route('/trackingSuccess.html')
def trackingSuccess():
    print('tracking Success')
    return render_template('trackingSuccess.html')


if __name__ == '__main__':
    app.run()
