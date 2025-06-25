# 🪨📄✂️ Rock, Paper, Scissors Game

A Python-based interactive Rock, Paper, Scissors game where players compete against the computer with comprehensive score tracking, statistics, and game history analysis.

## 🚀 Features

### 🎮 Core Gameplay
- **Classic Rules**: Rock crushes Scissors, Paper covers Rock, Scissors cut Paper
- **Computer Opponent**: Play against an AI that makes random choices
- **Real-time Scoring**: Track wins, losses, and ties throughout the session
- **Beautiful Interface**: Clean console interface with emojis and clear formatting

### 📊 Advanced Statistics
- **Win Rate Tracking**: Calculate and display your win percentage
- **Choice Analysis**: See which weapons you use most frequently
- **Session Statistics**: Track performance across multiple games
- **Historical Data**: View your gaming patterns and preferences

### 📜 Game History
- **Round-by-Round Tracking**: See every move and result
- **Recent Games Display**: View your last 10 games
- **Score Progression**: Track how scores change throughout the session
- **Timestamp Recording**: Know when each game was played

### 💾 Data Persistence
- **Statistics Saving**: Your progress is automatically saved
- **Session Continuity**: Resume games with your previous statistics
- **JSON Storage**: Clean, readable data format
- **Cross-session Tracking**: Maintain statistics across multiple game sessions

### 🎨 User Experience
- **Intuitive Menu**: Easy navigation through game options
- **Input Validation**: Robust error handling for invalid inputs
- **Screen Clearing**: Clean console experience
- **Cross-platform**: Works on Windows, macOS, and Linux

## 🛠️ Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

## 🏃‍♂️ How to Run

1. **Navigate to the task 3 folder**:
   ```bash
   cd "task 3"
   ```

2. **Run the game**:
   ```bash
   python rock_paper_scissors.py
   ```

## 🎮 How to Play

### Getting Started
1. **Enter Your Name**: Start by entering your name for personalization
2. **Read Rules**: Review the classic Rock, Paper, Scissors rules
3. **Choose Your Weapon**: Select Rock, Paper, or Scissors
4. **See Results**: View the round outcome and updated scores
5. **Continue Playing**: Play multiple rounds to build your statistics

### Game Options
- **1-3**: Choose Rock, Paper, or Scissors
- **4**: View detailed statistics and choice analysis
- **5**: View recent game history
- **6**: Exit the game and see final results

### Understanding Results
- **👤 Win**: Your weapon beats the computer's choice
- **🤖 Win**: Computer's weapon beats your choice
- **🤝 Tie**: Both players chose the same weapon

## 📊 Statistics Explained

### Basic Statistics
- **Total Games**: Number of rounds played
- **Wins**: Times you beat the computer
- **Losses**: Times the computer beat you
- **Ties**: Times both players chose the same weapon
- **Win Rate**: Percentage of games you won

### Choice Analysis
- **Weapon Usage**: How often you choose each weapon
- **Percentage Breakdown**: Distribution of your choices
- **Pattern Recognition**: Identify your playing style

### Game History
- **Round Details**: Each round's choices and results
- **Score Progression**: How scores changed over time
- **Recent Performance**: Your last 10 games for quick review

## 🎯 Strategy Tips

### For Beginners
1. **Random is Fair**: The computer makes random choices, so no strategy is inherently better
2. **Track Patterns**: Use the statistics to see if you have unconscious biases
3. **Mix It Up**: Try to use all three weapons equally to avoid predictability
4. **Learn from History**: Review your game history to understand your patterns

### For Advanced Players
1. **Analyze Statistics**: Use choice analysis to identify your tendencies
2. **Balance Your Choices**: Aim for equal distribution across all weapons
3. **Study Patterns**: Look for any unconscious patterns in your choices
4. **Set Goals**: Try to achieve specific win rates or choice distributions

## 🔧 Game Mechanics

### Win Conditions
```python
# Rock beats Scissors
# Paper beats Rock  
# Scissors beat Paper
# Same choice = Tie
```

### Score Calculation
- **Win**: +1 to player score
- **Loss**: +1 to computer score
- **Tie**: +1 to tie count
- **Win Rate**: (Player Wins / Total Games) × 100

