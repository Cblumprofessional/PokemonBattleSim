

def trainer_base():
    print("Create a Trainer\n=================")
    completed_trainer = {
    "Name" : "",
    "Gender": "",
    "Battle Style": ""
    }
    uGender = ""
    uYesNo = ""
    uBattleStyle = ""
    gender_options = ["boy", "girl", "b", "g"]
    yes_no = ["yes", "no", "y", "n"]
    battle_styles = {
        "Aggressive": "You rarely use items and prioritize damage output",
        "Balanced": "You balance using items and damage output",
        "Conservative": "You priortize keeping your pokemon alive"
                     
    }
    
    while(uGender.lower() not in gender_options):
        uGender = input("Are you a boy or a girl: ")
        if(uGender.lower() not in gender_options):
            print("Options are boy, girl, b, g")
            
    uName = input("Enter your name: ")
    print("Your name is " + uName + ". Is that Correct?")
    while(uYesNo not in yes_no and uYesNo != "yes" or uYesNo != "y"):
        uYesNo = input("Yes/No: ")
        if(uYesNo == "no" or uYesNo == "n"):
            uName = input("Enter your name: ")
        if(uYesNo not in yes_no):
            print("Options are yes, no, y, n")
    
    for key, value in battle_styles.items():
        print(f"{key} : {value}")        
    while(uBattleStyle not in battle_styles):        
        uBattleStyle = input("Enter your battle style: ")
        if uBattleStyle not in battle_styles:
            print("Choice not a battle style")
            
    completed_trainer.update({"Name": uName, "Gender": uGender, "Battle Style": uBattleStyle})
    

    return completed_trainer