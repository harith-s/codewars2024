
import math
import time
import numpy as np
from numpy import random

name = 'byte brawlers'

def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    pos = pirate.getPosition()
    s = pirate.trackPlayers()

    if (
        (up == "island1" and s[0] != "myCaptured")
        or (up == "island2" and s[1] != "myCaptured")
        or (up == "island3" and s[2] != "myCaptured")
    ): 
        island_coords = (pos[0], pos[1]-1)
        # island_pos[int(up[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{up[-1]},{pos[0]},{pos[1]-1}")
        return True
        
    elif (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ): 
        island_coords = (pos[0], pos[1]+1)
        # island_pos[int(down[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{down[-1]},{pos[0]},{pos[1]+1}")
        return True
    
    elif (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        island_coords = (pos[0] - 1, pos[1])
        # island_pos[int(left[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{left[-1]},{pos[0]-1},{pos[1]}")
        return True
    
    elif (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ): 
        island_coords = (pos[0] + 1, pos[1])
        # island_pos[int(right[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{right[-1]},{pos[0]+1},{pos[1]}")
        return True
    
    else:
        return False

def moveTo(x, y, Pirate):
    position = Pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] < y) * 2 + 1
    if position[1] == y:
        return (position[0] > x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

def spread(pirate):
    sw = checkfriends(pirate ,'sw' )
    se = checkfriends(pirate ,'se' )
    ne = checkfriends(pirate ,'ne' )
    nw = checkfriends(pirate ,'nw' )
   
    my_dict = {'sw': sw, 'se': se, 'ne': ne, 'nw': nw}
    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

    x, y = pirate.getPosition()
    
    if( x == 0 , y == 0):
        return random.randint(1,4)
    
    if(sorted_dict[list(sorted_dict())[3]] == 0 ):
        return random.randint(1,4)
    
    if(list(sorted_dict())[0] == 'sw'):
        return moveTo(x-1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'se'):
        return moveTo(x+1 , y+1 , pirate)
    elif(list(sorted_dict())[0] == 'ne'):
        return moveTo(x+1 , y-1 , pirate)
    elif(list(sorted_dict())[0] == 'nw'):
        return moveTo(x-1 , y-1 , pirate)


def check_initial_quad(pirate):
    posx, posy = pirate.getDeployPoint()
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    if posx <= X//2:
        if posy <=Y//2:
            pirate.setSignal(f"i-{(X//4,Y//4)}-{(X//4,3*Y//4)}-{(3*X//4,Y//4)}")
        else:
            pirate.setSignal(f"i-{(X//4,3*Y//4)}-{(X//4,Y//4)}-{(X//4,3*Y//4)}")
    else:
        if posy <= Y//2:
            pirate.setSignal(f"i-{(3*X//4,Y//4)}-{(X//4,Y//4)}-{(X//4,3*Y//4)}")
        else:
            pirate.setSignal(f"i-{(3*X//4,3*Y//4)}-{(X//4,3*Y//4)}-{(3*X//4,Y//4)}")
    moveTo_from_initial_pos(pirate)
        
def random_walk():
    return random.randint(1,4)

def island_status():
    pass

def moveTo_from_initial_pos(pirate):
    # ask if all pirates spawn in same location
    key = random.randint(1,3)
    signal = (pirate.getSignal()).split('-')

    if key ==1:
        pirate.setSignal(f'i-{signal[1]}')
    elif key ==2:
        pirate.setSignal(f'i-{signal[2]}')
    else:
        pirate.setSignal(f'i-{signal[3]}')
def checkfriends(pirate , quad ):
    sum = 0 
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]
    ne = pirate.investigate_ne()[1]
    nw = pirate.investigate_nw()[1]
    se = pirate.investigate_se()[1]
    sw = pirate.investigate_sw()[1]
    
    if(quad=='ne'):
        if(up == 'friend'):
            sum +=1 
        if(ne== 'friend'):
            sum +=1 
        if(right == 'friend'):
            sum +=1 
    if(quad=='se'):
        if(down == 'friend'):
            sum +=1 
        if(right== 'friend'):
            sum +=1 
        if(se == 'friend'):
            sum +=1 
    if(quad=='sw'):
        if(down == 'friend'):
            sum +=1 
        if(sw== 'friend'): 
            sum +=1 
        if(left == 'friend'):
            sum +=1 
    if(quad=='nw'):
        if(up == 'friend'):
            sum +=1 
        if(nw == 'friend'):
            sum +=1 
        if(left == 'friend'):
            sum +=1 

    return sum


def ActPirate(pirate):
    signal = pirate.getSignal()
    checkIsland(pirate)
    if signal == '':
        check_initial_quad(pirate)
        return 0
    elif signal.startswith('i'):
        return assigned_pos(pirate)
        print("reached assigned pirates return")
    if signal.startswith('e'):
        return random_walk()
        print("reached explorer pirates return")
    elif signal.startswith('c'):
        if pirate.getTeamSignal() == '':
            return random_walk()
            print("reached capturer pirates return")
        else:
            temp = pirate.getTeamSignal().split(',')
        s = pirate.trackPlayers()
        if s[int(temp[0][-1])-1] == 'myCaptured':
            pirate.setTeamSignal('')
        move = moveTo(int(temp[1]),int(temp[2]),pirate)
        if move != 0:
            return move

    
    
    


def ActTeam(team):
    list1 = team.getListOfSignals()
    time = team.getCurrentFrame()
    # print(time, list1)
# quadrants
# random walk
# flags
# islands status
# move to some particular set amount of pirates


def assigned_pos(pirate):
    signal = pirate.getSignal()
    temp = [int(i) for i in (signal.split('-'))[1].strip('()').split(",")]
    if moveTo(temp[0], temp[1], pirate) != 0:
        # print(temp[0], temp[1])
        return moveTo(temp[0], temp[1], pirate)
        
    else:
        if random.choice(['e','c'], p = [0.7, 0.3], size = (1))[0] == 'e':
            pirate.setSignal('e')
        else:
            pirate.setSignal('c')
        return 0
    
