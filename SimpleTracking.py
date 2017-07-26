from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route('/invokeClick.html', methods=['POST'])
def invokeClick():
    # this method to get cookie and url and user agent and persist same into database
    print(' invoke click is invoked')


@app.route('/trackingSuccess.html')
def trackingSuccess():
    print('tracking Success')
    return render_template('trackingSuccess.html')


if __name__ == '__main__':
    app.run()
