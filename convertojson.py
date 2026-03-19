import re
import json

with open("./files/pokemon_moves_list.txt", "r", encoding="utf-8") as f:
    raw = f.read()

# Strip TS header
start = raw.find("{")
raw = raw[start:]

# Remove ending semicolon
raw = raw.rstrip().rstrip(";")

# Quote bare keys
fixed = re.sub(r'([{\s,])([A-Za-z0-9_]+)\s*:', r'\1"\2":', raw)

# Convert single-quoted strings to double-quoted strings
fixed = re.sub(r"'([^'\\]*(?:\\.[^'\\]*)*)'", r'"\1"', fixed)

# Remove trailing commas before } or ]
fixed = re.sub(r',(\s*[}\]])', r'\1', fixed)

try:
    pokemon_moves = json.loads(fixed)
    print("Loaded successfully.")
    print("bulbasaur" in pokemon_moves)
    print(list(pokemon_moves["bulbasaur"]["learnset"].keys())[:10])

    with open("./files/learnsets.json", "w", encoding="utf-8") as out:
        json.dump(pokemon_moves, out, indent=2)

except json.JSONDecodeError as e:
    print("JSON error:", e)
    print(fixed[max(0, e.pos - 300):e.pos + 300])