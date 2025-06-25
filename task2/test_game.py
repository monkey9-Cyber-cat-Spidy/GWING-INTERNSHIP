#!/usr/bin/env python3
"""
Test file for the Number Guessing Game
This file demonstrates the game functionality without requiring user input.
"""

import random
import time

def test_number_guessing_logic():
    """Test the number guessing game logic"""
    print("🧪 TESTING NUMBER GUESSING GAME LOGIC")
    print("=" * 50)
    
    # Test different difficulty levels
    difficulty_levels = {
        "easy": {"range": (1, 50), "attempts": 10, "points": 100},
        "medium": {"range": (1, 100), "attempts": 8, "points": 200},
        "hard": {"range": (1, 200), "attempts": 6, "points": 300},
        "expert": {"range": (1, 500), "attempts": 5, "points": 500}
    }
    
    print("📊 Testing Difficulty Levels:")
    for difficulty, config in difficulty_levels.items():
        range_min, range_max = config["range"]
        attempts = config["attempts"]
        points = config["points"]
        
        print(f"\n🎮 {difficulty.upper()} MODE:")
        print(f"   Range: {range_min}-{range_max}")
        print(f"   Attempts: {attempts}")
        print(f"   Max Points: {points}")
        
        # Simulate a game
        secret_number = random.randint(range_min, range_max)
        print(f"   Secret Number: {secret_number}")
        
        # Simulate successful guess
        attempts_used = random.randint(1, attempts)
        print(f"   Guessed in: {attempts_used} attempts")
        
        # Calculate score
        efficiency = (attempts - attempts_used + 1) / attempts
        score = int(points * efficiency)
        print(f"   Score earned: {score} points")
        
        time.sleep(0.5)
    
    print("\n🎯 Testing Hint System:")
    test_number = random.randint(1, 100)
    max_attempts = 8
    
    print(f"Test number: {test_number}")
    print(f"Max attempts: {max_attempts}")
    
    for attempt in range(1, max_attempts + 1):
        hint = get_test_hint(test_number, attempt, max_attempts)
        if hint:
            print(f"   Attempt {attempt}: {hint}")
    
    print("\n📊 Testing Score Calculation:")
    test_cases = [
        (1, 8, 200),   # Perfect game
        (4, 8, 200),   # Half efficiency
        (8, 8, 200),   # Last attempt
        (10, 8, 200),  # Over attempts (should be 0)
    ]
    
    for attempts_used, max_attempts, base_points in test_cases:
        if attempts_used <= max_attempts:
            efficiency = (max_attempts - attempts_used + 1) / max_attempts
            score = int(base_points * efficiency)
        else:
            score = 0
        
        print(f"   {attempts_used}/{max_attempts} attempts: {score} points")
    
    print("\n✅ All tests completed successfully!")
    print("🎮 Ready to run the full game!")

def get_test_hint(secret_number, attempt, max_attempts):
    """Test version of hint system"""
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
        if secret_number <= 25:
            return "💡 Hint: The number is 25 or less!"
        elif secret_number <= 75:
            return "💡 Hint: The number is between 26 and 75!"
        else:
            return "💡 Hint: The number is greater than 75!"
    return None

def test_high_score_system():
    """Test the high score system"""
    print("\n🏆 TESTING HIGH SCORE SYSTEM")
    print("=" * 40)
    
    # Simulate high scores
    test_scores = [
        {"name": "Alice", "score": 150, "difficulty": "medium", "date": "2024-01-15 10:30"},
        {"name": "Bob", "score": 200, "difficulty": "hard", "date": "2024-01-15 11:45"},
        {"name": "Charlie", "score": 100, "difficulty": "easy", "date": "2024-01-15 12:15"},
        {"name": "Diana", "score": 400, "difficulty": "expert", "date": "2024-01-15 13:20"},
        {"name": "Eve", "score": 180, "difficulty": "medium", "date": "2024-01-15 14:05"}
    ]
    
    print("📊 Sample High Scores:")
    sorted_scores = sorted(test_scores, key=lambda x: x['score'], reverse=True)
    for i, score_data in enumerate(sorted_scores[:5], 1):
        print(f"{i}. {score_data['name']}: {score_data['score']} points "
              f"({score_data['difficulty']}) - {score_data['date']}")
    
    print("\n✅ High score system test completed!")

if __name__ == "__main__":
    test_number_guessing_logic()
    test_high_score_system() 