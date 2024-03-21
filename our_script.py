import random
import math
import time
import numpy as np
from numpy import random as rd

name = 'byte brawlers'
def lazy(dir1, dir2, coord):
    if 'island' in dir1 and "island" in dir2:
        result = coord
    elif 'island' in dir1 :
        result = coord + 1
    else:
        result = coord - 1
    return result

#checks if there == an island within the pirate's vicinity and retuens true/false and updates team signal
def new_checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw=pirate.investigate_nw()[0]
    ne=pirate.investigate_ne()[0]
    sw=pirate.investigate_sw()[0]
    se=pirate.investigate_se()[0]
    pos = pirate.getPosition()
    s = pirate.trackPlayers()
    # a=[int(i) for i in pirate.getTeamSignal().split("_")]
    # if(s[-1] != -1 or s[-2] != -1 or s[-3] != -1 or s[-4] != -1 or s[-5] != -1 or s[-6] != -1):
    #     if up == 'island1':    
    #         if (right != 'island1' or left != 'island1'):
    #             x = lazy(nw, ne, pos[0])
    #             # returns the center of the island
    #             team_signal_update(pirate,x1=x, y1 = pos[1]-2)
    #             return True
    #         elif (right == 'island1'):
    #             team_signal_update(pirate,x1=pos[0]+1, y1 = pos[1]-1)
    #             return True
    #         elif (left == 'island1'):
    #             team_signal_update(pirate,x1=pos[0]-1, y1 = pos[1]-1)
    #             return True
            

    #     if up == 'island2': 
    #         if(right != 'island2' or left != 'island2'):
    #             x = lazy(nw, ne, pos[0])
    #             team_signal_update(pirate,x2=x,y2=pos[1]-2)
    #             return True
    #         elif (right == 'island2'):
    #             team_signal_update(pirate,x1=pos[0]+1, y1 = pos[1]-1)
    #             return True
    #         elif (left == 'island3'):
    #             team_signal_update(pirate,x1=pos[0]-1, y1 = pos[1]-1)
    #             return True
            
    #     if up == 'island3': 
    #         if (right != 'island3' or left != 'island3'):
    #             x = lazy(nw, ne, pos[0])
    #             team_signal_update(pirate,x3=x,y3=pos[1]-2)
    #             return True
    #         elif (right == 'island3'):
    #             team_signal_update(pirate,x1=pos[0]+1, y1 = pos[1]-1)
    #             return True
    #         elif (left == 'island3'):
    #             team_signal_update(pirate,x1=pos[0]-1, y1 = pos[1]-1)
    #             return True
            
    #     if right == 'island1':
    #         if (down != 'island1' or up !='island1'):
    #             y = lazy(se, ne, pos[1])
    #             team_signal_update(pirate,x1=pos[0]+2,y1=y)
    #             return True
    #         elif (down == 'island1'):
    #             team_signal_update(pirate,x1=pos[0]+1,y1=pos[1]+1)
    #             return True
    #         elif (up == 'island1'):
    #             team_signal_update(pirate,x1=pos[0]+1,y1=pos[1]-1)
    #             return True
            
    #     if right == 'island2':
    #         if (down != 'island2' or up !='island2'):
    #             x = lazy(se, ne, pos[1])
    #             team_signal_update(pirate,x2=pos[0]+2,y2=pos[1])
    #             return True
    #         elif (down == 'island2'):
    #             team_signal_update(pirate,x1=pos[0]+1,y1=pos[1]+1)
    #             return True
    #         elif (up == 'island2'):
    #             team_signal_update(pirate,x1=pos[0]+1,y1=pos[1]-1)
    #             return True

    #     if right == 'island3':    
    #         if (down != 'island3' or up !='island3'):
    #             x = lazy(se, ne, pos[1])
    #             team_signal_update(pirate,x3=pos[0]+2,y3=pos[1])
    #             return True
    #         elif (down == 'island3'):
    #             team_signal_update(pirate,x1=pos[0]+1,y1=pos[1]+1)
    #             return True
    #         elif (up == 'island3'):
    #             team_signal_update(pirate,x1=pos[0]+1,y1=pos[1]-1)
    #             return True
            
    #         if(left == "island1"):
    #             team_signal_update(pirate,x1=pos[0]-1,y1=pos[1])
    #             return True
    #         if(left == "island2"):
    #             team_signal_update(pirate,x2=pos[0]-1,y2=pos[1])
    #             return True
    #         if(left == "island3"):
    #             team_signal_update(pirate,x3=pos[0]-1,y3=pos[1])
    #             return True
            
    #         if(down == "island1"):
    #             team_signal_update(pirate,x1=pos[0],y1=pos[1]+1)
    #             return True
    #         if(down == "island2"):
    #             team_signal_update(pirate,x2=pos[0],y2=pos[1]+1)
    #             return True
    #         if(down == "island3"):
    #             team_signal_update(pirate,x3=pos[0],y3=pos[1]+1)
    #             return True
    # return False
    
