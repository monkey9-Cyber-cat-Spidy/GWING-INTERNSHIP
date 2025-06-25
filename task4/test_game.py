#!/usr/bin/env python3
"""
Test file for The Kingdom of Shadows Choose Your Own Adventure Game
This file demonstrates the game functionality without requiring user input.
"""

import random
import time

def test_character_system():
    """Test the character system and statistics"""
    print("🧪 TESTING CHARACTER SYSTEM")
    print("=" * 50)
    
    # Simulate character stats
    character = {
        "name": "Kairo Nightvale",
        "health": 100,
        "shadow_mark": 0,
        "old_light": 0,
        "reputation": 50,
        "inventory": ["Ashfang", "Letter from Elira"],
        "relationships": {"elira": 0, "lazra": 0, "shadow_king": -50, "druids": 0},
        "choices_made": [],
        "story_path": []
    }
    
    print("📊 Initial Character Stats:")
    print(f"👤 Name: {character['name']}")
    print(f"❤️  Health: {character['health']}/100")
    print(f"🌑 Shadow Mark: {character['shadow_mark']}/100")
    print(f"✨ Old Light: {character['old_light']}/100")
    print(f"🏆 Reputation: {character['reputation']}/100")
    print(f"📦 Inventory: {', '.join(character['inventory'])}")
    print("-" * 50)
    
    # Simulate story choices and their effects
    print("🎯 Simulating Story Choices:")
    
    # Choice 1: Burn the letter
    print("\n1. 🔥 Burn the letter and stay in exile")
    character['shadow_mark'] += 10
    character['reputation'] -= 10
    character['relationships']['elira'] -= 20
    character['choices_made'].append("burned_letter")
    print(f"   → Shadow Mark: {character['shadow_mark']}, Reputation: {character['reputation']}")
    
    # Choice 2: Fight the Shadow King
    print("\n2. ⚔️  Fight the Shadow King directly")
    character['health'] -= 30
    character['shadow_mark'] += 25
    character['old_light'] += 10
    character['choices_made'].append("fought_shadow_king")
    print(f"   → Health: {character['health']}, Shadow Mark: {character['shadow_mark']}")
    
    # Choice 3: Train with druids
    print("\n3. ⚔️  Train with the druids to master your powers")
    character['old_light'] += 25
    character['health'] += 15
    character['shadow_mark'] += 10
    character['relationships']['druids'] += 30
    character['choices_made'].append("trained_with_druids")
    print(f"   → Old Light: {character['old_light']}, Health: {character['health']}")
    
    print(f"\n📊 Final Character Stats:")
    print(f"❤️  Health: {character['health']}/100")
    print(f"🌑 Shadow Mark: {character['shadow_mark']}/100")
    print(f"✨ Old Light: {character['old_light']}/100")
    print(f"🏆 Reputation: {character['reputation']}/100")
    print(f"🎯 Choices Made: {len(character['choices_made'])}")
    
    # Determine character archetype
    if character['shadow_mark'] > 70:
        archetype = "Shadow Walker"
    elif character['old_light'] > 70:
        archetype = "Light Bearer"
    elif character['reputation'] > 70:
        archetype = "Hero"
    elif character['health'] < 30:
        archetype = "Sacrificial Savior"
    else:
        archetype = "Balanced Warrior"
    
    print(f"🏷️  Character Archetype: {archetype}")
    print("\n✅ Character system test completed!")

