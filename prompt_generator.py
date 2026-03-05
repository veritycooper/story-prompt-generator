import random

characters = [
    "a disgraced knight",
    "a runaway prince",
    "a young mage",
    "a cursed warrior",
    "a forgotten god",
    "a thief with a secret past"
]

settings = [
    "in a ruined empire",
    "inside a floating city",
    "in a kingdom at war",
    "in a world where magic is dying",
    "inside an ancient forest",
    "in a land ruled by dragons"
]

conflicts = [
    "must defeat the god that cursed their bloodline",
    "must stop a war before the sun disappears",
    "must uncover a conspiracy threatening the throne",
    "must break a curse before time runs out",
    "must survive a deadly magical trial",
    "must face the person they once loved"
]

character = random.choice(characters)
setting = random.choice(settings)
conflict = random.choice(conflicts)

print("\n--- Story Prompt ---\n")
print(f"Hero: {character}")
print(f"Setting: {setting}")
print(f"Conflict: {conflict}")
