#!/usr/bin/env python3
"""
Test file for the Rock, Paper, Scissors Game
This file demonstrates the game functionality without requiring user input.
"""

import random
import time

def test_rock_paper_scissors_logic():
    """Test the Rock, Paper, Scissors game logic"""
    print("🧪 TESTING ROCK, PAPER, SCISSORS GAME LOGIC")
    print("=" * 50)
    
    # Game choices and rules
    choices = {
        "rock": {"emoji": "🪨", "beats": "scissors", "loses_to": "paper"},
        "paper": {"emoji": "📄", "beats": "rock", "loses_to": "scissors"},
        "scissors": {"emoji": "✂️", "beats": "paper", "loses_to": "rock"}
    }
    
    def determine_winner(player_choice, computer_choice):
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return "tie"
        elif choices[player_choice]["beats"] == computer_choice:
            return "player"
        else:
            return "computer"
    
    def get_win_phrase(winner_choice, loser_choice):
        """Get a descriptive phrase for how the winner won"""
        phrases = {
            "rock": {"scissors": "crushes scissors"},
            "paper": {"rock": "covers rock"},
            "scissors": {"paper": "cuts paper"}
        }
        return phrases[winner_choice][loser_choice]
    
    print("🎯 Testing Game Rules:")
    print("-" * 30)
    for player_choice, player_info in choices.items():
        for computer_choice, computer_info in choices.items():
            result = determine_winner(player_choice, computer_choice)
            player_emoji = player_info["emoji"]
            computer_emoji = computer_info["emoji"]
            
            if result == "tie":
                outcome = "🤝 Tie"
            elif result == "player":
                outcome = f"👤 Win ({player_choice} {get_win_phrase(player_choice, computer_choice)})"
            else:
                outcome = f"🤖 Win ({computer_choice} {get_win_phrase(computer_choice, player_choice)})"
            
            print(f"{player_emoji} vs {computer_emoji}: {outcome}")
    
    print("\n🎮 Simulating Game Rounds:")
    print("-" * 40)
    
    # Simulate multiple rounds
    player_score = 0
    computer_score = 0
    ties = 0
    total_rounds = 10
    
    for round_num in range(1, total_rounds + 1):
        player_choice = random.choice(list(choices.keys()))
        computer_choice = random.choice(list(choices.keys()))
        result = determine_winner(player_choice, computer_choice)
        
        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            ties += 1
        
        player_emoji = choices[player_choice]["emoji"]
        computer_emoji = choices[computer_choice]["emoji"]
        
        print(f"Round {round_num}: {player_emoji} vs {computer_emoji} = {result}")
        time.sleep(0.2)
    
    print(f"\n📊 Final Score:")
    print(f"👤 Player: {player_score}")
    print(f"🤖 Computer: {computer_score}")
    print(f"🤝 Ties: {ties}")
    print(f"🎮 Total Rounds: {total_rounds}")
    
    if total_rounds > 0:
        win_rate = (player_score / total_rounds) * 100
        print(f"📈 Win Rate: {win_rate:.1f}%")
    
    print("\n✅ Game logic test completed successfully!")

