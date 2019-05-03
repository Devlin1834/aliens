# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 04:17:44 2019

@author: Devlin
"""
import random as rn
###############################################################################
class Weapon():
    def __init__(self, name, damage, flavor, uses):
        self.name = name
        self.damage = damage
        self.flavor = flavor
        self.uses = uses
        
        self.used = 0
        
###############################################################################        
class Player():
    def __init__(self, health, armed, base_weapon):
        self.health = health
        self.armed = armed
        self.base_weapon = base_weapon
        self.triggers = 0
        self.prologue = True
        self.pages = 0
        self.boss = False
        self.encounter = False
        self.fourth = str(rn.randrange(1, 10))
        
    def drop_weapon(self):
        self.armed = self.base_weapon
        
    def update_status(self):
        pass

###############################################################################
class Beetle():
    def __init__(self, name, health, damage, stun_chance, drops):
        self.name = name
        self.health = health
        self.damage = damage
        self.stun_chance = stun_chance
        self.drops = drops
        self.dead = False

###############################################################################
def notnow():
    print("That doesn't seem very helpful right now")

###############################################################################
def transition(name):
    print("You pry open the door to the {}, it opens smoothly and quietly".format(name))

###############################################################################    
def linebreak(big = False):
    w = 100
    if big == False:
        print('-'*w)
    else:
        print('-'*w)
        print('+'*w)
        print('-'*w)
        
###############################################################################
def intcheck(string):
    while True:
        try:
            some_number = int(input(string))
        except ValueError:
            notnow()
        else:
            break
    
    return some_number
               
###############################################################################
def rangecheck(array, value):
    for i in range(1, value):
        try:
            print(str(i) + ": " + array[i])
        except KeyError:
            pass

###############################################################################
    
ship = """                _____     
               /     \\  
               |      \\_________
               | Labs /         \\
               |      | bridge  |
               \\      \\_________/        ____
                \\______|       |________/    \\
                /      |       |      |       \\
               /  Med  |       | Mess |        \\
             __|   Bay |       | Hall | Lounge |___
       _____|__|_______|_______|______|________|   \\ 
      /     |                                  |Obs \\
      )Dock |                                  | Bay| 
      \\_____|__________________________________|    /
            |  |               |__|       |    |___/
            |  |                  |  Sec  | Armory |
            |  |  Cargo Hold      | Office|________|
            |  |                  |_______|        |
            |  |                          | Engine |
            |  |__________________________|  Room  |
            |_____________________________|        |
            |                             |        |
            |                             |        |
            \\_____________________________|        |
               |    |   |    |   |    |   |        |
               |____|   |____|   |____|   |        |
               /    \\   /    \\   /    \\   \\________/
               \\    /   \\    /   \\    /     |    | 
                \\  /     \\  /     \\  /      |____| 
                 \\/       \\/       \\/       /    \\
                                            \\    /
                                             \\  /
                                              \\/                                          
 """        
###############################################################################