def checkIsland(pirate):
    up = pirate.investigate_up()[0]
    down = pirate.investigate_down()[0]
    left = pirate.investigate_left()[0]
    right = pirate.investigate_right()[0]
    nw=pirate.investigate_nw()[0]
    ne=pirate.investigate_ne()[0]
    sw=pirate.investigate_sw()[0]
    se=pirate.investigate_se()[0]
    pos = pirate.getPosition()
    s = pirate.trackPlayers()
    a=[int(i) for i in pirate.getTeamSignal().split("_")]
 
    if(s[-1] != -1 or s[-2] != -1 or s[-3] != -1 or s[-4] != -1 or s[-5] != -1 or s[-6] != -1):
            if(up == "island1"):
                team_signal_update(pirate,x1=pos[0],y1=pos[1]-1)
                return True
            if(up == "island2"):
                team_signal_update(pirate,x2=pos[0],y2=pos[1]-1)
                return True
            if(up == "island3"):
                team_signal_update(pirate,x3=pos[0],y3=pos[1]-1)
                return True
            
            if(right == "island1"):
                team_signal_update(pirate,x1=pos[0]+1,y1=pos[1])
                return True
            if(right == "island2"):
                team_signal_update(pirate,x2=pos[0]+1,y2=pos[1])
                return True
            if(right == "island3"):
                team_signal_update(pirate,x3=pos[0]+1,y3=pos[1])
                return True
            if(left == "island1"):
                team_signal_update(pirate,x1=pos[0]-1,y1=pos[1])
                return True
            if(left == "island2"):
                team_signal_update(pirate,x2=pos[0]-1,y2=pos[1])
                return True
            if(left == "island3"):
                team_signal_update(pirate,x3=pos[0]-1,y3=pos[1])
                return True
            
            if(down == "island1"):
                team_signal_update(pirate,x1=pos[0],y1=pos[1]+1)
                return True
            if(down == "island2"):
                team_signal_update(pirate,x2=pos[0],y2=pos[1]+1)
                return True
            if(down == "island3"):
                team_signal_update(pirate,x3=pos[0],y3=pos[1]+1)
                return True
    return False


#moves a pirate to a particular position
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

#moves while avoiding enemy contact
def moveTo_safe(x, y, pirate):
    position = pirate.getPosition()
    up = pirate.investigate_up()[1]
    down = pirate.investigate_down()[1]
    left = pirate.investigate_left()[1]
    right = pirate.investigate_right()[1]

    if(up == "enemy"):
        return 1
    elif(down == "enemy"):
        return 3
    elif(right == "enemy"):
        return 2
    elif(left == "enemy"):
        return 4
    elif position[0] == x and position[1] == y:
        return 0
    elif position[0] == x:
        return (position[1] < y) * 2 + 1
    elif position[1] == y:
        return (position[0] > x) * 2 + 2
    elif random.randint(1, 2) == 1:
        return (position[0] > x) * 2 + 2
    else:
        return (position[1] < y) * 2 + 1

#initial spread function
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

#checks the number of friends nearby
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
            pirate.setSignal(f"i-{(3*X//4,Y//4)}-{(X//4,Y//4)}-{(3*X//4,3*Y//4)}")
        else:
            pirate.setSignal(f"i-{(3*X//4,3*Y//4)}-{(X//4,3*Y//4)}-{(3*X//4,Y//4)}")
    moveTo_from_initial_pos(pirate)
        
def random_walk():
    return random.randint(1,4)

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

