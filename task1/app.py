from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'quiz_game_secret_key_2024'

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
                "correct": "C",
                "explanation": "Paris is the capital and largest city of France."
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
                "correct": "B",
                "explanation": "Mars is called the Red Planet due to its reddish appearance."
            },
            {
                "question": "What is 2 + 2?",
                "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
                "correct": "B",
                "explanation": "2 + 2 = 4"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
                "correct": "B",
                "explanation": "William Shakespeare wrote the famous tragedy 'Romeo and Juliet'."
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Pacific Ocean", "D) Arctic Ocean"],
                "correct": "C",
                "explanation": "The Pacific Ocean is the largest and deepest ocean on Earth."
            },
            {
                "question": "Which element has the chemical symbol 'O'?",
                "options": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Oganesson"],
                "correct": "B",
                "explanation": "Oxygen has the chemical symbol 'O' and atomic number 8."
            },
            {
                "question": "What year did World War II end?",
                "options": ["A) 1943", "B) 1944", "C) 1945", "D) 1946"],
                "correct": "C",
                "explanation": "World War II ended in 1945 with the surrender of Germany and Japan."
            },
            {
                "question": "What is the square root of 16?",
                "options": ["A) 2", "B) 4", "C) 8", "D) 16"],
                "correct": "B",
                "explanation": "The square root of 16 is 4, because 4 × 4 = 16."
            }
        ]

    def get_quiz_questions(self, num_questions=5):
        """Get random quiz questions"""
        return random.sample(self.questions, min(num_questions, len(self.questions)))

    def check_answer(self, question_index, player_answer):
        """Check if answer is correct"""
        if question_index < len(self.questions):
            return player_answer == self.questions[question_index]['correct']
        return False

# Global game instance
game = QuizGame()

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    """Start a new game"""
    player_name = request.form.get('player_name', 'Anonymous')
    session['player_name'] = player_name
    session['score'] = 0
    session['total_questions'] = 0
    session['current_question'] = 0
    session['quiz_questions'] = game.get_quiz_questions(5)
    session['game_state'] = 'quiz'
    return redirect(url_for('quiz'))

@app.route('/quiz')
def quiz():
    """Quiz page"""
    if 'game_state' not in session:
        return redirect(url_for('index'))
    
    if session['game_state'] == 'quiz':
        current_q = session['current_question']
        quiz_questions = session['quiz_questions']
        
        if current_q >= len(quiz_questions):
            # Quiz completed, move to number guessing
            session['game_state'] = 'number_guessing'
            session['secret_number'] = random.randint(1, 100)
            session['guessing_attempts'] = 0
            return redirect(url_for('number_guessing'))
        
        question_data = quiz_questions[current_q]
        return render_template('quiz.html', 
                             question=question_data, 
                             question_num=current_q + 1, 
                             total_questions=len(quiz_questions))
    
    return redirect(url_for('index'))

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    """Submit quiz answer"""
    answer = request.form.get('answer')
    current_q = session['current_question']
    quiz_questions = session['quiz_questions']
    
    if current_q < len(quiz_questions):
        question_data = quiz_questions[current_q]
        is_correct = answer == question_data['correct']
        
        if is_correct:
            session['score'] += 1
        
        session['total_questions'] += 1
        session['current_question'] += 1
        
        return jsonify({
            'correct': is_correct,
            'correct_answer': question_data['correct'],
            'explanation': question_data['explanation'],
            'next_url': url_for('quiz')
        })
    
    return jsonify({'error': 'Invalid question'})

@app.route('/number_guessing')
def number_guessing():
    """Number guessing game page"""
    if 'game_state' not in session or session['game_state'] != 'number_guessing':
        return redirect(url_for('index'))
    
    return render_template('number_guessing.html', 
                         attempts=session['guessing_attempts'],
                         max_attempts=10)

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    """Submit number guess"""
    try:
        guess = int(request.form.get('guess'))
        secret_number = session['secret_number']
        attempts = session['guessing_attempts']
        
        if guess < 1 or guess > 100:
            return jsonify({'error': 'Please enter a number between 1 and 100'})
        
        session['guessing_attempts'] += 1
        
        if guess == secret_number:
            bonus_points = max(1, 11 - session['guessing_attempts'])
            session['score'] += bonus_points
            session['game_state'] = 'completed'
            return jsonify({
                'correct': True,
                'message': f'Congratulations! You guessed it in {session["guessing_attempts"]} attempts!',
                'bonus_points': bonus_points,
                'next_url': url_for('results')
            })
        elif guess < secret_number:
            message = 'Too low! Try a higher number.'
        else:
            message = 'Too high! Try a lower number.'
        
        # Give hint after 5 attempts
        hint = ""
        if session['guessing_attempts'] == 5:
            if secret_number % 2 == 0:
                hint = "Hint: The number is even!"
            else:
                hint = "Hint: The number is odd!"
        
        # Check if game over
        if session['guessing_attempts'] >= 10:
            session['game_state'] = 'completed'
            return jsonify({
                'correct': False,
                'message': f'Game Over! The number was {secret_number}.',
                'next_url': url_for('results')
            })
        
        return jsonify({
            'correct': False,
            'message': message,
            'hint': hint,
            'attempts': session['guessing_attempts']
        })
        
    except ValueError:
        return jsonify({'error': 'Please enter a valid number'})

@app.route('/results')
def results():
    """Results page"""
    if 'game_state' not in session or session['game_state'] != 'completed':
        return redirect(url_for('index'))
    
    player_name = session.get('player_name', 'Anonymous')
    score = session.get('score', 0)
    total_questions = session.get('total_questions', 0)
    
    percentage = (score / total_questions * 100) if total_questions > 0 else 0
    
    # Grade the performance
    if percentage >= 90:
        grade = "A+ 🏆"
        message = "Excellent! You're a quiz master!"
    elif percentage >= 80:
        grade = "A 🥇"
        message = "Great job! You know your stuff!"
    elif percentage >= 70:
        grade = "B 🥈"
        message = "Good work! Keep learning!"
    elif percentage >= 60:
        grade = "C 🥉"
        message = "Not bad! Room for improvement."
    else:
        grade = "D 📚"
        message = "Keep studying! You'll get better!"
    
    return render_template('results.html',
                         player_name=player_name,
                         score=score,
                         total_questions=total_questions,
                         percentage=percentage,
                         grade=grade,
                         message=message)

@app.route('/play_again')
def play_again():
    """Reset game and start over"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 