from arrays import (players,Defenders,Attackers,Midfielders)
i_d=1
class player(object):
    def __init__ (self,ID,first_name,last_name,APT,SET,nationality,position):
        self.first_name=first_name
        self.last_name=last_name
        self.APT=APT
        self.SET=SET
        self.position=position
        self.nationality=nationality
        self.ID=ID
    def __str__(self):
        return str(self.ID) + " " + self.first_name + " " + self.last_name + " " + str(self.APT) + " " + str(self.SET) + " " + self.nationality + " "  + self.position
    
def new_player():
    global i_d
    first_name = input("Enter the player's first name: ")
    while not isinstance(first_name, str) or first_name.isdigit()==True:
        print("Invalid input. Please enter a string.")
        first_name = input("Enter the player's first name: ")

    last_name=input("Enter the player's last name: ")
    while not isinstance(last_name, str) or last_name.isdigit()==True:
        print("Invalid input. Please enter a string.")
        last_name=input("Enter the player's last name: ")

    while True:
        try:
            apt = int(input("Enter the player's APT: "))
            if apt>100 or apt<0 :
                continue
            break  # Break out of the loop if an integer value is entered
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            set=int(input("Enter the player's SET: "))
            if set>100 or set<0 :
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    na=input("Enter the player's Nationality: ")
    while not isinstance(na, str):
        print("Invalid input. Please enter a string.")
        na=input("Enter the player's Nationality: ")
    while True:
        if na=="Scotland":
            break
        elif na=="England":
            break
        elif na=="Northern Ireland":
            break
        elif na=="Wales":
            break
        else:
            print("Invalid Country")
            na=input("Enter the player's Nationality: ")

    Position=input("Enter the player's position: ")
    while not isinstance(Position, str):
        print("Invalid input. Please enter a string.")
        Position=input("Enter the player's position: ")
    while True:
        if Position=="Defender":
            break
        elif Position=="Midfielder":
            break
        elif Position=="Attacker":
            break
        else:
            print("Invalid position")
            Position=input("Enter the player's position: ")
    

    x=player(i_d,first_name,last_name,apt,set,na,Position)

    if x.position=="Defender":
        Defenders.append(x)
        Defenders.sort(key= lambda player: player.SET, reverse=True)
    elif x.position=="Midfielder":
        Midfielders.append(x)
        Midfielders.sort(key= lambda player: player.SET, reverse=True)
    else :
        Attackers.append(x)
        Attackers.sort(key= lambda player: player.SET, reverse=True)

    players.append(player(i_d,first_name,last_name,apt,set,na,Position))
    i_d=i_d + 1