def team_signal_update(pirate,p1=-1,p2=-1,p3=-1,x1=-1,y1=-1,x2=-1,y2=-1,x3=-1,y3=-1):    
    
    a=[int(i) for i in pirate.getTeamSignal().split("_")]

    if(p1 != -1):
        a[0]=p1
    if(p2 != -1):
        a[1]=p2
    if(p3 != -1):
        a[2]=p3
    if(x1 != -1):
        a[3]=x1
    if(y1 != -1):
        a[4]=y1
    if(x2 != -1):
        a[5]=x2
    if(y2 != -1):
        a[6]=y2
    if(x3 != -1):
        a[7]=x3
    if(y3 != -1):
        a[8]=y3
    b=""
    for i in range(len(a)-1):
        b+=str(a[i])+"_"
    b+=str(a[8])
    pirate.setTeamSignal(b)

# def pirate_signal_update(pirate,x,y,destination):
#     pos=pirate.getPosition()
#     if(pirate.getCurrentFrame()==1):
#         pirate.setSignal(pos[0]+""+pos[1]+"-1_-1")
#     if()
#     pirate.setSignal(pos[0]+""+pos[1]+"-1_-1")
def assigned_pos(pirate):
    signal = pirate.getSignal()
    temp = [int(i) for i in (signal.split('-'))[1].strip('()').split(",")]
    if moveTo_safe(temp[0], temp[1], pirate) != 0:
        # print(temp[0], temp[1])
        return moveTo_safe(temp[0], temp[1], pirate)
        
    else:
        # if rd.choice(['e','c'], p = [0.7, 0.3], size = (1))[0] == 'e':
        #     pirate.setSignal('e')
        # else:
        #     assignRole(pirate)
        # return 0
        id = int(pirate.getID())
        if id < 11 or 20<=id<=30 or 40<= id <= 50 or 60<= id <= 70 or 83<= id:
            pirate.setSignal('e')
        elif 11<= id <=19 or 31 <= id <= 39 or 51 <= id <=59 or 71<= id <= 82:
            if id % 3 == 0:
                pirate.setSignal("c island1")
            if id % 3 == 1:
                pirate.setSignal("c island2")
            if id % 3 == 2:
                pirate.setSignal("c island3")
    