### Data Storage
```json
{
  "player_name": "Player Name",
  "total_games": 25,
  "player_wins": 12,
  "computer_wins": 10,
  "ties": 3,
  "last_updated": "2024-01-15 14:30:00",
  "game_history": [...]
}
```

## 📝 File Structure

```
task 3/
├── rock_paper_scissors.py    # Main game file
├── README.md                 # This documentation
├── test_game.py              # Test file (optional)
├── requirements.txt          # Dependencies (none required)
├── run_game.bat              # Windows launcher script
└── statistics.json           # Game statistics (created automatically)
```

## 🎉 Sample Game Session

```
🪨📄✂️ WELCOME TO ROCK, PAPER, SCISSORS! 🪨📄✂️
============================================================
🎮 Features:
   • Play against the computer
   • Score tracking and statistics
   • Game history and analysis
   • Beautiful interface with emojis
   • Multiple game modes
============================================================

Enter your name: Alice

📋 GAME RULES:
----------------------------------------
🪨 Rock crushes ✂️ Scissors
📄 Paper covers 🪨 Rock
✂️ Scissors cut 📄 Paper
----------------------------------------
🎯 Choose your weapon and try to beat the computer!
📊 Your score will be tracked throughout the session.
----------------------------------------

🎯 CHOOSE YOUR WEAPON:
------------------------------
1. 🪨 Rock
2. 📄 Paper
3. ✂️ Scissors
4. 📊 View Statistics
5. 📜 View Game History
6. 🚪 Exit Game
------------------------------

🎮 ROUND RESULT:
----------------------------------------
👤 Alice: 🪨 Rock
🤖 Computer: ✂️ Scissors
----------------------------------------
🎉 Alice wins!
💪 Rock crushes scissors
----------------------------------------

📊 CURRENT SCORE:
------------------------------
👤 Alice: 1
🤖 Computer: 0
🤝 Ties: 0
🎮 Total Games: 1
------------------------------
📈 Win Rate: 100.0%
------------------------------
```

## 🏆 Advanced Features

### Statistics Analysis
- **Win Rate Trends**: Track how your performance changes over time
- **Choice Distribution**: See if you favor certain weapons
- **Session Comparison**: Compare performance across different gaming sessions
- **Pattern Recognition**: Identify unconscious playing patterns

### Game History Features
- **Detailed Records**: Every round is recorded with timestamps
- **Score Progression**: See how scores evolved throughout the session
- **Recent Performance**: Quick access to your last 10 games
- **Historical Analysis**: Review past sessions and performance

### Data Management
- **Automatic Saving**: Statistics are saved after each game
- **Session Continuity**: Resume with your previous statistics
- **Clean Data Format**: JSON storage for easy reading and modification
- **Memory Management**: Automatic cleanup of old game history

## 🐛 Troubleshooting

### Common Issues
- **Input Errors**: The game handles invalid inputs gracefully
- **File Permissions**: Ensure write access for statistics saving
- **Screen Issues**: Uses cross-platform screen clearing
- **Interruption**: Press Ctrl+C to exit safely

### Error Handling
- **Invalid Choices**: Re-enter valid numbers (1-6)
- **File Errors**: Statistics will be reset if file is corrupted
- **Memory Issues**: Game uses minimal memory resources

## 🔧 Customization

You can easily customize the game by modifying:

### Game Rules
```python
self.choices = {
    "rock": {"emoji": "🪨", "beats": "scissors", "loses_to": "paper"},
    "paper": {"emoji": "📄", "beats": "rock", "loses_to": "scissors"},
    "scissors": {"emoji": "✂️", "beats": "paper", "loses_to": "rock"}
}
```

### Statistics Tracking
- Modify the `save_statistics()` method to track additional data
- Add new analysis features to `display_statistics()`
- Customize the game history format

### User Interface
- Change emojis and formatting in display methods
- Modify menu options and navigation
- Add new game modes or features

## 🤝 Contributing

Feel free to:
- Add new game modes (best of 3, tournament style)
- Improve the statistics analysis
- Add sound effects or animations
- Create additional weapon options
- Report bugs or suggest features

## 📄 License

This project is open source and available for educational purposes.

---

**Enjoy playing Rock, Paper, Scissors! 🪨📄✂️🎉** 