# 🎯 Number Guessing Game

A Python-based interactive number guessing game with multiple difficulty levels, scoring system, and enhanced features. Players try to guess a randomly generated number within a specified range with helpful feedback and hints.

## 🚀 Features

### 🎮 Game Modes
- **Easy Mode**: Numbers 1-50, 10 attempts, 100 points max
- **Medium Mode**: Numbers 1-100, 8 attempts, 200 points max
- **Hard Mode**: Numbers 1-200, 6 attempts, 300 points max
- **Expert Mode**: Numbers 1-500, 5 attempts, 500 points max

### 🎯 Core Gameplay
- **Random Number Generation**: Each game generates a new random number
- **Attempt Tracking**: Monitor your attempts and remaining guesses
- **Smart Feedback**: Get "too high" or "too low" guidance
- **Previous Guesses**: See your previous guesses to avoid repetition
- **Input Validation**: Robust error handling for invalid inputs

### 💡 Intelligent Hints System
- **Even/Odd Hint**: After half the attempts, learn if the number is even or odd
- **Range Hints**: Get helpful range hints as attempts decrease
- **Strategic Guidance**: Hints become more specific as you run out of attempts

### 📊 Scoring & Statistics
- **Dynamic Scoring**: More points for fewer attempts
- **Efficiency Bonus**: Score calculation based on attempt efficiency
- **Statistics Tracking**: Track games played, total score, and average score
- **High Score System**: Persistent high scores saved to file
- **Performance History**: View your gaming history and achievements

### 🎨 User Experience
- **Clean Interface**: Beautiful console interface with emojis
- **Menu System**: Easy navigation through game options
- **Screen Clearing**: Clean console experience
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

## 🏃‍♂️ How to Run

1. **Navigate to the task 2 folder**:
   ```bash
   cd "task 2"
   ```

2. **Run the game**:
   ```bash
   python number_guessing_game.py
   ```

## 🎮 How to Play

### Getting Started
1. **Enter Your Name**: Start by entering your name for personalization
2. **Choose Difficulty**: Select from 4 difficulty levels
3. **Read Rules**: Review the specific rules for your chosen difficulty
4. **Start Playing**: Begin guessing numbers!

### Gameplay
1. **Make a Guess**: Enter a number within the specified range
2. **Get Feedback**: Receive "too high" or "too low" guidance
3. **Use Hints**: Pay attention to helpful hints that appear
4. **Track Progress**: Monitor your attempts and previous guesses
5. **Win or Try Again**: Guess correctly or run out of attempts

### Menu Options
- **Play Game**: Start a new game with current difficulty
- **View Statistics**: See your personal gaming statistics
- **View High Scores**: Check the leaderboard
- **Change Difficulty**: Switch to a different difficulty level
- **Exit**: Save your progress and exit the game

## 📊 Scoring System

### Point Calculation
- **Base Points**: Each difficulty has a maximum point value
- **Efficiency Multiplier**: Points are multiplied by attempt efficiency
- **Formula**: `Score = Base_Points × (Max_Attempts - Attempts_Used + 1) / Max_Attempts`

### Example Scoring
- **Easy Mode**: 100 points max
  - Perfect game (1 attempt): 100 points
  - Half efficiency (5 attempts): 60 points
  - Last attempt: 10 points

## 🏆 High Score System

### Features
- **Persistent Storage**: High scores saved to `high_scores.json`
- **Multiple Players**: Track scores from different players
- **Difficulty Tracking**: Separate scores for each difficulty level
- **Date Stamping**: Record when each score was achieved
- **Top 5 Display**: Show the best 5 scores

### High Score Format
```json
{
  "name": "Player Name",
  "score": 150,
  "difficulty": "medium",
  "date": "2024-01-15 14:30"
}
```

## 🎯 Strategy Tips

### For Beginners
1. **Start with Easy Mode**: Get familiar with the game mechanics
2. **Use Binary Search**: Start with the middle number and adjust
3. **Pay Attention to Hints**: They become more valuable as attempts decrease
4. **Track Previous Guesses**: Avoid repeating the same numbers

### For Advanced Players
1. **Optimize for Speed**: Fewer attempts = higher scores
2. **Use Range Hints**: Plan your guesses based on revealed ranges
3. **Challenge Yourself**: Try higher difficulties for better scores
4. **Study Patterns**: Learn from your previous games

## 🔧 Customization

You can easily customize the game by modifying:

### Difficulty Levels
```python
self.difficulty_levels = {
    "custom": {"range": (1, 1000), "attempts": 15, "points": 1000}
}
```

### Hint System
- Modify the `get_hint()` method to add custom hints
- Adjust hint timing and content
- Add difficulty-specific hints

### Scoring System
- Change the scoring formula in `calculate_score()`
- Add bonus points for special achievements
- Implement streak bonuses

## 🐛 Troubleshooting

### Common Issues
- **Input Errors**: The game handles invalid inputs gracefully
- **File Permissions**: Ensure write access for high score saving
- **Screen Issues**: Uses cross-platform screen clearing
- **Interruption**: Press Ctrl+C to exit safely

### Error Handling
- **Invalid Numbers**: Re-enter valid numbers within range
- **File Errors**: High scores will be reset if file is corrupted
- **Memory Issues**: Game uses minimal memory resources

## 📝 File Structure

```
task 2/
├── number_guessing_game.py    # Main game file
├── README.md                  # This documentation
├── high_scores.json          # High scores data (created automatically)
└── test_game.py              # Test file (optional)
```

## 🎉 Sample Game Session

```
🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯
============================================================
🎮 Features:
   • Multiple difficulty levels
   • Score tracking and high scores
   • Hints and feedback
   • Statistics tracking
   • Beautiful interface
============================================================

Enter your name: John

📋 MAIN MENU:
------------------------------
1. 🎮 Play Game
2. 📊 View Statistics
3. 🏆 View High Scores
4. ⚙️  Change Difficulty
5. 🚪 Exit
------------------------------

📊 SELECT DIFFICULTY LEVEL:
----------------------------------------
1. EASY: Range 1-50, 10 attempts, 100 points
2. MEDIUM: Range 1-100, 8 attempts, 200 points
3. HARD: Range 1-200, 6 attempts, 300 points
4. EXPERT: Range 1-500, 5 attempts, 500 points
----------------------------------------

🎮 Starting MEDIUM mode...
🎯 I'm thinking of a number between 1 and 100
🎲 You have 8 attempts
--------------------------------------------------

📊 Attempt 1/8 (Attempts left: 8)
🎯 Enter your guess (1-100): 50
📉 Too high! Try a lower number.
🎲 7 attempts remaining...

📊 Attempt 2/8 (Attempts left: 7)
📝 Previous guesses: 50
🎯 Enter your guess (1-100): 25
📈 Too low! Try a higher number.
💡 Hint: The number is even!
🎲 6 attempts remaining...

🎉 CONGRATULATIONS! You guessed it in 3 attempts!
🏆 Score earned: 150 points!
```

## 🤝 Contributing

Feel free to:
- Add new difficulty levels
- Improve the hint system
- Add sound effects or animations
- Create additional game modes
- Report bugs or suggest features

## 📄 License

This project is open source and available for educational purposes.

---

**Enjoy playing the Number Guessing Game! 🎯🎉** 