def new_(pirate):
    id = pirate.getID()
    X = pirate.getDimensionX()
    Y = pirate.getDimensionY()
    posx, posy = pirate.getDeployPoint()
    signal = pirate.getSignal()
    q = (0,0)
    if posx <= X//2:
        if posy <=Y//2:
            q = (X//4, Y//4)
        else:
            q  = (X//4,3*Y//4)
    else:
        if posy <= Y//2:
            q = (3*X//4,Y//4)
        else:
            q = (3*X//4,3*Y//4)
    if signal == '':
        if int(id) < 21:
            if moveTo(q[0], q[1],pirate) == 0:
                pirate.setSignal("random")
            return moveTo(q[0], q[1],pirate)
        elif int(id) < 41:
            if moveTo(q[0], q[1],pirate) == 0:
                pirate.setSignal("random")
            return moveTo(((q[0]+X//2)%X), ((q[1]+Y//2)%Y), pirate)
        elif int(id) < 61:
            if moveTo(q[0], q[1],pirate) == 0:
                pirate.setSignal("random")
            return moveTo(abs((q[0]-X//2))%X, abs((q[1]-Y//2))%Y,pirate)
        else:
            return random_walk()
    else:
        return random_walk()

def configuration(pirate):
    pirate.getSignal()

def moveAway(x,y,pirate):
    position = pirate.getPosition()
    if position[0] == x and position[1] == y:
        return 0
    if position[0] == x:
        return (position[1] > y) * 2 + 1
    if position[1] == y:
        return (position[0] < x) * 2 + 2
    if random.randint(1, 2) == 1:
        return (position[0] < x) * 2 + 2
    else:
        return (position[1] > y) * 2 + 1

def circleAround(x, y, radius, Pirate, initial, clockwise=True):
    position = Pirate.getPosition()
    rx = position[0]
    ry = position[1]
    pos = [[x + i, y + radius] for i in range(-1 * radius, radius + 1)]
    pos.extend([[x + radius, y + i] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x + i, y - radius] for i in range(radius - 1, -1 * radius - 1, -1)])
    pos.extend([[x - radius, y + i] for i in range(-1 * radius + 1, radius)])
    if [rx, ry] not in pos:
        if initial != (x + radius, y):
            return moveTo(x + radius, y, Pirate)
        if rx in [x + i for i in range(-1 * radius, radius + 1)] and ry in [
            y + i for i in range(-1 * radius, radius + 1)
        ]:
            return moveAway(x, y, Pirate)
        else:
            return moveTo(x, y, Pirate)
    else:
        index = pos.index([rx, ry])
        return moveTo(
            pos[(index + (clockwise * 2) - 1) % len(pos)][0],
            pos[(index + (clockwise * 2) - 1) % len(pos)][1],
            Pirate)

def no_of_pirates_to_island(team): #just in case any pirate dies
    a=team.getListOfSignals()
    i1=0
    i2=0
    i3=0 
    if team.getCurrentFrame() == 1:
        return None
    for i in range(len(a)):
        if a[i].startswith('c'):
            if(a[i].split()[1] == "island1"):
                # a[i] += " "+str(i1)
                i1+=1
            if(a[i].split()[1] == "island2"):
                # a[i]+=" "+str(i2)
                i2+=1
            if(a[i].split()[1] == "island2"):
                # a[i]+=" "+str(i3)
                i3+=1
    # if(team.getCurentFrame() == 1):
    #     team.setTeamSignal("-1_-1_-1_-1_-1_-1_-1_-1_-1")
    a = [int(i) for i in team.getTeamSignal().split("_")]

    if(i1 != 0):
        a[0]=i1
    if(i2 != 0):
        a[1]=i2
    if(i3 != 0):
        a[2]=i3
    b=""
    for i in range(len(a)-1):
        b+=str(a[i])+"_"
    b+=str(a[8])
    team.setTeamSignal(b)

def assignRole(pirate): #assign roles to pirates
    a=[int(i) for i in pirate.getTeamSignal().split("_")]
    if(a[0] < 13):
        pirate.setSignal("c island1 "+ str(a[0]))
        return 0
    if(a[1] < 13):
        pirate.setSignal("c island2 "+ str(a[1]))
        return 0
    if(a[2] < 13):
        pirate.setSignal("c island3 "+ str(a[2]))   
        return 0
    
def ActPirate(pirate):
    if(pirate.getCurrentFrame() == 1):
        pirate.setTeamSignal("-1_-1_-1_-1_-1_-1_-1_-1_-1")
    signal = pirate.getSignal()
    island_status = pirate.trackPlayers()
    checkIsland(pirate)
    if signal == '':
        check_initial_quad(pirate)
        return 0
    elif signal.startswith('i'):
        return assigned_pos(pirate)
    if signal.startswith('e'):
        return random_walk()
    elif signal.startswith('c'):
        # p1=-1 , p2=-1 ,p3=-1 ,x1=-1 ,y1=-1 ,x2=-1, y2=-1, x3=-1, y3=-1
        t_signal = [int(i) for i in pirate.getTeamSignal().split('_')]
        print(t_signal)
        island = signal.split()[1]

        if island == 'island1':
            if t_signal[3] == -1 or island_status[int(island[-1])-1] == 'myCaptured':
                return random_walk()
            elif island_status[int(island[-1])-1] in ['myCapturing', '']:
                move = moveTo_safe(t_signal[3], t_signal[4],pirate)
                if move == 0:
                    return 1
                return move
        
        elif island == 'island2':
            if t_signal[5] == -1 or island_status[int(island[-1])-1] == 'myCaptured':
                return random_walk()
            elif island_status[int(island[-1])-1] in ['myCapturing', '']:
                move = moveTo_safe(t_signal[5], t_signal[6],pirate)
                if move == 0:
                    return 1
                return move
            
        elif island == 'island3':
            if t_signal[7] == -1 or island_status[int(island[-1])-1] == 'myCaptured':
                return random_walk()
            elif island_status[int(island[-1])-1] in ['myCapturing', '']:
                move = moveTo_safe(t_signal[7], t_signal[8],pirate)
                if move == 0:
                    return 1
                return move
        



        # if pirate.getTeamSignal() == '':
        #     return random_walk()
    
        # else:
        #     temp = pirate.getTeamSignal().split('_')
        
        # if island_status[int(temp[0][-1])-1] == 'myCaptured':
        #     pirate.setTeamSignal('')
        # move = moveTo(int(temp[1]),int(temp[2]),pirate)
        # if move != 0:
        #     return move
def reinforcements():
    pass
def ActTeam(team):
    list1 = team.getListOfSignals()
    time = team.getCurrentFrame()
    no_of_pirates_to_island(team)

    # print(time, list1)
