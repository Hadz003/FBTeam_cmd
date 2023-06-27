from arrays import players
def Average(player):
    return float((player.APT +player.SET)/2)

def calc_average():
    found=False
    find_by_name=input("Enter the first_name of the player: ")
    while not isinstance(find_by_name, str) or find_by_name.isdigit()==True:
        print("Invalid input. Please enter a string.")
        find_by_name=input("Enter the first_name of the player: ")
    find_by_last_name=input("Enter the last_name of the player: ")
    while not isinstance(find_by_last_name, str) or find_by_last_name.isdigit()==True:
        print("Invalid input. Please enter a string.")
        find_by_last_name=input("Enter the last_name of the player: ")
    for i in players:
        if i.first_name==find_by_name  and i.last_name==find_by_last_name :
            found=True
            found_player=i
            break
    if found==True:
        print("\nThe Average of "+find_by_name+" "+find_by_last_name+" is "+str(Average(found_player)))
    else:
        print("player not found")
