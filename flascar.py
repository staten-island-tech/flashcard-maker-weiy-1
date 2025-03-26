import json

class teacher:
    def teacher_cards():
        madedcards = {}
        while True:
            isingthewanting = input("do u are want to do the make card thing (yes or no): ")
            if isingthewanting == "yes":
                questioning = input("enter question: ")
                ansering = input("enter the answer to the question: ")
                madedcards[questioning] = ansering
            elif isingthewanting == "no":
                print("ok bye byes u doned")
                with open("FlashCards.json", "w") as file:
                    json.dump(madedcards, file, indent=4)
                break
            else: 
                print("do u are have stoobid")
                break



class spudent:
    def spudent_cards():
        lepoints = 0
        correc_ansereds = 0
        strek = 0
        with open("FlashCards.json", "r") as file:
            spudent_isansering = json.load(file)
        for card in spudent_isansering:
            


t_or_s = input("teacher mode or student mode (enter t or s): ")
if t_or_s == "t":
    print("u are now in teacher mode")
    print("(note: make everything lowercase so that the spudent doesnt inadvertently get it wrong and start questioning themselves)")
    teacher.teacher_cards()

elif t_or_s == "s":
    print("u are now in student mode")
    print("(note: answer everything in lowercase so that u doesnt inadvertently get it wrong cuz it might be big dum about the typography of letters)")
    spudent.spudent_cards()

else:
    print("ur input no working")
    