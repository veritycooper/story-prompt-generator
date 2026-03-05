import random

# Genre data
genres = {
    "1": {
        "name": "Fantasy",
        "characters": ["dragon rider", "exiled prince", "battle mage", "forest guardian", "runaway noble"],
        "settings": ["a cursed kingdom", "a floating city", "an ancient forest", "a collapsing empire"]
    },
    "2": {
        "name": "Sci-Fi",
        "characters": ["rogue pilot", "android detective", "space smuggler", "genetic experiment", "AI engineer"],
        "settings": ["a distant colony", "a failing space station", "a cyberpunk megacity", "a newly discovered planet"]
    },
    "3": {
        "name": "Romance",
        "characters": ["small town baker", "travelling musician", "overworked journalist", "aspiring artist"],
        "settings": ["a quiet seaside town", "a bustling city café", "a wedding destination", "a snowy mountain lodge"]
    },
    "4": {
        "name": "Mystery",
        "characters": ["retired detective", "crime journalist", "amateur sleuth", "forensic analyst"],
        "settings": ["a foggy coastal town", "an old mansion", "a quiet university campus", "a historic village"]
    }
}

# Tropes
tropes = {
    "1": "Enemies to Lovers",
    "2": "Chosen One",
    "3": "Revenge",
    "4": "Forbidden Love",
    "5": "Betrayal",
    "6": "Random"
}

# Goals / conflicts
goals = [
    "uncover a dangerous secret",
    "prevent a catastrophe",
    "solve a mysterious disappearance",
    "break an ancient curse",
    "stop a growing conspiracy"
]


print("\nChoose a genre:\n")

for key, genre in genres.items():
    print(f"{key}. {genre['name']}")

genre_choice = input("\nEnter genre number: ")

selected_genre = genres.get(genre_choice, random.choice(list(genres.values())))

print("\nChoose a trope:\n")

for key, trope in tropes.items():
    print(f"{key}. {trope}")

trope_choice = input("\nEnter trope number: ")

trope = tropes.get(trope_choice, "Random")

character = random.choice(selected_genre["characters"])
setting = random.choice(selected_genre["settings"])
goal = random.choice(goals)

print("\n--- Story Prompt ---\n")

print(f"Genre: {selected_genre['name']}")
print(f"Trope: {trope}")

print("\nPrompt:\n")
print(f"A {character} in {setting} must {goal}.")
