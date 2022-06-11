from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    name = 'Nick'
    return render_template('profile.html', name=name)


app.run()
