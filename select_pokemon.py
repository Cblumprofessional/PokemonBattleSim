import start_menu as sm
import json
import random
import time

def clean_name(name):
    return (
        name.lower()
        .replace(" ", "")
        .replace("-", "")
        .replace(".", "")
        .replace("'", "")
        .replace("♀", "f")
        .replace("♂", "m")
    )

def select_pokemon():
    trainers_pokemon = {}

    with open('./files/pokedex.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

    with open('./files/learnsets.json', 'r', encoding="utf-8") as moves:
        movesset = json.load(moves)

    with open("./files/moveswitheffects.json", "r", encoding="utf-8") as f:
        moveseffects = json.load(f)

    mode = sm.game_mode()
    trainer1 = {}
    trainer2 = {}

    if mode[-1] == "single":
        trainer = mode
        for item in trainer:
            if isinstance(item, dict):
                for key, value in item.items():
                    trainer1[key] = value

        for key, value in trainer1.items():
            print(f"\t{key} : {value}")
        print("\n")

        uSelection = input(
            f'{trainer1["Name"]}, would you like to pick 6 pokemon or have 6 randomly chosen for you? (p/r): '
        )

        for i in range(6):
            pokemonNoNormal = random.choice(data)
            pokemon = pokemonNoNormal
            pokemonNameDict = pokemon["name"]["english"]
            pokemonName = clean_name(pokemonNameDict)

            print(f"\n{i+1}. {pokemon['name']['english']}")
            print(f"   Type: {' / '.join(pokemon['type'])}")

            base = pokemon["base"]
            stats_text = (
                f"HP: {base['HP']} | "
                f"Atk: {base['Attack']} | "
                f"Def: {base['Defense']} | "
                f"SpA: {base['Sp. Attack']} | "
                f"SpD: {base['Sp. Defense']} | "
                f"Spe: {base['Speed']}"
            )
            print(f"   {stats_text}")

            chosen_pokemon = {
                "Name": pokemon["name"]["english"],
                "Type": pokemon["type"],
                "Stats": stats_text,
                "Moves": [],
                "hasStatus": 0,
                "Status": []
            }

            if pokemonName in movesset:
                print("Found pokemon in moveset:", pokemonName)

                allowed_moves = list(movesset[pokemonName]["learnset"].keys())
                chosen_moves = random.sample(allowed_moves, min(4, len(allowed_moves)))

                for move_chosen in chosen_moves:
                    move_data = moveseffects.get(move_chosen)

                    if move_data:
                        chosen_pokemon["Moves"].append({
                            "id": move_chosen,
                            "name": move_data["name"],
                            "power": move_data["basePower"],
                            "accuracy": move_data["accuracy"],
                            "type": move_data["type"],
                            "category": move_data["category"],
                            "effect": move_data["shortDesc"]
                        })
                    else:
                        chosen_pokemon["Moves"].append({
                            "id": move_chosen,
                            "name": move_chosen,
                            "power": None,
                            "accuracy": None,
                            "type": None,
                            "category": None,
                            "effect": "Move data not found"
                        })
            else:
                print("Pokemon not found in learnset:", pokemonName)

            trainers_pokemon[i] = chosen_pokemon

        for key, value in trainers_pokemon.items():
            print(f"\nSlot {key + 1}: {value['Name']}")
            print(f"Type: {' / '.join(value['Type'])}")
            print(value["Stats"])
            print("Moves:")
            for move in value["Moves"]:
                print(
                    f"  - {move['name']} | {move['type']} | {move['category']} | "
                    f"Power: {move['power']} | Accuracy: {move['accuracy']}"
                )
                print(f"    Effect: {move['effect']}")

    print("\n")
    if mode[-1] == "multiplayer":
        trainers = mode
        for item in trainers:
            if isinstance(item, dict):
                for key, value in item.items():
                    if len(trainer1) != 3:
                        trainer1[key] = value
                    else:
                        trainer2[key] = value
                        
        for key, value in trainer1.items():
            print(f"\t{key} : {value}")    
        print("\n") 
        for key, value in trainer2.items():
            print(f"\t{key} : {value}")     

        print("\n") 
        
        uSelection = input(f'{trainer1["Name"]}, would you like to pick 6 pokemon or have 6 randomly chosen for you? (p/r): ')
        
        for i in range(6):
            pokemonNoNormal = random.choice(data)
            pokemon = pokemonNoNormal
            pokemonNameDict = pokemon["name"]["english"]
            pokemonName = clean_name(pokemonNameDict)

            print(f"\n{i+1}. {pokemon['name']['english']}")
            print(f"   Type: {' / '.join(pokemon['type'])}")

            base = pokemon["base"]
            stats_text = (
                f"HP: {base['HP']} | "
                f"Atk: {base['Attack']} | "
                f"Def: {base['Defense']} | "
                f"SpA: {base['Sp. Attack']} | "
                f"SpD: {base['Sp. Defense']} | "
                f"Spe: {base['Speed']}"
            )
            print(f"   {stats_text}")

            chosen_pokemon = {
                "Name": pokemon["name"]["english"],
                "Type": pokemon["type"],
                "Stats": stats_text,
                "Moves": []
            }

            if pokemonName in movesset:
                print("Found pokemon in moveset:", pokemonName)

                allowed_moves = list(movesset[pokemonName]["learnset"].keys())
                chosen_moves = random.sample(allowed_moves, min(4, len(allowed_moves)))

                for move_chosen in chosen_moves:
                    move_data = moveseffects.get(move_chosen)

                    if move_data:
                        chosen_pokemon["Moves"].append({
                            "id": move_chosen,
                            "name": move_data["name"],
                            "power": move_data["basePower"],
                            "accuracy": move_data["accuracy"],
                            "type": move_data["type"],
                            "category": move_data["category"],
                            "effect": move_data["shortDesc"]
                        })
                    else:
                        chosen_pokemon["Moves"].append({
                            "id": move_chosen,
                            "name": move_chosen,
                            "power": None,
                            "accuracy": None,
                            "type": None,
                            "category": None,
                            "effect": "Move data not found"
                        })
            else:
                print("Pokemon not found in learnset:", pokemonName)

            trainers_pokemon[i] = chosen_pokemon
        print(f'{trainer1["Name"]}, "pokemon"')
        for key, value in trainers_pokemon.items():
            print(f"\nSlot {key + 1}: {value['Name']}")
            print(f"Type: {' / '.join(value['Type'])}")
            print(value["Stats"])
            print("Moves:")
            for move in value["Moves"]:
                print(
                    f"  - {move['name']} | {move['type']} | {move['category']} | "
                    f"Power: {move['power']} | Accuracy: {move['accuracy']}"
                )
                print(f"    Effect: {move['effect']}")


        uSelection = input(f'{trainer2["Name"]}, would you like to pick 6 pokemon or have 6 randomly chosen for you? (p/r): ')
        for i in range(6):
            pokemonNoNormal = random.choice(data)
            pokemon = pokemonNoNormal
            pokemonNameDict = pokemon["name"]["english"]
            pokemonName = clean_name(pokemonNameDict)

            print(f"\n{i+1}. {pokemon['name']['english']}")
            print(f"   Type: {' / '.join(pokemon['type'])}")

            base = pokemon["base"]
            stats_text = (
                f"HP: {base['HP']} | "
                f"Atk: {base['Attack']} | "
                f"Def: {base['Defense']} | "
                f"SpA: {base['Sp. Attack']} | "
                f"SpD: {base['Sp. Defense']} | "
                f"Spe: {base['Speed']}"
            )
            print(f"   {stats_text}")

            chosen_pokemon = {
                "Name": pokemon["name"]["english"],
                "Type": pokemon["type"],
                "Stats": stats_text,
                "Moves": []
            }

            if pokemonName in movesset:
                print("Found pokemon in moveset:", pokemonName)

                allowed_moves = list(movesset[pokemonName]["learnset"].keys())
                chosen_moves = random.sample(allowed_moves, min(4, len(allowed_moves)))

                for move_chosen in chosen_moves:
                    move_data = moveseffects.get(move_chosen)

                    if move_data:
                        chosen_pokemon["Moves"].append({
                            "id": move_chosen,
                            "name": move_data["name"],
                            "power": move_data["basePower"],
                            "accuracy": move_data["accuracy"],
                            "type": move_data["type"],
                            "category": move_data["category"],
                            "effect": move_data["shortDesc"]
                        })
                    else:
                        chosen_pokemon["Moves"].append({
                            "id": move_chosen,
                            "name": move_chosen,
                            "power": None,
                            "accuracy": None,
                            "type": None,
                            "category": None,
                            "effect": "Move data not found"
                        })
            else:
                print("Pokemon not found in learnset:", pokemonName)

            trainers_pokemon[i] = chosen_pokemon

        print(f'{trainer1["Name"]}, "pokemon"')
        for key, value in trainers_pokemon.items():
            print(f"\nSlot {key + 1}: {value['Name']}")
            print(f"Type: {' / '.join(value['Type'])}")
            print(value["Stats"])
            print("Moves:")
            for move in value["Moves"]:
                print(
                    f"  - {move['name']} | {move['type']} | {move['category']} | "
                    f"Power: {move['power']} | Accuracy: {move['accuracy']}"
                )
                print(f"    Effect: {move['effect']}")

    print("\n")