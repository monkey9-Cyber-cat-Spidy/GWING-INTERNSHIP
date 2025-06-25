"""
Core logic for The Kingdom of Shadows: Complete Saga
Contains the story structure, branching logic, and game engine for use in both console and web versions.
"""
import json
import os
from copy import deepcopy

# --- Story Data Structure ---

STORY = {
    "prologue": {
        "text": (
            "The Kingdom of Vaeloria was once the light of the world,\n"
            "held together by steel, magic, and unshakable oaths.\n\n"
            "Then came the Shadow Plague. Whole cities vanished.\n"
            "People twisted into beasts. The sky wept black for weeks.\n"
            "And at the heart of it all: the Shadow King, a fallen knight\n"
            "who pierced the sun and drank the void.\n\n"
            "You are Kairo, once a knight of the Sun Court, now a fugitive.\n"
            "You were betrayed. Banished. Marked with a curse.\n\n"
            "You wanted peace. But when the winds howl and the ravens circle,\n"
            "you know deep in your bones: 'It's not over.'"
        ),
        "choices": [
            {
                "desc": "Burn the letter and stay in exile",
                "next": "exile_path",
                "effects": {"shadow_mark": 10, "reputation": -10, "elira": -20, "choice": "burned_letter"}
            },
            {
                "desc": "Ride to Highspire immediately",
                "next": "highspire",
                "effects": {"reputation": 10, "elira": 10, "choice": "rode_immediately"}
            },
            {
                "desc": "Investigate the letter's authenticity first",
                "next": "investigate_letter",
                "effects": {"old_light": 5, "choice": "investigated_letter"}
            },
            {
                "desc": "Head to Driftmark instead",
                "next": "driftmark",
                "effects": {"reputation": -5, "choice": "went_to_driftmark"}
            }
        ]
    },
    "exile_path": {
        "text": (
            "You burn the letter. The flames eat away at the last tie to your old life.\n"
            "You remain in exile, haunted by dreams of a kingdom in ruin.\n"
            "But the darkness grows. One night, the Shadow King's minions find you.\n"
            "You fight bravely, but alone, you cannot stop the tide.\n"
            "Your story ends in the shadows, but legends whisper of your sacrifice."
        ),
        "choices": [
            {"desc": "Accept your fate (Ending)", "next": "epilogue_hermit", "effects": {}}
        ]
    },
    "highspire": {
        "text": (
            "You ride to Highspire. The city burns. Shadow beasts roam the streets.\n"
            "Atop the tower stands Elira, pale and possessed. The Shadow King emerges.\n"
            "You must act."
        ),
        "choices": [
            {"desc": "Fight the Shadow King directly", "next": "fight_shadow_king", "effects": {"health": -30, "shadow_mark": 25, "old_light": 10, "choice": "fought_shadow_king"}},
            {"desc": "Flee immediately", "next": "flee_highspire", "effects": {"reputation": -20, "choice": "fled_highspire"}},
            {"desc": "Try to reason with Elira", "next": "reason_with_elira", "effects": {"elira": 20, "old_light": 10, "choice": "reasoned_with_elira"}},
            {"desc": "Use your shadow mark to resist", "next": "use_shadow_mark", "effects": {"shadow_mark": 20, "choice": "used_shadow_mark"}}
        ]
    },
    "investigate_letter": {
        "text": (
            "You investigate the letter. It's genuine, but laced with a subtle magic.\n"
            "You sense a warning: the Shadow King is watching.\n"
            "You must choose your next move carefully."
        ),
        "choices": [
            {"desc": "Go to Highspire", "next": "highspire", "effects": {"choice": "rode_immediately"}},
            {"desc": "Go to Driftmark", "next": "driftmark", "effects": {"choice": "went_to_driftmark"}}
        ]
    },
    "driftmark": {
        "text": (
            "You head to Driftmark, city of thieves and pirates.\n"
            "You find Lazra, an assassin you once saved. She warns you of a cult: The Eclipsed.\n"
            "They serve the Shadow King. You must decide your approach."
        ),
        "choices": [
            {"desc": "Kill Elira without hesitation", "next": "kill_elira", "effects": {"elira": -100, "shadow_mark": 20, "choice": "killed_elira"}},
            {"desc": "Try to save her one last time", "next": "save_elira", "effects": {"elira": 40, "old_light": 20, "choice": "saved_elira"}},
            {"desc": "Pretend to join the cult", "next": "pretend_to_join", "effects": {"shadow_mark": 10, "choice": "pretended_to_join"}},
            {"desc": "Escape and leave her to her fate", "next": "escape_driftmark", "effects": {"reputation": -10, "choice": "escaped_driftmark"}}
        ]
    },
    "fight_shadow_king": {
        "text": (
            "You face the Shadow King in battle. His power is overwhelming.\n"
            "You are wounded, but manage to escape with your life.\n"
            "You seek help from the druids in Elderglen."
        ),
        "choices": [
            {"desc": "Train with the druids to master your powers", "next": "train_with_druids", "effects": {"old_light": 25, "health": 15, "shadow_mark": 10, "druids": 30, "choice": "trained_with_druids"}},
            {"desc": "Continue fighting alone", "next": "epilogue_eternal_warrior", "effects": {}}
        ]
    },
    "flee_highspire": {
        "text": (
            "You flee Highspire. The city falls. Guilt haunts you, but you survive.\n"
            "You wander the land, hunted by shadows."
        ),
        "choices": [
            {"desc": "Seek understanding of your new nature", "next": "epilogue_seeker", "effects": {}}
        ]
    },
    "reason_with_elira": {
        "text": (
            "You try to reason with Elira. For a moment, her true self breaks through.\n"
            "She begs you to end her suffering or save her."
        ),
        "choices": [
            {"desc": "Kill Elira to end her pain", "next": "kill_elira", "effects": {"elira": -100, "shadow_mark": 20, "choice": "killed_elira"}},
            {"desc": "Try to save her", "next": "save_elira", "effects": {"elira": 40, "old_light": 20, "choice": "saved_elira"}}
        ]
    },
    "use_shadow_mark": {
        "text": (
            "You unleash your shadow mark. The Shadow King is impressed, but you feel your humanity slipping.\n"
            "He offers you a place at his side."
        ),
        "choices": [
            {"desc": "Pretend to join him, then betray", "next": "pretend_to_join", "effects": {"shadow_mark": 10, "choice": "pretended_to_join"}},
            {"desc": "Refuse and fight", "next": "fight_shadow_king", "effects": {"health": -20, "choice": "fought_shadow_king"}}
        ]
    },
    "kill_elira": {
        "text": (
            "You kill Elira. The act scars your soul, but the Shadow King is weakened.\n"
            "You are left with a choice: continue fighting or disappear."
        ),
        "choices": [
            {"desc": "Continue fighting the cultists", "next": "epilogue_eternal_warrior", "effects": {}},
            {"desc": "Disappear into the wilderness", "next": "epilogue_hermit", "effects": {}}
        ]
    },
    "save_elira": {
        "text": (
            "You save Elira, breaking the Shadow King's hold. Together, you rebuild Highspire.\n"
            "But the darkness lingers."
        ),
        "choices": [
            {"desc": "Return to Highspire as a hero", "next": "epilogue_legend", "effects": {}}
        ]
    },
    "pretend_to_join": {
        "text": (
            "You pretend to join the Shadow King. You learn his secrets, then betray him at the last moment.\n"
            "The world is saved, but you are forever changed."
        ),
        "choices": [
            {"desc": "Seek understanding of your new nature", "next": "epilogue_seeker", "effects": {}}
        ]
    },
    "escape_driftmark": {
        "text": (
            "You escape Driftmark, leaving Elira to her fate. The world moves on, but you are haunted by regret."
        ),
        "choices": [
            {"desc": "Disappear into the wilderness", "next": "epilogue_hermit", "effects": {}}
        ]
    },
    "train_with_druids": {
        "text": (
            "You train with the druids, mastering your powers. You are ready for the final battle.\n"
            "You ride for the Obsidian Citadel, where the Shadow King awaits."
        ),
        "choices": [
            {"desc": "Confront the Shadow King", "next": "final_battle", "effects": {"choice": "confronted_shadow_king"}}
        ]
    },
    "final_battle": {
        "text": (
            "The battle is biblical. Ashfang glows with Old Light.\n"
            "You defeat the Shadow King, but at great cost.\n"
            "You must choose your path forward."
        ),
        "choices": [
            {"desc": "Return to Highspire as a hero", "next": "epilogue_legend", "effects": {}},
            {"desc": "Continue fighting the cultists", "next": "epilogue_eternal_warrior", "effects": {}},
            {"desc": "Seek understanding of your new nature", "next": "epilogue_seeker", "effects": {}},
            {"desc": "Disappear into the wilderness", "next": "epilogue_hermit", "effects": {}}
        ]
    }
}

