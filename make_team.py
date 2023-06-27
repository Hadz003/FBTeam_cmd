from arrays import (players,Defenders,Attackers,Midfielders)
def team_select():
    check=True
    if len(players)<10:
        print("Not enough players available, please input more players to build a team")
        check=False
    while check==True:
        while True:
            try:
                num_of_def=int(input("Enter the number of defenders: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                num_of_mid=int(input("Enter the number of midfielders: "))
                break
            except:
                print("Invalid input. Please enter an integer.")
        while True:
            try:
                num_of_attack=int(input("Enter the number of attackers: "))
                break
            except:
                print("Invalid input. Please enter an integer.")
        if (num_of_attack + num_of_def + num_of_mid)!=10:
            print("not 10 players")
            continue

        if num_of_def>len(Defenders):
            print("Not enough defenders available")
            continue
        if num_of_mid>len(Midfielders):
            print("Not enough midfielders available")
            continue
        if num_of_attack>len(Attackers):
            print("Not enough attackers available")
            continue
        check=False
        #print("ID First Name Last Name APT SET Nationality Position")
        for i in range(num_of_def):
            print(Defenders[i])
        for i in range(num_of_mid):
            print(Midfielders[i])
        for i in range(num_of_attack):
            print(Attackers[i])