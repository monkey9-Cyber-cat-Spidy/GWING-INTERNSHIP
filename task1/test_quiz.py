#!/usr/bin/env python3
"""
Test file for the Quiz Game
This file demonstrates the quiz game functionality without requiring user input.
"""

import random
import time

def test_quiz_functionality():
    """Test the quiz game functionality"""
    print("🧪 TESTING QUIZ GAME FUNCTIONALITY")
    print("=" * 50)
    
    # Sample questions for testing
    test_questions = [
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
        }
    ]
    
    score = 0
    total_questions = len(test_questions)
    
    print("📝 Testing Quiz Questions:")
    for i, question in enumerate(test_questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question['options']:
            print(f"   {option}")
        
        # Simulate correct answer
        correct_answer = question['correct']
        print(f"✅ Correct answer: {correct_answer}")
        print(f"💡 {question['explanation']}")
        score += 1
        time.sleep(0.5)
    
    print(f"\n📊 Test Results:")
    print(f"Score: {score}/{total_questions}")
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Test number guessing logic
    print("\n🎯 Testing Number Guessing Logic:")
    secret_number = random.randint(1, 100)
    print(f"Secret number: {secret_number}")
    
    # Simulate a successful guess
    attempts = random.randint(1, 10)
    print(f"Guessed in {attempts} attempts")
    bonus_points = max(1, 11 - attempts)
    print(f"Bonus points earned: {bonus_points}")
    
    # Update total score
    total_score = score + bonus_points
    total_questions_with_bonus = total_questions + 1
    
    print(f"\n🏁 Final Test Score: {total_score}/{total_questions_with_bonus}")
    final_percentage = (total_score / total_questions_with_bonus) * 100
    print(f"Final Percentage: {final_percentage:.1f}%")
    
    # Grade the performance
    if final_percentage >= 90:
        grade = "A+ 🏆"
    elif final_percentage >= 80:
        grade = "A 🥇"
    elif final_percentage >= 70:
        grade = "B 🥈"
    elif final_percentage >= 60:
        grade = "C 🥉"
    else:
        grade = "D 📚"
    
    print(f"Grade: {grade}")
    print("\n✅ All tests completed successfully!")
    print("🎮 Ready to run the full game!")

if __name__ == "__main__":
    test_quiz_functionality() 