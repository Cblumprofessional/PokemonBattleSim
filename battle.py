import select_pokemon as sp
import random
import time
import terminalhelpers as th


type_chart = {
    "Fire": {
        "Grass": 2.0,
        "Water": 0.5,
        "Fire": 0.5,
        "Rock": 0.5,
        "Bug": 2.0,
        "Ice": 2.0,
        "Steel": 2.0
    },
    "Water": {
        "Fire": 2.0,
        "Water": 0.5,
        "Grass": 0.5,
        "Rock": 2.0,
        "Ground": 2.0
    },
    "Electric": {
        "Water": 2.0,
        "Flying": 2.0,
        "Electric": 0.5,
        "Grass": 0.5,
        "Ground": 0.0
    },
    "Fighting": {
        "Normal": 2.0,
        "Ice": 2.0,
        "Rock:": 2.0,
        "Dark": 2.0,
        "Steel": 2.0,
        "Poison": .5,
        "Psychic": .5,
        "Flying": .5,
        "Bug": .5,
        "Fairy": .5,
        "Ghost": 0
    }
}


def get_poke_stat(stats_string, stat_name):
    if stat_name == "Spe":
        return int(stats_string.split(f"{stat_name}: ")[1])
    return int(stats_string.split(f"{stat_name}: ")[1].split(" |")[0])


def get_poke_stats(stats_string):
    return {
        "HP": int(stats_string.split("HP: ")[1].split(" |")[0]),
        "Atk": int(stats_string.split("Atk: ")[1].split(" |")[0]),
        "Def": int(stats_string.split("Def: ")[1].split(" |")[0]),
        "SpA": int(stats_string.split("SpA: ")[1].split(" |")[0]),
        "SpD": int(stats_string.split("SpD: ")[1].split(" |")[0]),
        "Spe": int(stats_string.split("Spe: ")[1])
    }


def rebuild_stats_string(poke_stats):
    return (
        f'HP: {poke_stats["HP"]} | '
        f'Atk: {poke_stats["Atk"]} | '
        f'Def: {poke_stats["Def"]} | '
        f'SpA: {poke_stats["SpA"]} | '
        f'SpD: {poke_stats["SpD"]} | '
        f'Spe: {poke_stats["Spe"]}'
    )


def move_stats(move):
    move_stat = {
        "Name": move["name"],
        "Power": move["power"],
        "Accuracy": move["accuracy"],
        "Type": move["type"],
        "Category": move["category"],
        "Effect": move["effect"],
        "Priority": move["priority"]
    }

    return move_stat


def compare_stats(stat, t1pokemon, t2pokemon):
    first_move = ""
    if stat == "Spe":
        t1pokespeed = t1pokemon["Stats"]
        t1speed = int(t1pokespeed.split("Spe: ")[1])

        t2pokespeed = t2pokemon["Stats"]
        t2speed = int(t2pokespeed.split("Spe: ")[1])

        th.subheader("Speed Check")
        th.info(f"{t1pokemon['Name']}: {t1speed}")
        th.info(f"{t2pokemon['Name']}: {t2speed}")

        if t1speed > t2speed:
            first_move = t1pokemon["Name"]
            return first_move
        if t2speed > t1speed:
            first_move = t2pokemon["Name"]
            return first_move
        else:
            random_start = random.randint(1, 2)
            if random_start == 1:
                first_move = t1pokemon["Name"]
                return first_move
            if random_start == 2:
                first_move = t2pokemon["Name"]
                return first_move


def compare_attack(t1Attack, t1pokemon, t2Attack, t2pokemon):
    first_attack = ""
    second_attack = ""

    p1_attack_priority = t1Attack["Priority"]
    p2_attack_priority = t2Attack["Priority"]

    th.subheader("Priority Check")
    th.info(f"{t1pokemon['Name']}: {p1_attack_priority}")
    th.info(f"{t2pokemon['Name']}: {p2_attack_priority}")

    if p1_attack_priority > p2_attack_priority:
        first_attack = t1pokemon["Name"]
        second_attack = t2pokemon["Name"]

    if p2_attack_priority > p1_attack_priority:
        first_attack = t2pokemon["Name"]
        second_attack = t1pokemon["Name"]

    if p1_attack_priority == p2_attack_priority:
        faster_pokemon = compare_stats("Spe", t1pokemon, t2pokemon)
        if faster_pokemon == t1pokemon["Name"]:
            first_attack = t1pokemon["Name"]
            second_attack = t2pokemon["Name"]
        if faster_pokemon == t2pokemon["Name"]:
            first_attack = t2pokemon["Name"]
            second_attack = t1pokemon["Name"]

    th.success(f"Turn Order: {first_attack} -> {second_attack}")

    return first_attack, second_attack


