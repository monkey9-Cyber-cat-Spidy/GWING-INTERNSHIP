
import random
import time
import os
import json
from datetime import datetime

class RockPaperScissors:
    def __init__(self):
        self.player_name = ""
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.games_played = 0
        self.game_history = []
        self.choices = {
            "rock": {"emoji": "🪨", "beats": "scissors", "loses_to": "paper"},
            "paper": {"emoji": "📄", "beats": "rock", "loses_to": "scissors"},
            "scissors": {"emoji": "✂️", "beats": "paper", "loses_to": "rock"}
        }
        self.statistics = self.load_statistics()
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_welcome(self):
        """Display welcome message"""
        self.clear_screen()
        print("=" * 60)
        print("🪨📄✂️ WELCOME TO ROCK, PAPER, SCISSORS! 🪨📄✂️")
        print("=" * 60)
        print("🎮 Features:")
        print("   • Play against the computer")
        print("   • Score tracking and statistics")
        print("   • Game history and analysis")
        print("   • Beautiful interface with emojis")
        print("   • Multiple game modes")
        print("=" * 60)
        print()
    
    def get_player_name(self):
        """Get player's name"""
        while True:
            name = input("Enter your name: ").strip()
            if name:
                return name
            print("Please enter a valid name!")
    
    def display_rules(self):
        """Display game rules"""
        print("\n📋 GAME RULES:")
        print("-" * 40)
        print("🪨 Rock crushes ✂️ Scissors")
        print("📄 Paper covers 🪨 Rock")
        print("✂️ Scissors cut 📄 Paper")
        print("-" * 40)
        print("🎯 Choose your weapon and try to beat the computer!")
        print("📊 Your score will be tracked throughout the session.")
        print("-" * 40)
        input("Press Enter to continue...")
    
    def display_choices(self):
        """Display available choices"""
        print("\n🎯 CHOOSE YOUR WEAPON:")
        print("-" * 30)
        for i, (choice, info) in enumerate(self.choices.items(), 1):
            print(f"{i}. {info['emoji']} {choice.title()}")
        print("4. 📊 View Statistics")
        print("5. 📜 View Game History")
        print("6. 🚪 Exit Game")
        print("-" * 30)
    
    def get_player_choice(self):
        """Get player's choice"""
        while True:
            try:
                choice = int(input("Enter your choice (1-6): "))
                if 1 <= choice <= 6:
                    return choice
                else:
                    print("Please enter a number between 1 and 6!")
            except ValueError:
                print("Please enter a valid number!")
    
    def get_computer_choice(self):
        """Get computer's choice"""
        return random.choice(list(self.choices.keys()))
    
    def determine_winner(self, player_choice, computer_choice):
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return "tie"
        elif self.choices[player_choice]["beats"] == computer_choice:
            return "player"
        else:
            return "computer"
    
    def display_round_result(self, player_choice, computer_choice, result):
        """Display the result of a round"""
        player_emoji = self.choices[player_choice]["emoji"]
        computer_emoji = self.choices[computer_choice]["emoji"]
        
        print(f"\n🎮 ROUND RESULT:")
        print("-" * 40)
        print(f"👤 {self.player_name}: {player_emoji} {player_choice.title()}")
        print(f"🤖 Computer: {computer_emoji} {computer_choice.title()}")
        print("-" * 40)
        
        if result == "tie":
            print("🤝 It's a tie!")
            print("💭 Both players chose the same weapon.")
        elif result == "player":
            print(f"🎉 {self.player_name} wins!")
            print(f"💪 {player_choice.title()} {self.get_win_phrase(player_choice, computer_choice)}")
        else:
            print("😔 Computer wins!")
            print(f"💪 {computer_choice.title()} {self.get_win_phrase(computer_choice, player_choice)}")
        
        print("-" * 40)
    
    def get_win_phrase(self, winner_choice, loser_choice):
        """Get a descriptive phrase for how the winner won"""
        phrases = {
            "rock": {
                "scissors": "crushes scissors"
            },
            "paper": {
                "rock": "covers rock"
            },
            "scissors": {
                "paper": "cuts paper"
            }
        }
        return phrases[winner_choice][loser_choice]
    
    def update_scores(self, result):
        """Update scores based on round result"""
        if result == "player":
            self.player_score += 1
        elif result == "computer":
            self.computer_score += 1
        else:
            self.ties += 1
        
        self.games_played += 1
    
    def display_current_score(self):
        """Display current score"""
        print(f"\n📊 CURRENT SCORE:")
        print("-" * 30)
        print(f"👤 {self.player_name}: {self.player_score}")
        print(f"🤖 Computer: {self.computer_score}")
        print(f"🤝 Ties: {self.ties}")
        print(f"🎮 Total Games: {self.games_played}")
        print("-" * 30)
        
        if self.games_played > 0:
            win_rate = (self.player_score / self.games_played) * 100
            print(f"📈 Win Rate: {win_rate:.1f}%")
            print("-" * 30)
    
    def display_statistics(self):
        """Display detailed statistics"""
        print("\n📊 DETAILED STATISTICS:")
        print("=" * 50)
        print(f"👤 Player: {self.player_name}")
        print(f"🎮 Total Games: {self.games_played}")
        print(f"🏆 Wins: {self.player_score}")
        print(f"😔 Losses: {self.computer_score}")
        print(f"🤝 Ties: {self.ties}")
        
        if self.games_played > 0:
            win_rate = (self.player_score / self.games_played) * 100
            loss_rate = (self.computer_score / self.games_played) * 100
            tie_rate = (self.ties / self.games_played) * 100
            
            print(f"📈 Win Rate: {win_rate:.1f}%")
            print(f"📉 Loss Rate: {loss_rate:.1f}%")
            print(f"📊 Tie Rate: {tie_rate:.1f}%")
        
        # Display choice statistics
        if self.game_history:
            print("\n🎯 CHOICE ANALYSIS:")
            print("-" * 30)
            player_choices = [game['player_choice'] for game in self.game_history]
            choice_counts = {}
            for choice in self.choices.keys():
                choice_counts[choice] = player_choices.count(choice)
            
            for choice, count in choice_counts.items():
                percentage = (count / len(player_choices)) * 100 if player_choices else 0
                emoji = self.choices[choice]['emoji']
                print(f"{emoji} {choice.title()}: {count} times ({percentage:.1f}%)")
        
        print("=" * 50)
    
    def display_game_history(self):
        """Display recent game history"""
        if not self.game_history:
            print("\n📜 No games played yet!")
            return
        
        print("\n📜 RECENT GAME HISTORY:")
        print("=" * 60)
        print(f"{'Round':<6} {'Player':<12} {'Computer':<12} {'Result':<10} {'Score'}")
        print("-" * 60)
        
        # Show last 10 games
        recent_games = self.game_history[-10:]
        for i, game in enumerate(recent_games, 1):
            player_emoji = self.choices[game['player_choice']]['emoji']
            computer_emoji = self.choices[game['computer_choice']]['emoji']
            
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
    
    def save_game_result(self, player_choice, computer_choice, result):
        """Save game result to history"""
        game_data = {
            'player_choice': player_choice,
            'computer_choice': computer_choice,
            'result': result,
            'player_score': self.player_score,
            'computer_score': self.computer_score,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.game_history.append(game_data)
        
        # Keep only last 50 games to prevent memory issues
        if len(self.game_history) > 50:
            self.game_history = self.game_history[-50:]
    
    def save_statistics(self):
        """Save statistics to file"""
        stats_data = {
            'player_name': self.player_name,
            'total_games': self.games_played,
            'player_wins': self.player_score,
            'computer_wins': self.computer_score,
            'ties': self.ties,
            'last_updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'game_history': self.game_history[-20:]  # Save last 20 games
        }
        
        try:
            with open('task 3/statistics.json', 'w') as f:
                json.dump(stats_data, f, indent=2)
        except Exception as e:
            print(f"Could not save statistics: {e}")
    
    def load_statistics(self):
        """Load statistics from file"""
        try:
            with open('task 3/statistics.json', 'r') as f:
                data = json.load(f)
                self.player_name = data.get('player_name', '')
                self.games_played = data.get('total_games', 0)
                self.player_score = data.get('player_wins', 0)
                self.computer_score = data.get('computer_wins', 0)
                self.ties = data.get('ties', 0)
                self.game_history = data.get('game_history', [])
                return data
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Could not load statistics: {e}")
            return {}
    
    def play_round(self):
        """Play a single round"""
        choice_num = self.get_player_choice()
        
        if choice_num == 4:  # View Statistics
            self.display_statistics()
            input("\nPress Enter to continue...")
            return "menu"
        elif choice_num == 5:  # View Game History
            self.display_game_history()
            input("\nPress Enter to continue...")
            return "menu"
        elif choice_num == 6:  # Exit Game
            return "exit"
        
        # Get player's choice
        choice_names = list(self.choices.keys())
        player_choice = choice_names[choice_num - 1]
        
        # Get computer's choice
        computer_choice = self.get_computer_choice()
        
        # Determine winner
        result = self.determine_winner(player_choice, computer_choice)
        
        # Display result
        self.display_round_result(player_choice, computer_choice, result)
        
        # Update scores
        self.update_scores(result)
        
        # Save game result
        self.save_game_result(player_choice, computer_choice, result)
        
        # Display current score
        self.display_current_score()
        
        return "continue"
    
    def display_final_results(self):
        """Display final results when exiting"""
        print("\n🏁 FINAL RESULTS:")
        print("=" * 40)
        print(f"👤 {self.player_name}: {self.player_score} wins")
        print(f"🤖 Computer: {self.computer_score} wins")
        print(f"🤝 Ties: {self.ties}")
        print(f"🎮 Total Games: {self.games_played}")
        
        if self.games_played > 0:
            win_rate = (self.player_score / self.games_played) * 100
            print(f"📈 Final Win Rate: {win_rate:.1f}%")
            
            if self.player_score > self.computer_score:
                print("🏆 Congratulations! You won the session!")
            elif self.computer_score > self.player_score:
                print("😔 The computer won this session. Better luck next time!")
            else:
                print("🤝 It's a tie! Great competition!")
        
        print("=" * 40)
    
    def run_game(self):
        """Main game loop"""
        while True:
            self.print_welcome()
            
            if not self.player_name:
                self.player_name = self.get_player_name()
            
            self.display_rules()
            
            while True:
                self.display_choices()
                result = self.play_round()
                
                if result == "exit":
                    self.display_final_results()
                    self.save_statistics()
                    print(f"\n👋 Thanks for playing, {self.player_name}!")
                    return
                elif result == "menu":
                    continue
                else:
                    # Ask if player wants to continue
                    while True:
                        choice = input("\nPlay another round? (y/n): ").strip().lower()
                        if choice in ['y', 'yes']:
                            break
                        elif choice in ['n', 'no']:
                            self.display_final_results()
                            self.save_statistics()
                            print(f"\n👋 Thanks for playing, {self.player_name}!")
                            return
                        else:
                            print("Please enter 'y' or 'n'!")

def main():
    """Main function to start the game"""
    game = RockPaperScissors()
    try:
        game.run_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please try running the game again.")

if __name__ == "__main__":
    main() 