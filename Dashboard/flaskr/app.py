from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "Hackathon 2017"

@app.route('/police')
def police():
    return render_template('police.html')

@app.route('/fire')
def fire():
    return render_template('fire.html')

@app.route('/ambulance')
def ambulance():
    return render_template('ambulance.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
