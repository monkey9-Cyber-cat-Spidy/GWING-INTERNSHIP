from flask import Flask, render_template, request, redirect, url_for, session
from kingdom_of_shadows import KingdomOfShadowsGame
import os
import json

app = Flask(__name__)
app.secret_key = 'kingdom_of_shadows_secret_key'
SAVE_FILE = 'game_state.json'

# --- Helper functions ---
def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            data = json.load(f)
        return KingdomOfShadowsGame(
            state=data['character'],
            current_node=data.get('current_node', 'prologue'),
            ended=data.get('ended', False),
            epilogue=data.get('epilogue')
        )
    return None

def save_game(game):
    game.save(SAVE_FILE)

# --- Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        game = KingdomOfShadowsGame(name=name)
        save_game(game)
        session['active'] = True
        return redirect(url_for('play'))
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    game = load_game()
    if not game:
        return redirect(url_for('index'))
    if request.method == 'POST':
        choice = int(request.form.get('choice', -1))
        game.make_choice(choice)
        save_game(game)
        if game.is_ended():
            return redirect(url_for('ending'))
        return redirect(url_for('play'))
    text, choices = game.get_current_story()
    stats = game.get_stats()
    return render_template('play.html', text=text, choices=choices, stats=stats)

@app.route('/ending')
def ending():
    game = load_game()
    if not game or not game.is_ended():
        return redirect(url_for('play'))
    epilogue = game.get_epilogue()
    stats = game.get_stats()
    return render_template('ending.html', epilogue=epilogue, stats=stats)

@app.route('/restart')
def restart():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
    session.pop('active', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 