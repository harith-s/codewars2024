import random 
import math
import time

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
        island_pos[int(up[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{up[-1]},{pos[0]},{pos[1]}")
        return True
        
    elif (
        (down == "island1" and s[0] != "myCaptured")
        or (down == "island2" and s[1] != "myCaptured")
        or (down == "island3" and s[2] != "myCaptured")
    ): 
        island_coords = (pos[0], pos[1]+1)
        island_pos[int(down[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{down[-1]},{pos[0]},{pos[1]}")
        return True
    
    elif (
        (left == "island1" and s[0] != "myCaptured")
        or (left == "island2" and s[1] != "myCaptured")
        or (left == "island3" and s[2] != "myCaptured")
    ):
        island_coords = (pos[0] - 1, pos[1])
        island_pos[int(left[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{left[-1]},{pos[0]},{pos[1]}")
        return True
    
    elif (
        (right == "island1" and s[0] != "myCaptured")
        or (right == "island2" and s[1] != "myCaptured")
        or (right == "island3" and s[2] != "myCaptured")
    ): 
        island_coords = (pos[0] + 1, pos[1])
        island_pos[int(right[-1]) - 1] = island_coords
        pirate.setTeamSignal(f"{right[-1]},{pos[0]},{pos[1]}")
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

def randomwalk():
    return random.randint(1,4)

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
    key = random.randint(1,10)
    signal = (pirate.getSignal()).split('-')

    if key <= 6:
        pirate.setSignal(f'i-{signal[1]}')
    elif key <= 8:
        pirate.setSignal(f'i-{signal[2]}')
    else:
        pirate.setSignal(f'i-{signal[3]}')



def ActPirate(pirate):
    if (pirate.getCurrentFrame() == 1):
        global island_pos
        island_pos = [-1,-1,-1]
        check_initial_quad(pirate)
    signal = pirate.getSignal()
    if signal[0] == 'i':
        temp = [int(i) for i in (signal.split('-'))[1].strip('()').split(",")]
        if moveTo(temp[0], temp[1]) == 0:
            pirate.setSignal('r')
        return moveTo(temp[0], temp[1])
    
    # check if there is no signal
    # if yes do random walk
    if pirate.getTeamSignal() == '':
        return random_walk()
    else:
        temp = pirate.getTeamSignal().split(',')
        return moveTo(temp[1],temp[2])
    


def ActTeam(team):
    pass

# quadrants
# random walk
# flags
# islands status
# move to some particular set amount of pirates