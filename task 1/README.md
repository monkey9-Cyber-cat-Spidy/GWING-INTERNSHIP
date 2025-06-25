# 🎮 Interactive Quiz Game

A Python-based interactive quiz game with both console and web interfaces. Test your knowledge with multiple-choice questions and challenge yourself with a number guessing game!

## 🚀 Features

### 📝 **Quiz Section**
- **Multiple Choice Questions**: Test your knowledge across various topics
- **Random Question Selection**: Questions are shuffled for variety
- **Real-time Feedback**: Get immediate feedback on your answers
- **Detailed Explanations**: Learn from explanations for each question
- **Progress Tracking**: See your progress through the quiz

### 🎯 **Number Guessing Challenge**
- **Smart Hints**: Get helpful hints after 5 attempts
- **Bonus Points**: Earn extra points for quick guesses
- **Attempt Tracking**: Monitor your remaining attempts
- **Progressive Difficulty**: Hints become more specific over time

### 📊 **Scoring System**
- **Quiz Points**: Earn points for correct answers
- **Bonus Points**: Extra points for quick number guessing
- **Performance Grading**: Get graded from A+ to D based on performance
- **Detailed Results**: Comprehensive performance summary

### 🌐 **Web Interface**
- **Modern UI**: Beautiful, responsive web design
- **Real-time Updates**: AJAX-powered interactions
- **Mobile Friendly**: Works on all devices
- **Session Management**: Secure game state tracking
- **Visual Feedback**: Animated progress bars and effects

## 🛠️ Requirements

- Python 3.6 or higher
- Flask (for web interface)
- No additional dependencies for console version

## 🏃‍♂️ How to Run

### Console Version
1. **Navigate to the task 1 folder**:
   ```bash
   cd "task 1"
   ```

2. **Run the console game**:
   ```bash
   python quiz_game.py
   ```
   
   Or use the batch file on Windows:
   ```bash
   run_game.bat
   ```

### Web Version
1. **Navigate to the task 1 folder**:
   ```bash
   cd "task 1"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web application**:
   ```bash
   python app.py
   ```
   
   Or use the batch file on Windows:
   ```bash
   run_web.bat
   ```

4. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## 🎮 How to Play

### Getting Started
1. **Enter Your Name**: Provide your name to personalize the experience
2. **Quiz Section**: Answer 5 multiple-choice questions
3. **Number Guessing**: Guess a number between 1 and 100
4. **View Results**: See your final score and grade
5. **Play Again**: Start a new game anytime

### Game Mechanics
- **Quiz Questions**: 5 random questions from a pool of 8
- **Answer Options**: Choose from A, B, C, or D
- **Number Guessing**: 10 attempts to guess the secret number
- **Bonus Points**: Earn 1-10 bonus points based on guessing speed
- **Final Grade**: A+ (90%+), A (80%+), B (70%+), C (60%+), D (<60%)

### Web Interface Features
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Real-time Feedback**: Instant feedback on answers and guesses
- **Progress Indicators**: Visual progress bars and counters
- **Animations**: Smooth transitions and visual effects
- **Session Persistence**: Your game state is saved during the session

## 📝 File Structure

```
task 1/
├── quiz_game.py             # Console version of the game
├── app.py                   # Flask web application
├── templates/               # HTML templates for web interface
│   ├── base.html           # Base template with styling
│   ├── index.html          # Home page
│   ├── quiz.html           # Quiz questions page
│   ├── number_guessing.html # Number guessing game page
│   └── results.html        # Results page
├── README.md               # This documentation
├── requirements.txt        # Python dependencies
├── run_game.bat           # Console game launcher (Windows)
├── run_web.bat            # Web app launcher (Windows)
└── test_game.py           # Test file (optional)
```

## 🎯 Sample Questions

The game includes questions on various topics:
- **Geography**: Capitals, oceans, landmarks
- **Science**: Planets, elements, mathematics
- **Literature**: Authors, famous works
- **History**: Important events and dates

## 🌟 Web Interface Features

### Home Page
- Welcome screen with game features
- Player name input form
- Modern gradient design

### Quiz Interface
- Clean question display
- Interactive answer buttons
- Real-time feedback
- Progress tracking

### Number Guessing
- Input validation
- Attempt counter
- Smart hints system
- Visual feedback

### Results Page
- Comprehensive score display
- Performance grading
- Animated progress bars
- Play again option

## 🎉 Sample Game Session

### Console Version
```
🎮 WELCOME TO THE INTERACTIVE QUIZ GAME! 🎮
================================================================================
This game includes:
📝 Multiple choice questions
🎯 Number guessing challenges
📊 Score tracking
🏆 Final results
================================================================================

Enter your name: John

📝 QUIZ SECTION
==================================================

Question 1 of 5

❓ What is the capital of France?
   A) London
   B) Berlin
   C) Paris
   D) Madrid

Enter your answer (A/B/C/D): C
✅ Correct! Well done!
💡 Paris is the capital and largest city of France.

🎯 NUMBER GUESSING CHALLENGE! 🎯
==================================================
I'm thinking of a number between 1 and 100.
You have 10 attempts to guess it!
==================================================

Attempt 1/10
Enter your guess (1-100): 50
📉 Too high! Try a lower number.

🏁 FINAL RESULTS 🏁
================================================================================
Player: John
Total Questions: 5
Correct Answers: 4
Score: 4/5
Percentage: 80.0%
Grade: A 🥇
Message: Great job! You know your stuff!
================================================================================
```

### Web Version
- Beautiful web interface with modern design
- Interactive buttons and real-time feedback
- Responsive layout for all devices
- Session management and state tracking

## 🔧 Technical Details

### Console Version
- **Language**: Python 3.6+
- **Dependencies**: None (uses only built-in modules)
- **Features**: Full game functionality with console UI

### Web Version
- **Framework**: Flask 2.3.3
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Features**: AJAX interactions, session management, responsive design
- **Port**: 5000 (configurable in app.py)

## 🎨 Customization

### Adding Questions
Edit the `questions` list in both `quiz_game.py` and `app.py`:
```python
{
    "question": "Your question here?",
    "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
    "correct": "A",
    "explanation": "Explanation of the correct answer."
}
```

### Styling
- **Console**: Modify the print statements and formatting
- **Web**: Edit the CSS in `templates/base.html`

### Game Settings
- **Quiz Questions**: Change `num_questions` parameter
- **Number Range**: Modify the range in `number_guessing_game()`
- **Attempts**: Adjust `max_attempts` variable

## 🐛 Troubleshooting

### Common Issues
1. **Port already in use**: Change the port in `app.py`
2. **Dependencies not found**: Run `pip install -r requirements.txt`
3. **Template errors**: Ensure all template files are in the `templates/` folder

### Browser Compatibility
- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Full support
- **Edge**: Full support
- **Mobile browsers**: Responsive design supported

## 📄 License

This project is part of the Gwing Internship tasks and is provided as-is for educational purposes.

## 🤝 Contributing

Feel free to enhance the game by:
- Adding more questions
- Improving the UI/UX
- Adding new game modes
- Implementing user accounts
- Adding leaderboards

---

**Enjoy the game! 🎮✨** 