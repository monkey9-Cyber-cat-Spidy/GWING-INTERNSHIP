import random
import time
import os
import json
from datetime import datetime

class NumberGuessingGame:
    def __init__(self):
        self.player_name = ""
        self.score = 0
        self.games_played = 0
        self.best_score = 0
        self.difficulty_levels = {
            "easy": {"range": (1, 50), "attempts": 10, "points": 100},
            "medium": {"range": (1, 100), "attempts": 8, "points": 200},
            "hard": {"range": (1, 200), "attempts": 6, "points": 300},
            "expert": {"range": (1, 500), "attempts": 5, "points": 500}
        }
        self.current_difficulty = "medium"
        self.high_scores = self.load_high_scores()
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_welcome(self):
        """Display welcome message"""
        self.clear_screen()
        print("=" * 60)
        print("🎯 WELCOME TO THE NUMBER GUESSING GAME! 🎯")
        print("=" * 60)
        print("🎮 Features:")
        print("   • Multiple difficulty levels")
        print("   • Score tracking and high scores")
        print("   • Hints and feedback")
        print("   • Statistics tracking")
        print("   • Beautiful interface")
        print("=" * 60)
        print()
    
    def get_player_name(self):
        """Get player's name"""
        while True:
            name = input("Enter your name: ").strip()
            if name:
                return name
            print("Please enter a valid name!")
    
    def display_difficulty_menu(self):
        """Display difficulty selection menu"""
        print("\n📊 SELECT DIFFICULTY LEVEL:")
        print("-" * 40)
        for i, (level, config) in enumerate(self.difficulty_levels.items(), 1):
            range_min, range_max = config["range"]
            attempts = config["attempts"]
            points = config["points"]
            print(f"{i}. {level.upper()}: Range {range_min}-{range_max}, "
                  f"{attempts} attempts, {points} points")
        print("-" * 40)
    
    def select_difficulty(self):
        """Let player select difficulty level"""
        while True:
            try:
                choice = int(input("Enter difficulty level (1-4): "))
                if 1 <= choice <= 4:
                    difficulties = list(self.difficulty_levels.keys())
                    self.current_difficulty = difficulties[choice - 1]
                    return
                else:
                    print("Please enter a number between 1 and 4!")
            except ValueError:
                print("Please enter a valid number!")
    
    def display_game_rules(self):
        """Display game rules for current difficulty"""
        config = self.difficulty_levels[self.current_difficulty]
        range_min, range_max = config["range"]
        attempts = config["attempts"]
        points = config["points"]
        
        print(f"\n📋 GAME RULES - {self.current_difficulty.upper()} MODE:")
        print("-" * 50)
        print(f"🎯 Guess a number between {range_min} and {range_max}")
        print(f"🎲 You have {attempts} attempts")
        print(f"🏆 Maximum points: {points}")
        print(f"💡 You'll get hints to help you guess!")
        print("-" * 50)
        input("Press Enter to start the game...")
    
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
    
    def play_game(self):
        """Main game logic"""
        config = self.difficulty_levels[self.current_difficulty]
        range_min, range_max = config["range"]
        max_attempts = config["attempts"]
        base_points = config["points"]
        
        secret_number = random.randint(range_min, range_max)
        attempts_used = 0
        guesses = []
        
        print(f"\n🎮 Starting {self.current_difficulty.upper()} mode...")
        print(f"🎯 I'm thinking of a number between {range_min} and {range_max}")
        print(f"🎲 You have {max_attempts} attempts")
        print("-" * 50)
        
        while attempts_used < max_attempts:
            attempts_used += 1
            attempts_left = max_attempts - attempts_used + 1
            
            print(f"\n📊 Attempt {attempts_used}/{max_attempts} (Attempts left: {attempts_left})")
            
            # Show previous guesses
            if guesses:
                print(f"📝 Previous guesses: {', '.join(map(str, guesses))}")
            
            try:
                guess = int(input(f"🎯 Enter your guess ({range_min}-{range_max}): "))
                
                if guess < range_min or guess > range_max:
                    print(f"❌ Please enter a number between {range_min} and {range_max}!")
                    attempts_used -= 1  # Don't count invalid attempts
                    continue
                
                guesses.append(guess)
                
                if guess == secret_number:
                    print(f"🎉 CONGRATULATIONS! You guessed it in {attempts_used} attempts!")
                    score = self.calculate_score(attempts_used, max_attempts, base_points)
                    print(f"🏆 Score earned: {score} points!")
                    self.score += score
                    self.games_played += 1
                    return True
                elif guess < secret_number:
                    print("📈 Too low! Try a higher number.")
                else:
                    print("📉 Too high! Try a lower number.")
                
                # Provide hints
                hint = self.get_hint(secret_number, attempts_used, max_attempts)
                if hint:
                    print(hint)
                
                # Show remaining attempts
                if attempts_left > 1:
                    print(f"🎲 {attempts_left - 1} attempts remaining...")
                
            except ValueError:
                print("❌ Please enter a valid number!")
                attempts_used -= 1  # Don't count invalid attempts
                continue
        
        print(f"\n😔 Game Over! The number was {secret_number}.")
        print("💪 Better luck next time!")
        self.games_played += 1
        return False
    
    def display_statistics(self):
        """Display player statistics"""
        print("\n📊 YOUR STATISTICS:")
        print("-" * 40)
        print(f"👤 Player: {self.player_name}")
        print(f"🎮 Games Played: {self.games_played}")
        print(f"🏆 Total Score: {self.score}")
        if self.games_played > 0:
            avg_score = self.score / self.games_played
            print(f"📈 Average Score: {avg_score:.1f}")
        print("-" * 40)
    
    def display_high_scores(self):
        """Display high scores"""
        if not self.high_scores:
            print("\n🏆 No high scores yet! Be the first to set one!")
            return
        
        print("\n🏆 HIGH SCORES:")
        print("-" * 40)
        sorted_scores = sorted(self.high_scores, key=lambda x: x['score'], reverse=True)
        for i, score_data in enumerate(sorted_scores[:5], 1):  # Top 5 scores
            print(f"{i}. {score_data['name']}: {score_data['score']} points "
                  f"({score_data['difficulty']}) - {score_data['date']}")
        print("-" * 40)
    
    def save_high_score(self):
        """Save current score to high scores if it's good enough"""
        if self.score > 0:
            score_data = {
                'name': self.player_name,
                'score': self.score,
                'difficulty': self.current_difficulty,
                'date': datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            
            # Check if this is a new high score
            if not self.high_scores or self.score > max(s['score'] for s in self.high_scores):
                print("🏆 NEW HIGH SCORE! 🏆")
            
            self.high_scores.append(score_data)
            self.save_high_scores_to_file()
    
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
    
    def display_menu(self):
        """Display main menu"""
        print("\n📋 MAIN MENU:")
        print("-" * 30)
        print("1. 🎮 Play Game")
        print("2. 📊 View Statistics")
        print("3. 🏆 View High Scores")
        print("4. ⚙️  Change Difficulty")
        print("5. 🚪 Exit")
        print("-" * 30)
    
    def get_menu_choice(self):
        """Get player's menu choice"""
        while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("Please enter a number between 1 and 5!")
            except ValueError:
                print("Please enter a valid number!")
    
    def run_game(self):
        """Main game loop"""
        while True:
            self.print_welcome()
            
            if not self.player_name:
                self.player_name = self.get_player_name()
            
            self.display_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:  # Play Game
                self.display_difficulty_menu()
                self.select_difficulty()
                self.display_game_rules()
                self.play_game()
                self.save_high_score()
                input("\nPress Enter to continue...")
                
            elif choice == 2:  # View Statistics
                self.display_statistics()
                input("\nPress Enter to continue...")
                
            elif choice == 3:  # View High Scores
                self.display_high_scores()
                input("\nPress Enter to continue...")
                
            elif choice == 4:  # Change Difficulty
                self.display_difficulty_menu()
                self.select_difficulty()
                print(f"✅ Difficulty changed to {self.current_difficulty.upper()}")
                input("Press Enter to continue...")
                
            elif choice == 5:  # Exit
                print(f"\n👋 Thanks for playing, {self.player_name}!")
                print("🏆 Final Score:", self.score)
                print("🎮 Games Played:", self.games_played)
                break

def main():
    """Main function to start the game"""
    game = NumberGuessingGame()
    try:
        game.run_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the game again.")

if __name__ == "__main__":
    main() 