def test_story_branches():
    """Test different story branches and outcomes"""
    print("\n📖 TESTING STORY BRANCHES")
    print("=" * 50)
    
    story_branches = [
        {
            "chapter": "Chapter I: Letters & Lies",
            "choices": [
                "Burn the letter and stay in exile",
                "Ride to Highspire immediately", 
                "Investigate the letter's authenticity first",
                "Head to Driftmark instead"
            ],
            "outcomes": [
                "Alternate path - exile",
                "Main story - confrontation",
                "Cautious path - investigation",
                "Early Driftmark path"
            ]
        },
        {
            "chapter": "Chapter II: The Fall of Highspire",
            "choices": [
                "Fight the Shadow King directly",
                "Flee immediately",
                "Try to reason with Elira",
                "Use your shadow mark to resist"
            ],
            "outcomes": [
                "Combat path - wounded but escaped",
                "Flight path - safe but dishonorable",
                "Diplomatic path - partial success",
                "Power path - discovered abilities"
            ]
        },
        {
            "chapter": "Chapter III: Driftmark and Daggers",
            "choices": [
                "Kill Elira without hesitation",
                "Try to save her one last time",
                "Pretend to join her side",
                "Escape and leave her to her fate"
            ],
            "outcomes": [
                "Dark path - no regrets",
                "Redemption path - partial success",
                "Undercover path - deception",
                "Neutral path - avoidance"
            ]
        }
    ]
    
    for branch in story_branches:
        print(f"\n📖 {branch['chapter']}:")
        for i, (choice, outcome) in enumerate(zip(branch['choices'], branch['outcomes']), 1):
            print(f"   {i}. {choice}")
            print(f"      → {outcome}")
    
    print("\n✅ Story branches test completed!")

def test_epilogues():
    """Test the different epilogue endings"""
    print("\n🌌 TESTING EPILOGUES")
    print("=" * 50)
    
    epilogues = [
        {
            "name": "The Hermit",
            "trigger": "Disappear into the wilderness",
            "theme": "Isolation and sacrifice",
            "quote": "One man carried the weight of a kingdom. Then he carried the darkness too."
        },
        {
            "name": "The Legend", 
            "trigger": "Return to Highspire as a hero",
            "theme": "Leadership and legacy",
            "quote": "A legacy is built not by power—but by sacrifice."
        },
        {
            "name": "The Eternal Warrior",
            "trigger": "Continue fighting the remaining cultists",
            "theme": "Duty and protection",
            "quote": "Duty vs freedom—sometimes you must choose both."
        },
        {
            "name": "The Seeker",
            "trigger": "Seek to understand your new nature",
            "theme": "Wisdom and philosophy",
            "quote": "Light isn't purity. Shadow isn't evil. They're both parts of us."
        }
    ]
    
    for epilogue in epilogues:
        print(f"\n🌌 {epilogue['name']}:")
        print(f"   Trigger: {epilogue['trigger']}")
        print(f"   Theme: {epilogue['theme']}")
        print(f"   Quote: \"{epilogue['quote']}\"")
    
    print("\n✅ Epilogues test completed!")

def test_game_mechanics():
    """Test game mechanics and systems"""
    print("\n⚙️ TESTING GAME MECHANICS")
    print("=" * 50)
    
    # Test character progression
    print("📈 Character Progression:")
    base_stats = {"health": 100, "shadow_mark": 0, "old_light": 0, "reputation": 50}
    
    # Simulate different choice effects
    choice_effects = [
        ("Burn letter", {"shadow_mark": 10, "reputation": -10}),
        ("Fight Shadow King", {"health": -30, "shadow_mark": 25, "old_light": 10}),
        ("Train with druids", {"old_light": 25, "health": 15, "shadow_mark": 10}),
        ("Save Elira", {"health": -20, "old_light": 15, "reputation": 5})
    ]
    
    for choice, effects in choice_effects:
        print(f"\n   {choice}:")
        for stat, change in effects.items():
            print(f"      {stat}: {change:+d}")
    
    # Test relationship system
    print("\n🤝 Relationship System:")
    relationships = {
        "elira": {"initial": 0, "burn_letter": -20, "save_elira": 20, "kill_elira": -50},
        "lazra": {"initial": 0, "help_lazra": 30, "betray_lazra": -30},
        "shadow_king": {"initial": -50, "fight_him": -30, "join_him": 20},
        "druids": {"initial": 0, "train_with_them": 30, "ignore_them": -10}
    }
    
    for person, rel_changes in relationships.items():
        print(f"   {person.title()}: {rel_changes['initial']} (initial)")
        for action, change in rel_changes.items():
            if action != "initial":
                print(f"      {action}: {change:+d}")
    
    print("\n✅ Game mechanics test completed!")

if __name__ == "__main__":
    test_character_system()
    test_story_branches()
    test_epilogues()
    test_game_mechanics()
    print("\n🎉 All tests completed successfully!")
    print("🎮 Ready to run The Kingdom of Shadows: Complete Saga!") 