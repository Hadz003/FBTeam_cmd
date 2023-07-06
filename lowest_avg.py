from arrays import (players)
from average import Average
def lowest_AVG():
    counter=100
    found="None"
    for i in range(len(players)):
        if Average(players[i])<counter:
            counter=Average(players[i])
            found=str(players[i])
    print (found)