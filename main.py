print("Welcome to the Football Team Program!!\n")
num=1
while num !=0:

    print("\nChoose one of the options below:\n\n1. Create a new player\n2. Get a player's average\n3. Make a team of 10 players\n4. Randomly select players\n5. Count players based on position\n6. Sort all players by APT from high to low\n7. Find the player with the highest APT score\n8. Find the player with lowest AVG score\n\nPress 0 to exit the program ")
    while True:
        try:
            num=int(input("Enter a number: "))    
            break  # Break out of the loop if an integer value is entered
        except ValueError:
            print("Invalid input. Please enter an integer.")
    print("\n")
    if num==1:
        from create_player import new_player
        new_player()

    elif num==2:
        from average import calc_average
        calc_average()

    elif num==3:
       from make_team import team_select
       team_select()
    elif num==4:
        from random_select import rand_select
        rand_select()
    elif num==5:
        from count import pos_count
        pos_count()
    elif num==6:
        from sort_apt import APT_sort
        APT_sort()
    elif num==7:
        from highest_apt import highest_APT
        highest_APT()
    elif num==8:
        from lowest_avg import lowest_AVG
        lowest_AVG()
print("GoodBye!")

