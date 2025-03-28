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
        total = 0
        with open("FlashCards.json", "r") as file:
            spudent_isansering = json.load(file)
        for card in spudent_isansering:
            spudentresponse = input(f'{card}')
            if spudentresponse == spudent_isansering[card]:
                lepoints = lepoints + 1
                strek = strek + 1
                correc_ansereds = correc_ansereds + 1
                total = total + 1
                print("big smar u got corret")
                print(f"points: {lepoints}, corret answers/total: {correc_ansereds}/{total}, ur streak: {strek}")
                if strek == 3:
                    lepoints = lepoints + 3
                    print(f"wow u streak is {strek}, u get bognus 3 point (current points: {lepoints})")
                if strek == 7:
                    lepoints = lepoints + 5
                    print(f"wow u streek is {strek}, u get bognus 5 point (current points: {lepoints})")

            else:
                print("o teh noes u got it rong (u strek get backed to zeero.)")
                strek = 0
                total = total + 1



t_or_s = input("teacher mode or student mode (enter t or s): ")

if t_or_s == "t":
    print("u are now in teacher mode")
    print("(note: make all answers lowercase and at end of question type '? ')")
    teacher.teacher_cards()

elif t_or_s == "s":
    print("u are now in student mode. each correct answer is 1 point. u will get bongus points for streak.")
    print("(note: answer everything in lowercase)")
    spudent.spudent_cards()

else:
    print("ur input no working")