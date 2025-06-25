from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'rps_secret_key_2024'

CHOICES = {
    "rock": {"emoji": "🪨", "beats": "scissors", "loses_to": "paper"},
    "paper": {"emoji": "📄", "beats": "rock", "loses_to": "scissors"},
    "scissors": {"emoji": "✂️", "beats": "paper", "loses_to": "rock"}
}

WIN_PHRASES = {
    ("rock", "scissors"): "crushes scissors",
    ("paper", "rock"): "covers rock",
    ("scissors", "paper"): "cuts paper"
}

STAT_FILE = 'task 3/statistics.json'

# --- Helper functions ---
def load_statistics():
    try:
        with open(STAT_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        return {}

def save_statistics(data):
    try:
        with open(STAT_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Could not save statistics: {e}")

def get_win_phrase(winner, loser):
    return WIN_PHRASES.get((winner, loser), "beats")

# --- Flask routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    player_name = request.form.get('player_name', 'Anonymous')
    session['player_name'] = player_name
    session['player_score'] = 0
    session['computer_score'] = 0
    session['ties'] = 0
    session['games_played'] = 0
    session['game_history'] = []
    session['game_state'] = 'playing'
    return redirect(url_for('play'))

@app.route('/play')
def play():
    if 'game_state' not in session:
        return redirect(url_for('index'))
    return render_template('play.html',
        player_name=session['player_name'],
        player_score=session['player_score'],
        computer_score=session['computer_score'],
        ties=session['ties'],
        games_played=session['games_played'],
        game_history=session['game_history'][-10:],
        choices=CHOICES)

@app.route('/make_move', methods=['POST'])
def make_move():
    if 'game_state' not in session:
        return jsonify({'error': 'Session expired.'})
    player_choice = request.form.get('choice')
    if player_choice not in CHOICES:
        return jsonify({'error': 'Invalid choice.'})
    computer_choice = random.choice(list(CHOICES.keys()))
    if player_choice == computer_choice:
        result = 'tie'
        session['ties'] += 1
    elif CHOICES[player_choice]['beats'] == computer_choice:
        result = 'player'
        session['player_score'] += 1
    else:
        result = 'computer'
        session['computer_score'] += 1
    session['games_played'] += 1
    # Save round to history
    round_data = {
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
        'player_score': session['player_score'],
        'computer_score': session['computer_score'],
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if 'game_history' not in session:
        session['game_history'] = []
    session['game_history'].append(round_data)
    if len(session['game_history']) > 50:
        session['game_history'] = session['game_history'][-50:]
    # Prepare response
    phrase = ''
    if result == 'player':
        phrase = get_win_phrase(player_choice, computer_choice)
    elif result == 'computer':
        phrase = get_win_phrase(computer_choice, player_choice)
    return jsonify({
        'player_choice': player_choice,
        'player_emoji': CHOICES[player_choice]['emoji'],
        'computer_choice': computer_choice,
        'computer_emoji': CHOICES[computer_choice]['emoji'],
        'result': result,
        'phrase': phrase,
        'player_score': session['player_score'],
        'computer_score': session['computer_score'],
        'ties': session['ties'],
        'games_played': session['games_played']
    })

@app.route('/statistics')
def statistics():
    if 'player_name' not in session:
        return redirect(url_for('index'))
    # Calculate stats
    games_played = session.get('games_played', 0)
    player_score = session.get('player_score', 0)
    computer_score = session.get('computer_score', 0)
    ties = session.get('ties', 0)
    win_rate = (player_score / games_played * 100) if games_played > 0 else 0
    loss_rate = (computer_score / games_played * 100) if games_played > 0 else 0
    tie_rate = (ties / games_played * 100) if games_played > 0 else 0
    # Choice analysis
    game_history = session.get('game_history', [])
    player_choices = [g['player_choice'] for g in game_history]
    choice_counts = {c: player_choices.count(c) for c in CHOICES}
    return render_template('statistics.html',
        player_name=session['player_name'],
        games_played=games_played,
        player_score=player_score,
        computer_score=computer_score,
        ties=ties,
        win_rate=win_rate,
        loss_rate=loss_rate,
        tie_rate=tie_rate,
        choice_counts=choice_counts,
        choices=CHOICES)

@app.route('/history')
def history():
    if 'player_name' not in session:
        return redirect(url_for('index'))
    game_history = session.get('game_history', [])[-10:]
    return render_template('history.html',
        player_name=session['player_name'],
        game_history=game_history,
        choices=CHOICES)

@app.route('/results')
def results():
    if 'player_name' not in session:
        return redirect(url_for('index'))
    games_played = session.get('games_played', 0)
    player_score = session.get('player_score', 0)
    computer_score = session.get('computer_score', 0)
    ties = session.get('ties', 0)
    win_rate = (player_score / games_played * 100) if games_played > 0 else 0
    # Save stats to file
    stats_data = {
        'player_name': session['player_name'],
        'total_games': games_played,
        'player_wins': player_score,
        'computer_wins': computer_score,
        'ties': ties,
        'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'game_history': session.get('game_history', [])[-20:]
    }
    save_statistics(stats_data)
    return render_template('results.html',
        player_name=session['player_name'],
        games_played=games_played,
        player_score=player_score,
        computer_score=computer_score,
        ties=ties,
        win_rate=win_rate)

@app.route('/play_again')
def play_again():
    # Reset scores but keep name
    player_name = session.get('player_name', 'Anonymous')
    session.clear()
    session['player_name'] = player_name
    session['player_score'] = 0
    session['computer_score'] = 0
    session['ties'] = 0
    session['games_played'] = 0
    session['game_history'] = []
    session['game_state'] = 'playing'
    return redirect(url_for('play'))

@app.route('/reset_session')
def reset_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002) 