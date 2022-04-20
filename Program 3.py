#Author : Theoren Hayne
#Date : 2020-11-23
#Description : This program is a simple but functional version of the game battleship


from string import ascii_uppercase
def Validation(targetChosen, maxWidth, maxHeight): #validation function
    while True: #loops until a real value is chosen
        targetChosen = targetChosen[:1],targetChosen[1:]
        if(targetChosen[1].isdigit() == False):
            pass 
        elif(targetChosen[0] in ascii_uppercase[:maxWidth] and int(targetChosen[1]) <= maxHeight):
            break
        targetChosen = input("Not a real value please enter a position on the map (Ex. B2: ").upper()
    return targetChosen


file = open("map.txt", "r") #reading the map into the "f" array and turing it into the map to be used 
f = file.readlines()
file.close()
battleMap = [line.strip().split(',') for line in f]
currentMap = []

requiredHits = 0 
for lists in battleMap:
    currentMap.append([" " for char in lists])
    requiredHits += lists.count('1')
ammo = 30
print(f"Lets's play Battleship!\n You have {ammo} missiles to sink all five ships!\n")
hits = 0

while True:
    print(" "," ".join(ascii_uppercase[:len(currentMap[0])]))
    for index in range(len(currentMap)):
        print(index+1, *currentMap[index]) 
    userPick = input("\nChoose your target (Ex. A1): ").upper()
    userPick = Validation(userPick, len(currentMap[0]), len(currentMap)) #Validating User Pick
    mapIndex = battleMap[int(userPick[1])-1][ascii_uppercase.index(userPick[0])]
    if(mapIndex == '1'):
        currentMap[int(userPick[1])-1][ascii_uppercase.index(userPick[0])] = "X"
        print('HIT!!!!') #setting the index the user chose on the current map to X
        hits += 1
    elif(mapIndex == '0'): #setting the index the user chose on the current map to O
        currentMap[int(userPick[1])-1][ascii_uppercase.index(userPick[0])] = "O"
        print('Miss') #Miss if they missed the shot
    else:
        print("You already shot a missile at that spot! Try a differnt one.")
        ammo += 1 #everytime the user fires a missile the ammo goes down by 1 but if they misthe board the counter goes back up
    ammo -= 1
    if(ammo == 0):
        print(f"You have {ammo} missiles remaining")
        print(f"GAME OVER.\nYou had {hits} out of {requiredHits} hits, but didn't sink all the ships")
        print("Better luck next time.")
        break #Breaking the while loop ending the game in different ways
    elif(hits >= requiredHits):
        print(f"YOU SANK MY ENTIRE FLEET!\nYou had {hits} out of {requiredHits} hits, which sannk all the ships")
        print("You won, congratulations!")
        break
    print(f"You have {ammo} missiles remaining")
