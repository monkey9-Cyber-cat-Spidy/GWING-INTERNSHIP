from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import json
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'number_guessing_secret_key_2024'

class NumberGuessingGame:
    def __init__(self):
        self.difficulty_levels = {
            "easy": {"range": (1, 50), "attempts": 10, "points": 100},
            "medium": {"range": (1, 100), "attempts": 8, "points": 200},
            "hard": {"range": (1, 200), "attempts": 6, "points": 300},
            "expert": {"range": (1, 500), "attempts": 5, "points": 500}
        }
        self.high_scores = self.load_high_scores()
    
    def get_hint(self, secret_number, attempt, max_attempts):
        """Provide helpful hints based on attempt number"""
        if attempt == max_attempts // 2:
            if secret_number % 2 == 0:
                return "💡 Hint: The number is even!"
            else:
                return "💡 Hint: The number is odd!"
        elif attempt == max_attempts * 3 // 4:
            if secret_number <= 50:
                return "💡 Hint: The number is 50 or less!"
            else:
                return "💡 Hint: The number is greater than 50!"
        elif attempt == max_attempts - 1:
            # Last attempt hint
            if secret_number <= 25:
                return "💡 Hint: The number is 25 or less!"
            elif secret_number <= 75:
                return "💡 Hint: The number is between 26 and 75!"
            else:
                return "💡 Hint: The number is greater than 75!"
        return None
    
    def calculate_score(self, attempts_used, max_attempts, base_points):
        """Calculate score based on attempts used"""
        if attempts_used <= max_attempts:
            # More points for fewer attempts
            efficiency = (max_attempts - attempts_used + 1) / max_attempts
            return int(base_points * efficiency)
        return 0
    
    def load_high_scores(self):
        """Load high scores from file"""
        try:
            with open('task 2/high_scores.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_high_scores_to_file(self):
        """Save high scores to file"""
        try:
            with open('task 2/high_scores.json', 'w') as f:
                json.dump(self.high_scores, f, indent=2)
        except Exception as e:
            print(f"Could not save high scores: {e}")
    
    def save_high_score(self, player_name, score, difficulty):
        """Save current score to high scores if it's good enough"""
        if score > 0:
            score_data = {
                'name': player_name,
                'score': score,
                'difficulty': difficulty,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            # Check if this is a new high score
            is_new_high = not self.high_scores or score > max(s['score'] for s in self.high_scores)
            
            self.high_scores.append(score_data)
            self.save_high_scores_to_file()
            
            return is_new_high
        return False

# Global game instance
game = NumberGuessingGame()

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game"""
    player_name = request.form.get('player_name', 'Anonymous')
    difficulty = request.form.get('difficulty', 'medium')
    
    session['player_name'] = player_name
    session['difficulty'] = difficulty
    session['score'] = 0
    session['games_played'] = 0
    session['total_score'] = 0
    session['game_state'] = 'playing'
    
    # Initialize game session
    config = game.difficulty_levels[difficulty]
    session['secret_number'] = random.randint(config['range'][0], config['range'][1])
    session['attempts_used'] = 0
    session['max_attempts'] = config['attempts']
    session['range_min'] = config['range'][0]
    session['range_max'] = config['range'][1]
    session['base_points'] = config['points']
    session['guesses'] = []
    
    return redirect(url_for('play'))

@app.route('/play')
def play():
    """Game play page"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    if session['game_state'] == 'completed':
        return redirect(url_for('results'))
    
    return render_template('play.html',
                         difficulty=session['difficulty'],
                         attempts_used=session['attempts_used'],
                         max_attempts=session['max_attempts'],
                         range_min=session['range_min'],
                         range_max=session['range_max'],
                         guesses=session['guesses'])

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    """Submit a guess"""
    try:
        guess = int(request.form.get('guess'))
        secret_number = session['secret_number']
        range_min = session['range_min']
        range_max = session['range_max']
        attempts_used = session['attempts_used']
        max_attempts = session['max_attempts']
        
        if guess < range_min or guess > range_max:
            return jsonify({'error': f'Please enter a number between {range_min} and {range_max}!'})
        
        # Update attempts
        session['attempts_used'] += 1
        attempts_used = session['attempts_used']
        
        # Add to guesses list
        if 'guesses' not in session:
            session['guesses'] = []
        session['guesses'].append(guess)
        
        if guess == secret_number:
            # Player won!
            score = game.calculate_score(attempts_used, max_attempts, session['base_points'])
            session['score'] = score
            session['total_score'] += score
            session['games_played'] += 1
            session['game_state'] = 'completed'
            
            # Save high score
            is_new_high = game.save_high_score(
                session['player_name'], 
                session['total_score'], 
                session['difficulty']
            )
            
            return jsonify({
                'correct': True,
                'message': f'🎉 CONGRATULATIONS! You guessed it in {attempts_used} attempts!',
                'score': score,
                'total_score': session['total_score'],
                'is_new_high': is_new_high,
                'next_url': url_for('results')
            })
        else:
            # Wrong guess
            if guess < secret_number:
                message = "📈 Too low! Try a higher number."
            else:
                message = "📉 Too high! Try a lower number."
            
            # Check if game over
            if attempts_used >= max_attempts:
                session['games_played'] += 1
                session['game_state'] = 'completed'
                return jsonify({
                    'correct': False,
                    'message': f"😔 Game Over! The number was {secret_number}.",
                    'game_over': True,
                    'next_url': url_for('results')
                })
            
            # Provide hint
            hint = game.get_hint(secret_number, attempts_used, max_attempts)
            
            return jsonify({
                'correct': False,
                'message': message,
                'hint': hint,
                'attempts_used': attempts_used,
                'attempts_left': max_attempts - attempts_used
            })
            
    except ValueError:
        return jsonify({'error': 'Please enter a valid number!'})

@app.route('/results')
def results():
    """Results page"""
    if 'game_state' not in session or session['game_state'] != 'completed':
        return redirect(url_for('index'))
    
    return render_template('results.html',
                         player_name=session['player_name'],
                         score=session['score'],
                         total_score=session['total_score'],
                         games_played=session['games_played'],
                         difficulty=session['difficulty'])

@app.route('/statistics')
def statistics():
    """Statistics page"""
    if 'player_name' not in session:
        return redirect(url_for('index'))
    
    avg_score = session['total_score'] / session['games_played'] if session['games_played'] > 0 else 0
    
    return render_template('statistics.html',
                         player_name=session['player_name'],
                         games_played=session['games_played'],
                         total_score=session['total_score'],
                         avg_score=avg_score)

@app.route('/high_scores')
def high_scores():
    """High scores page"""
    sorted_scores = sorted(game.high_scores, key=lambda x: x['score'], reverse=True)
    return render_template('high_scores.html', high_scores=sorted_scores[:10])

@app.route('/difficulty')
def difficulty():
    """Difficulty selection page"""
    if 'player_name' not in session:
        return redirect(url_for('index'))
    
    return render_template('difficulty.html', 
                         difficulty_levels=game.difficulty_levels,
                         current_difficulty=session.get('difficulty', 'medium'))

@app.route('/change_difficulty', methods=['POST'])
def change_difficulty():
    """Change difficulty level"""
    difficulty = request.form.get('difficulty', 'medium')
    session['difficulty'] = difficulty
    return redirect(url_for('index'))

@app.route('/new_game')
def new_game():
    """Start a new game with current settings"""
    if 'player_name' not in session:
        return redirect(url_for('index'))
    
    difficulty = session.get('difficulty', 'medium')
    config = game.difficulty_levels[difficulty]
    
    session['game_state'] = 'playing'
    session['secret_number'] = random.randint(config['range'][0], config['range'][1])
    session['attempts_used'] = 0
    session['max_attempts'] = config['attempts']
    session['range_min'] = config['range'][0]
    session['range_max'] = config['range'][1]
    session['base_points'] = config['points']
    session['guesses'] = []
    
    return redirect(url_for('play'))

@app.route('/reset_session')
def reset_session():
    """Reset session and go to home"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 