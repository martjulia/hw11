from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidates_by_name, get_candidate, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates_from_json()
    return render_template('list.html', x=candidates['name'])


@app.route('/search/<candidate_name>')
def search_by_name(name):
    candidate = get_candidates_by_name(name)
    return render_template('search.html', )


@app.route('/candidate/<int:uid>/')
def candidate_page(uid):
    candidate = get_candidate(uid)
    name = candidate['name']
    position = candidate['position']
    picture = candidate['picture']
    skills = candidate['skills']
    return render_template('card.html', id=uid, name=name, position=position, picture=picture, skills=skills)


app.run()
