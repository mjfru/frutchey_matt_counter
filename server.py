from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'one of the best lines spoken by gandalf'


@app.route('/', methods=['GET'])
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template('index.html')


@app.route('/add_two', methods=['GET'])
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/custom_number', methods=['POST'])
def custom_number():
    session['counter'] = session['counter'] + int(request.form['custom_number']) - 1
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)