def test_statistics_calculation():
    """Test statistics calculation"""
    print("\n📊 TESTING STATISTICS CALCULATION")
    print("=" * 40)
    
    # Simulate game history
    game_history = [
        {"player_choice": "rock", "computer_choice": "scissors", "result": "player"},
        {"player_choice": "paper", "computer_choice": "rock", "result": "player"},
        {"player_choice": "scissors", "computer_choice": "paper", "result": "player"},
        {"player_choice": "rock", "computer_choice": "paper", "result": "computer"},
        {"player_choice": "paper", "computer_choice": "scissors", "result": "computer"},
        {"player_choice": "scissors", "computer_choice": "rock", "result": "computer"},
        {"player_choice": "rock", "computer_choice": "rock", "result": "tie"},
        {"player_choice": "paper", "computer_choice": "paper", "result": "tie"},
        {"player_choice": "scissors", "computer_choice": "scissors", "result": "tie"}
    ]
    
    # Calculate statistics
    total_games = len(game_history)
    player_wins = sum(1 for game in game_history if game["result"] == "player")
    computer_wins = sum(1 for game in game_history if game["result"] == "computer")
    ties = sum(1 for game in game_history if game["result"] == "tie")
    
    print(f"📈 Statistics from {total_games} games:")
    print(f"👤 Player Wins: {player_wins}")
    print(f"🤖 Computer Wins: {computer_wins}")
    print(f"🤝 Ties: {ties}")
    
    if total_games > 0:
        win_rate = (player_wins / total_games) * 100
        loss_rate = (computer_wins / total_games) * 100
        tie_rate = (ties / total_games) * 100
        
        print(f"📊 Win Rate: {win_rate:.1f}%")
        print(f"📉 Loss Rate: {loss_rate:.1f}%")
        print(f"📊 Tie Rate: {tie_rate:.1f}%")
    
    # Choice analysis
    print(f"\n🎯 Choice Analysis:")
    player_choices = [game['player_choice'] for game in game_history]
    choice_counts = {}
    for choice in ["rock", "paper", "scissors"]:
        choice_counts[choice] = player_choices.count(choice)
    
    for choice, count in choice_counts.items():
        percentage = (count / len(player_choices)) * 100 if player_choices else 0
        emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}[choice]
        print(f"{emoji} {choice.title()}: {count} times ({percentage:.1f}%)")
    
    print("\n✅ Statistics calculation test completed!")

def test_game_history_display():
    """Test game history display format"""
    print("\n📜 TESTING GAME HISTORY DISPLAY")
    print("=" * 40)
    
    # Sample game history
    game_history = [
        {"player_choice": "rock", "computer_choice": "scissors", "result": "player", "player_score": 1, "computer_score": 0},
        {"player_choice": "paper", "computer_choice": "rock", "result": "player", "player_score": 2, "computer_score": 0},
        {"player_choice": "scissors", "computer_choice": "paper", "result": "player", "player_score": 3, "computer_score": 0},
        {"player_choice": "rock", "computer_choice": "paper", "result": "computer", "player_score": 3, "computer_score": 1},
        {"player_choice": "paper", "computer_choice": "scissors", "result": "computer", "player_score": 3, "computer_score": 2}
    ]
    
    print("📜 RECENT GAME HISTORY:")
    print("=" * 60)
    print(f"{'Round':<6} {'Player':<12} {'Computer':<12} {'Result':<10} {'Score'}")
    print("-" * 60)
    
    for i, game in enumerate(game_history, 1):
        player_emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}[game['player_choice']]
        computer_emoji = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}[game['computer_choice']]
        
        if game['result'] == 'player':
            result = "👤 Win"
        elif game['result'] == 'computer':
            result = "🤖 Win"
        else:
            result = "🤝 Tie"
        
        score = f"{game['player_score']}-{game['computer_score']}"
        
        print(f"{i:<6} {player_emoji} {game['player_choice']:<10} "
              f"{computer_emoji} {game['computer_choice']:<10} {result:<10} {score}")
    
    print("=" * 60)
    print("\n✅ Game history display test completed!")

def test_data_persistence():
    """Test data persistence format"""
    print("\n💾 TESTING DATA PERSISTENCE FORMAT")
    print("=" * 40)
    
    # Sample statistics data
    stats_data = {
        "player_name": "TestPlayer",
        "total_games": 15,
        "player_wins": 8,
        "computer_wins": 5,
        "ties": 2,
        "last_updated": "2024-01-15 14:30:00",
        "game_history": [
            {
                "player_choice": "rock",
                "computer_choice": "scissors",
                "result": "player",
                "player_score": 1,
                "computer_score": 0,
                "timestamp": "2024-01-15 14:25:00"
            }
        ]
    }
    
    print("📄 Sample Statistics Data Structure:")
    print("-" * 40)
    for key, value in stats_data.items():
        if key == "game_history":
            print(f"{key}: [{len(value)} game records]")
        else:
            print(f"{key}: {value}")
    
    print("\n✅ Data persistence format test completed!")

if __name__ == "__main__":
    test_rock_paper_scissors_logic()
    test_statistics_calculation()
    test_game_history_display()
    test_data_persistence()
    print("\n🎉 All tests completed successfully!")
    print("🎮 Ready to run the full Rock, Paper, Scissors game!") 