import start_menu as sm

def select_pokemon():
    print("inside select pokemon")
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
    
    uSelection = input(trainer1["Name"], "Would you like to pick 6 pokemon or have 6 randomly chose for you? (p/r): ")

    