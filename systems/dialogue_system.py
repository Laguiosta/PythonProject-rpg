import os

# History Function

def game_history(history):
    def skip_history_function():
        skip_history = False
        while skip_history != True:
            user_choice_skip = input("Press Enter to continue ")
            if user_choice_skip == "":
                skip_history = True

    history1 = (
        "\nAn adventurer left the house he inherited from his missing father, "
        "leaving his mother to take care of it as he set out to explore the world.\n"
    )

    mother_history = '''
Mother:
“So… the day has finally come for you to leave.”
She tries to smile, but her eyes reveal the fear of someone who has already lost someone once.

You:
“I have to find out what happened to Dad. And I want to see the world outside.”

Mother:
“Your father said the exact same thing…”
'''

    tutorial_combat = '''
As soon as he left home and followed the old trail, the young adventurer heard quick scratches nearby. 
From behind broken crates, giant rats appeared, hissing and ready to attack.

It wasn’t a great danger — just a first test. The journey had truly begun.
'''

    history2 = "\nSun, the darkness takes me. I believe in you; one day, you will follow my path — the volc...\n"
    history3 = "\nThe father returned to normal, the world’s corruption vanished, and the young explorer returned home.\n"

    if history == 1:
        os.system("cls")
        print(history1)
        skip_history_function()
    elif history == 1.1:
        os.system("cls")
        print(mother_history)
        skip_history_function()
    elif history == 1.2:
        os.system("cls")
        print(tutorial_combat)
        skip_history_function()
    elif history == 2:
        os.system("cls")
        print(history2)
        skip_history_function()
    elif history == 3:
        os.system("cls")
        print(history3)
        skip_history_function()
    else:
        print("Error! Verify history variables.")