# --- Default Character State ---

def default_character(name="Kairo"):
    return {
        "name": name or "Kairo Nightvale",
        "health": 100,
        "shadow_mark": 0,
        "old_light": 0,
        "reputation": 50,
        "inventory": ["Ashfang", "Letter from Elira"],
        "relationships": {"elira": 0, "lazra": 0, "shadow_king": -50, "druids": 0},
        "choices_made": [],
        "story_path": []
    }

# --- Game Engine ---

class KingdomOfShadowsGame:
    def __init__(self, name="Kairo", state=None, current_node=None, ended=None, epilogue=None):
        self.character = deepcopy(state) if state else default_character(name)
        self.current_node = current_node if current_node else "prologue"
        self.ended = ended if ended is not None else False
        self.epilogue = epilogue

    def get_current_story(self):
        node = STORY[self.current_node]
        return node["text"], [c["desc"] for c in node.get("choices", [])]

    def make_choice(self, choice_idx):
        node = STORY[self.current_node]
        if self.ended or choice_idx < 0 or choice_idx >= len(node["choices"]):
            return False
        choice = node["choices"][choice_idx]
        # Apply effects
        effects = choice.get("effects", {})
        for k, v in effects.items():
            if k == "choice":
                self.character["choices_made"].append(v)
                self.character["story_path"].append(v)
            elif k in self.character:
                self.character[k] += v
            elif k in self.character["relationships"]:
                self.character["relationships"][k] += v
        # Move to next node
        self.current_node = choice["next"]
        # Check for ending
        if self.current_node.startswith("epilogue_"):
            self.ended = True
            self.epilogue = self.current_node
        else:
            self.ended = False
            self.epilogue = None
        return True

    def is_ended(self):
        return self.ended

    def get_epilogue(self):
        if not self.ended:
            return None
        return EPILOGUES[self.epilogue]

    def get_stats(self):
        return deepcopy(self.character)

    def save(self, path):
        with open(path, "w") as f:
            json.dump({
                "character": self.character,
                "current_node": self.current_node,
                "ended": self.ended,
                "epilogue": self.epilogue
            }, f, indent=2)

    @staticmethod
    def load(path):
        if not os.path.exists(path):
            return None
        with open(path) as f:
            data = json.load(f)
        return KingdomOfShadowsGame(
            state=data["character"],
            current_node=data.get("current_node", "prologue"),
            ended=data.get("ended", False),
            epilogue=data.get("epilogue")
        )

