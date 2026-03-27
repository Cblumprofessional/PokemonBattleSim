# =========================
# TERMINAL STYLE HELPERS
# =========================
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"


def header(text):
    print(f"\n{C.BOLD}{C.CYAN}{'=' * 18} {text} {'=' * 18}{C.RESET}")


def subheader(text):
    print(f"{C.BOLD}{C.YELLOW}-- {text} --{C.RESET}")


def info(text):
    print(f"{C.WHITE}{text}{C.RESET}")


def success(text):
    print(f"{C.GREEN}{text}{C.RESET}")


def warning(text):
    print(f"{C.YELLOW}{text}{C.RESET}")


def danger(text):
    print(f"{C.RED}{text}{C.RESET}")


def stat_line(name, hp):
    color = C.GREEN if hp > 50 else C.YELLOW if hp > 20 else C.RED
    print(f"{C.BOLD}{name}{C.RESET} HP: {color}{hp}{C.RESET}")


def print_move_block(move_stat_block):
    subheader("Move Chosen")
    print(f"  {C.BOLD}{move_stat_block['Name']}{C.RESET}")
    print(
        f"  Type: {C.BLUE}{move_stat_block['Type']}{C.RESET} | "
        f"Category: {C.MAGENTA}{move_stat_block['Category']}{C.RESET}"
    )
    print(
        f"  Power: {move_stat_block['Power']} | "
        f"Accuracy: {move_stat_block['Accuracy']} | "
        f"Priority: {move_stat_block['Priority']}"
    )
    print(f"  Effect: {C.DIM}{move_stat_block['Effect']}{C.RESET}\n")


def print_pokemon_sendout(trainer_name, pokemon):
    print(
        f"{C.BOLD}{trainer_name}{C.RESET} sends out "
        f"{C.GREEN}{pokemon['Name']}{C.RESET}"
    )
    print(f"  {pokemon['Stats']}")


def print_damage_calc(crit, power, A, D, stab, type1, type2):
    subheader("Damage Calculation")
    print(f"  Crit: {crit}")
    print(f"  Power: {power}")
    print(f"  A: {A} | D: {D}")
    print(f"  STAB: {stab}")
    print(f"  Type Multiplier: {type1} x {type2}")