import random
import time
import os

class QuizGame:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
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
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_welcome(self):
        """Display welcome message"""
        self.clear_screen()
        print("=" * 60)
        print("🎮 WELCOME TO THE INTERACTIVE QUIZ GAME! 🎮")
        print("=" * 60)
        print("This game includes:")
        print("📝 Multiple choice questions")
        print("🎯 Number guessing challenges")
        print("📊 Score tracking")
        print("🏆 Final results")
        print("=" * 60)
        print()
    
    def get_player_name(self):
        """Get player's name"""
        while True:
            name = input("Enter your name: ").strip()
            if name:
                return name
            print("Please enter a valid name!")
    
    def display_question(self, question_data):
        """Display a single question with options"""
        print(f"\n❓ {question_data['question']}")
        print()
        for option in question_data['options']:
            print(f"   {option}")
        print()
    
    def get_answer(self):
        """Get player's answer"""
        while True:
            answer = input("Enter your answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                return answer
            print("Please enter A, B, C, or D!")
    
    def check_answer(self, player_answer, correct_answer, explanation):
        """Check if answer is correct and provide feedback"""
        if player_answer == correct_answer:
            print("✅ Correct! Well done!")
            self.score += 1
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}.")
        
        print(f"💡 {explanation}")
        self.total_questions += 1
    
    def number_guessing_game(self):
        """Number guessing mini-game"""
        print("\n" + "=" * 50)
        print("🎯 NUMBER GUESSING CHALLENGE! 🎯")
        print("=" * 50)
        print("I'm thinking of a number between 1 and 100.")
        print("You have 10 attempts to guess it!")
        print("=" * 50)
        
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        
        while attempts < max_attempts:
            attempts += 1
            print(f"\nAttempt {attempts}/{max_attempts}")
            
            try:
                guess = int(input("Enter your guess (1-100): "))
                
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100!")
                    continue
                
                if guess == secret_number:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                    bonus_points = max(1, 11 - attempts)  # More points for fewer attempts
                    self.score += bonus_points
                    print(f"🎁 Bonus points earned: {bonus_points}")
                    return True
                elif guess < secret_number:
                    print("📈 Too low! Try a higher number.")
                else:
                    print("📉 Too high! Try a lower number.")
                
                # Give a hint after 5 attempts
                if attempts == 5:
                    if secret_number % 2 == 0:
                        print("💡 Hint: The number is even!")
                    else:
                        print("💡 Hint: The number is odd!")
                
            except ValueError:
                print("Please enter a valid number!")
                continue
        
        print(f"\n😔 Game Over! The number was {secret_number}.")
        return False
    
    def run_quiz(self):
        """Run the main quiz"""
        print("\n" + "=" * 50)
        print("📝 QUIZ SECTION")
        print("=" * 50)
        
        # Shuffle questions for variety
        quiz_questions = random.sample(self.questions, min(5, len(self.questions)))
        
        for i, question_data in enumerate(quiz_questions, 1):
            print(f"\nQuestion {i} of {len(quiz_questions)}")
            self.display_question(question_data)
            player_answer = self.get_answer()
            self.check_answer(player_answer, question_data['correct'], question_data['explanation'])
            
            # Add a small delay for better readability
            time.sleep(1)
    
    def display_final_results(self, player_name):
        """Display final results and score"""
        self.clear_screen()
        print("=" * 60)
        print("🏁 FINAL RESULTS 🏁")
        print("=" * 60)
        print(f"Player: {player_name}")
        print(f"Total Questions: {self.total_questions}")
        print(f"Correct Answers: {self.score}")
        print(f"Score: {self.score}/{self.total_questions}")
        
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        
        print(f"Percentage: {percentage:.1f}%")
        print()
        
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
        
        print(f"Grade: {grade}")
        print(f"Message: {message}")
        print("=" * 60)
    
    def play_again(self):
        """Ask if player wants to play again"""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'!")
    
    def run_game(self):
        """Main game loop"""
        while True:
            self.print_welcome()
            player_name = self.get_player_name()
            
            # Reset score for new game
            self.score = 0
            self.total_questions = 0
            
            # Run quiz section
            self.run_quiz()
            
            # Run number guessing game
            self.number_guessing_game()
            
            # Display final results
            self.display_final_results(player_name)
            
            # Ask to play again
            if not self.play_again():
                print("\n👋 Thanks for playing! Goodbye!")
                break

def main():
    """Main function to start the game"""
    game = QuizGame()
    try:
        game.run_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the game again.")

if __name__ == "__main__":
    main() 