# --- Epilogues (to be filled in next edit) ---

EPILOGUES = {
    "epilogue_hermit": {
        "title": "The Hermit",
        "text": (
            "You disappear into the wilderness, carrying the Shadow King within you.\n"
            "The darkness and light war inside your soul. Centuries pass. Legends grow.\n"
            "Some say you became a wandering spirit, watching over the world from the shadows."
        )
    },
    "epilogue_legend": {
        "title": "The Legend",
        "text": (
            "You return to Highspire as a hero, though changed forever.\n"
            "The people hail you as their savior, but they don't understand the price you paid.\n"
            "You rule wisely, using both your human wisdom and the Shadow King's knowledge to rebuild the kingdom."
        )
    },
    "epilogue_eternal_warrior": {
        "title": "The Eternal Warrior",
        "text": (
            "You continue fighting, using your new powers to hunt down the remaining cultists and protect the innocent.\n"
            "You become a legend among warriors, known as the Blade of Eclipse—part man, part shadow, all protector."
        )
    },
    "epilogue_seeker": {
        "title": "The Seeker",
        "text": (
            "You dedicate your life to understanding the nature of light and shadow, good and evil.\n"
            "You write treatises that change how people think about morality and power.\n"
            "Your wisdom guides future generations."
        )
    }
}

# --- More story nodes and epilogues will be filled in next edit ---