def action(pokemon, trainer):
    th.subheader(f"{trainer['Name']}'s Turn Decision")
    th.info(f"Active Pokemon: {pokemon['Name']}")
    

    moves = pokemon["Moves"]
    move = random.choice(moves)
    move_stat_block = move_stats(move)

    th.print_move_block(move_stat_block)

    decided_action = move_stat_block
    return decided_action


def get_attack_defense(attacker, defender, move):
    attacker = get_poke_stats(attacker)
    defender = get_poke_stats(defender)

    if move["Category"] == "Physical":
        return attacker["Atk"], defender["Def"]
    elif move["Category"] == "Special":
        return attacker["SpA"], defender["SpD"]

    return None, None


def get_stab(move_type, attacker_types):
    return 1.5 if move_type in attacker_types else 1.0


def get_random_modifier():
    return random.randint(217, 255) / 255


def get_type_modifiers(move_type, defender_types):
    type1 = 1.0
    type2 = 1.0

    move_chart = type_chart.get(move_type, {})

    if len(defender_types) >= 1:
        type1 = move_chart.get(defender_types[0], 1.0)

    if len(defender_types) >= 2:
        type2 = move_chart.get(defender_types[1], 1.0)

    return type1, type2


def calculate_damage(attacker, defender, move, critical=False):
    level = 50
    power = move["Power"]

    if power is None or power <= 0:
        return 0

    A, D = get_attack_defense(attacker["Stats"], defender["Stats"], move)

    if A is None or D is None:
        return 0

    crit = 2 if critical else 1
    stab = get_stab(move["Type"], attacker["Type"])
    type1, type2 = get_type_modifiers(move["Type"], defender["Type"])
    rand = get_random_modifier()

    th.subheader("Type Effectiveness")
    th.info(f"Attacker Types: {attacker['Type']} | STAB: {stab}")
    th.info(f"Defender Types: {defender['Type']} | Multiplier: {type1} x {type2}")

    th.print_damage_calc(crit, power, A, D, stab, type1, type2)

    base_damage = (((2 * level * crit / 5 + 2) * power * A / D) / 50) + 2
    damage = int(base_damage * stab * type1 * type2 * rand)

    return max(1, damage) if (type1 * type2) > 0 else 0


def apply_status(user, target, move):
    boosts = move.get("boosts", {})

    if not boosts:
        return

    if move["target"] == "self":
        affected = user
    else:
        affected = target

    th.warning(f"{move['Name']} applies {boosts} to {affected['Name']}")


def execute_move(user, target, move):
    th.header(f"{user['Name']} uses {move['Name']}")

    if move["Category"] in ("Physical", "Special") and move["Power"] > 0:
        damage = calculate_damage(user, target, move)
        th.danger(f"{user['Name']} deals {damage} damage to {target['Name']}")
        return update_stats(target, "HP", True, damage)

    if move["Category"] == "Status":
        apply_status(user, target, move)
        return get_poke_stats(target["Stats"])

    return get_poke_stats(target["Stats"])


def update_stats(pokemon, stat, damage, number):
    poke_stats = get_poke_stats(pokemon["Stats"])
    hp = poke_stats["HP"]
    if stat == "HP":
        if damage:
            hp = hp - number
        if not damage:
            hp = hp + number
        poke_stats["HP"] = hp
        return poke_stats


