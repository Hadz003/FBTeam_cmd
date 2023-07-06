from arrays import (players)
def rand_select():
    check=True
    while check==True:
        while True:
            try:
                rand_num=int(input("Enter the number of players required: "))
                break
            except:
                print("Invalid input. Please enter an integer.")

        if rand_num>len(players):
            print("Not enough players available, thereare only "+str(len(players))+" players")
            continue
        elif rand_num<0:
            print("Very few players!")
            continue
        check=False
        import random
        rand_list=random.sample(players,rand_num)

        for i in rand_list:
            print(i)