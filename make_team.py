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

        sorted_defence=sorted( Defenders, key=lambda player: player.SET, reverse=True)
        sorted_mid=sorted( Midfielders, key=lambda player: player.SET, reverse=True)
        sorted_attack=sorted( Attackers, key=lambda player: player.SET, reverse=True)


        for i in range(num_of_def):
            print(sorted_defence[i])
        for i in range(num_of_mid):
            print(sorted_mid[i])
        for i in range(num_of_attack):
            print(sorted_attack[i])
        