def battle(trainer1, trainer1_pokemon, trainer2, trainer2_pokemon, mode):

    if mode[-1] == "multiplayer":
        th.header("MULTIPLAYER BATTLE")
        th.info("Battle Starting")

        t1_key = random.choice(list(trainer1_pokemon.keys()))
        t1CurrentPokemon = trainer1_pokemon.pop(t1_key)

        t2_key = random.choice(list(trainer2_pokemon.keys()))
        t2CurrentPokemon = trainer2_pokemon.pop(t2_key)

        th.header("Send Out")
        th.print_pokemon_sendout(trainer1["Name"], t1CurrentPokemon)
        time.sleep(2)
        th.print_pokemon_sendout(trainer2["Name"], t2CurrentPokemon)
        time.sleep(2)

        p1 = get_poke_stats(t1CurrentPokemon["Stats"])
        p2 = get_poke_stats(t2CurrentPokemon["Stats"])

        th.header("Starting HP")
        th.stat_line(t1CurrentPokemon["Name"], p1["HP"])
        time.sleep(2)
        th.stat_line(t2CurrentPokemon["Name"], p2["HP"])
        time.sleep(2)

        while p1["HP"] > 0 and p2["HP"] > 0:
            th.header("NEW TURN")

            p1_chosen_action = action(t1CurrentPokemon, trainer1)
            time.sleep(2)

            p2_chosen_action = action(t2CurrentPokemon, trainer2)
            time.sleep(2)

            order = compare_attack(p1_chosen_action, t1CurrentPokemon, p2_chosen_action, t2CurrentPokemon)
            time.sleep(2)

            if order[0] == t1CurrentPokemon["Name"]:
                p2_turn = execute_move(t1CurrentPokemon, t2CurrentPokemon, p1_chosen_action)
                time.sleep(2)
                
                p2["HP"] = p2_turn["HP"]

                if p2["HP"] < 1:
                    th.header("FAINT CHECK")
                    th.stat_line(t1CurrentPokemon["Name"], p1["HP"])
                    th.stat_line(t2CurrentPokemon["Name"], p2["HP"])
                    time.sleep(2)

                    if not trainer2_pokemon:
                        th.header(f"{trainer1['Name']} WINS")
                        break

                    th.danger(f"{t2CurrentPokemon['Name']} has fainted")
                    time.sleep(2)

                    t2_key = random.choice(list(trainer2_pokemon.keys()))
                    t2CurrentPokemon = trainer2_pokemon.pop(t2_key)
                    p2 = get_poke_stats(t2CurrentPokemon["Stats"])

                    th.header("Replacement")
                    th.print_pokemon_sendout(trainer2["Name"], t2CurrentPokemon)
                    time.sleep(2)

                p1_turn = execute_move(t2CurrentPokemon, t1CurrentPokemon, p2_chosen_action)
                p1["HP"] = p1_turn["HP"]
                time.sleep(2)

                th.header("Current HP")
                th.stat_line(t1CurrentPokemon["Name"], p1["HP"])
                th.stat_line(t2CurrentPokemon["Name"], p2["HP"])

                if p1["HP"] < 1:
                    th.header("FAINT CHECK")
                    if not trainer1_pokemon:
                        th.header(f"{trainer2['Name']} WINS")
                        break

                    th.danger(f"{t1CurrentPokemon['Name']} has fainted")
                    time.sleep(2)

                    t1_key = random.choice(list(trainer1_pokemon.keys()))
                    t1CurrentPokemon = trainer1_pokemon.pop(t1_key)
                    p1 = get_poke_stats(t1CurrentPokemon["Stats"])

                    th.header("Replacement")
                    th.print_pokemon_sendout(trainer1["Name"], t1CurrentPokemon)
                    time.sleep(2)

                t2CurrentPokemon["Stats"] = rebuild_stats_string(p2)
                t1CurrentPokemon["Stats"] = rebuild_stats_string(p1)

            elif order[0] == t2CurrentPokemon["Name"]:
                p1_turn = execute_move(t2CurrentPokemon, t1CurrentPokemon, p2_chosen_action)
                p1["HP"] = p1_turn["HP"]
                time.sleep(2)

                if p1["HP"] < 1:
                    th.header("FAINT CHECK")
                    th.stat_line(t1CurrentPokemon["Name"], p1["HP"])
                    th.stat_line(t2CurrentPokemon["Name"], p2["HP"])

                    if not trainer1_pokemon:
                        th.header(f"{trainer2['Name']} WINS")
                        break

                    th.danger(f"{t1CurrentPokemon['Name']} has fainted")
                    time.sleep(2)

                    t1_key = random.choice(list(trainer1_pokemon.keys()))
                    t1CurrentPokemon = trainer1_pokemon.pop(t1_key)
                    p1 = get_poke_stats(t1CurrentPokemon["Stats"])

                    th.header("Replacement")
                    th.print_pokemon_sendout(trainer1["Name"], t1CurrentPokemon)
                    time.sleep(2)

                p2_turn = execute_move(t1CurrentPokemon, t2CurrentPokemon, p1_chosen_action)
                p2["HP"] = p2_turn["HP"]
                time.sleep(2)

                th.header("Current HP")
                th.stat_line(t1CurrentPokemon["Name"], p1["HP"])
                th.stat_line(t2CurrentPokemon["Name"], p2["HP"])
                time.sleep(2)

                if p2["HP"] < 1:
                    th.header("FAINT CHECK")
                    if not trainer2_pokemon:
                        th.header(f"{trainer1['Name']} WINS")
                        break

                    th.danger(f"{t2CurrentPokemon['Name']} has fainted")
                    time.sleep(2)

                    t2_key = random.choice(list(trainer2_pokemon.keys()))
                    t2CurrentPokemon = trainer2_pokemon.pop(t2_key)
                    p2 = get_poke_stats(t2CurrentPokemon["Stats"])

                    th.header("Replacement")
                    th.print_pokemon_sendout(trainer2["Name"], t2CurrentPokemon)
                    time.sleep(2)

                t2CurrentPokemon["Stats"] = rebuild_stats_string(p2)
                t1CurrentPokemon["Stats"] = rebuild_stats_string(p1)

            time.sleep(2)