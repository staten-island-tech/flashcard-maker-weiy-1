import json

class teacher:
    def teacher_cards():
        doned = False
        madedcards = []
        while doned == False:
            isingthewanting = input("do u are want to do the make card thing (yes or no): ")
            if isingthewanting == "yes":
                wip here
            questioning = input("enter question for a card (if u done, type done): ")
            ansering = input("enter the answer to the question: ")
            if questioning == "done":
                doned = True
                with open("FlashCards.json", "w") as file:
                    json.dump(madedcards, file, indent=4)

            


class spudent:
    def spudent_cards():
        print("testing1")


t_or_s = input("teacher mode or student mode (enter t or s): ")
if t_or_s == "t":
    print("u are now in teacher mode")
    teacher.teacher_cards()

elif t_or_s == "s":
    print("u are now in student mode")
    spudent.spudent_cards()

else:
    print("ur input no working")
    