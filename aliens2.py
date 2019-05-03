# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:44:35 2019

@author: Devlin
"""

##Possible Addons - 
# Clones
# new victory methods
# purpose for lore
# more lore
# more rooms
# different player heros

import random as rn
import game_classes
import game_text
        
fists = game_classes.Weapon('bare fists', 5, "You slug your enemies across the 'face' with your fist", 10000)
lamp = game_classes.Weapon('heavy lamp', 10, "You brandish your lamp with skill and attack your opponent", 4)
bust = game_classes.Weapon('small bust', 10, "You brandish your bust with skill and attack your opponent", 9)
tool = game_classes.Weapon('crobar', 15, "You brandish your crobar with skill and attack your opponent", 20)
knife = game_classes.Weapon('kitchen knife', 20, "You brandish your kitchen knife with skill and attack your opponent", 7)
axe = game_classes.Weapon('axe', 18, "You brandish your axe with skill and attack your opponent", 10)
scalpel = game_classes.Weapon('scalpel', 20, "You brandish your scalpel with skill and attack your opponent", 12)
rifle = game_classes.Weapon('blaster rifle', 30, "You let loose with your blaster rifle, firing off several devestatng rounds that are sure to ruin someones day", 20)
suit = game_classes.Weapon('Exo-Suit', 50, "Your Exo-Suit whirs to life and supplies power to your devestating blows", 200)

hero = game_classes.Player(health = 100, armed = fists, base_weapon = fists)

kevin = game_classes.Beetle('Red Specks', 30, 8, 101, None)
dave = game_classes.Beetle('Blue Bars', 20, 9, 101, None)
shawn = game_classes.Beetle('No-Wings', 35, 5, 101, None)
gus = game_classes.Beetle('3-Arms', 15, 4, 51, None)
lassie = game_classes.Beetle('Sneak', 30, 8, 101, None)
jim = game_classes.Beetle('White Eyes', 25, 10, 201, None)
paul = game_classes.Beetle('Red Stripes', 30, 8, 101, None)
john = game_classes.Beetle('Green Marks', 30, 8, 101, None)
george = game_classes.Beetle('Black Stripes', 30, 8, 101, None)
ringo = game_classes.Beetle('The Small One', 40, 10, 101, None)
ben = game_classes.Beetle('Hairy', 30, 8, 101, None)
chris = game_classes.Beetle('Blue Specks', 30, 8, 101, None)
BBEG = game_classes.Beetle('The Warlord', 100, 15, 51, None)

###############################################################################
def combat(user, enemies):
    
    print("Health: {}".format(user.health))
    for beetle in enemies:
        print('{}\'s Health: {}'.format(beetle.name, beetle.health))
    print("\n")
    
    while len(enemies) > 0 and user.health > 0:
        print("Attack or Run")
        action = input("> ")
        ##-------------------------------------------------------------------##
        if 'a' in action.lower() or action == '1':
            print(user.armed.flavor)
            user.armed.used += 1
            enemies[0].health -= rn.randrange(1, user.armed.damage)
            if enemies[0].health <= 0:
                print('You killed {}!'.format(enemies[0].name))
                enemies[0].dead = True
                del enemies[0]
            else:
                print('{}\'s Health: {}'.format(enemies[0].name, enemies[0].health))
            ##----------------------------------------------------------------##    
            if user.armed.uses <= user.armed.used:
                if user.armed.name == 'blaster rifle':
                    print('\nYour {} has run out of ammo'.format(user.armed.name))
                    print('You\'ll have to rely on your fists for now\n')
                    user.drop_weapon()
                else:
                    broken = rn.randrange(1, 2)
                    if broken == 1:
                        print('\nYour {} has broken from overuse!'.format(user.armed.name))
                        print('You\'ll have to rely on your fists for now\n')
                        user.drop_weapon()
            ##---------------------------------------------------------------##            
            for beetle in enemies:
                print("\n{} attacks you with ferocity".format(beetle.name))
                user.health -= rn.randrange(1, beetle.damage)
                ##-----------------------------------------------------------##
                if user.armed.name == 'Exo-Suit':
                    print("But your armor absorbs most of the blow")
                    if user.health < 10:
                        user.health += 50
                        print("Your Exo Suit breaks down and spits you out unarmed!")
                        user.drop_weapon()         
                ##-----------------------------------------------------------##
                if user.armed.name not in ['bare fists', 'Exo-Suit']:
                    stun = rn.randrange(1, beetle.stun_chance)
                    if stun == 50:
                        print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
                        print("{} attacked you so viciously, he caused you to drop your {}!".format(beetle.name, user.armed.name))
                        user.drop_weapon()  
                print('Health: {}'.format(user.health))
                ##-----------------------------------------------------------##
        elif 'r' in action.lower() or action =="2":
            score = 2
            break        
        else:
            print("{} mocks your indecision!".format(rn.choice(enemies).name))
            user.health -= rn.randrange(0,2)
        ##-------------------------------------------------------------------##
                   
    
    if user.health <= 0:
        print('uh oh')
        score = 1       
    elif len(enemies) == 0:
        print("Health: {}".format(user.health))
        print("VICTORY")
        if user.encounter == False:
            print(game_text.seen)
            user.encounter = True
        score = 0
       
    return score
                
###############################################################################
def weapon_swap(user, new_weapon, joke = False):
    if new_weapon.damage == user.armed.damage:
        print("Give up you {} for the {}? This will have no impact on combat".format(user.armed.name, new_weapon.name))
    elif new_weapon.damage > user.armed.damage:
        print("Give up your {} for the {}? This will make you Stronger in combat".format(user.armed.name, new_weapon.name))
    elif new_weapon.damage < user.armed.damage:
        print("Give up your {} for the {}? This will make you weaker in combat".format(user.armed.name, new_weapon.name))
    
    yn = game_classes.intcheck("1 = Yes, 2 = No: ")
    if yn == 1:
        print('You are now equipped with a {}'.format(new_weapon.name))
        if joke == True:
            print('Thats what she said')
        old_weapon = user.armed
        user.armed = new_weapon
        if old_weapon == fists:
            return False
        else:
            return old_weapon
    else:
        print("You decide to keep your {}. You can come back for the {} later".format(user.armed.name, new_weapon.name))
        return new_weapon

###############################################################################
def heal(user, factor):
    print("Health: {}".format(user.health))
    print("This will heal you by {}, up to full health. Would you like to heal?".format(factor))
    yn = game_classes.intcheck("1 = Yes, 2 = No: ")
    if yn == 1:
        if user.health == 100:
            print("You do not need any healing you lucky duck!")
            return True
        else:
            user.health = min(user.health + factor, 100)
            print("Health: {}".format(user.health))
            return False
    else:
        print("You can come back for it later")
        return True
         
###############################################################################
class Engine():
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.run_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter(hero)
            current_scene = self.scene_map.run_scene(next_scene_name)
        
        current_scene.enter(hero)

###############################################################################        
class Death():

    quips = [
            "Death is for pussies and youre a pussy",
            "You lose",
            "You died. Now you'll never get to see that cool new movie",
            "There aren't 72 virgins where YOURE going",
            "I've seen monkeys masturbate with greater skill than you played this game",
            "You must really suck at life because this game is easy and you REALLY suck at this",
            "DED"
            ]
    
    def enter(self, protag):
        
        game_classes.linebreak(big = True)
        print(Death.quips[rn.randrange(0, len(self.quips) - 1)])
        return 'finished'

        
###############################################################################
class Lounge():
    
    weapon_available = lamp
    
    options = {1: 'Look around the lounge',
               2: 'Listen through the door to the Central Corridor',
               3: 'Walk out into the Central Corridor',
               4: 'Pick up the {}'.format(weapon_available.name),
               5: "Read 'The History of the UEA'",
               6: 'Go into the Mess Hall',
               7: 'Clean the Lounge',
               8: 'Read the Birthday Wall'}
    
    possibilities = {
                     1: game_text.lounge_la,
                     2: game_text.lounge_cc_door,
                     5: game_text.lore1,
                     8: game_text.lounge_calendar
                        }
    
    setup = 4
        
    def enter(self, protag):
        game_classes.linebreak(big = True)
        if protag.prologue == True:
            print("You are the captain of the freighter 'Resilience'")
            print("on a mission to deliver rations to the setlers of")
            print("Thiressa IX, a young colony on the edge of UEA space.")
            print("\n")
            print("After a long 20 hours of work, your small crew has returned")
            print("to the upper levels of the ship to rest and you have fallen")
            print("into an uneasy sleep in the ships crew lounge on the main floor.")
            print("As you drift between dim awareness and uncomfortable sleep you are")
            print("moved to full attention by a loud 'KLANG' and a deep 'THUD' echoing")
            print("throughout the ship. As you stuggle to figure out what must've happened")
            print("the power goes out and you hear scurrying coming from the central hallway.")
            print("\n")
            protag.prologue = False
        else:
            print("You enter the crew lounge, the area where the crew relaxes on their breaks")
        
        while True:            
            game_classes.linebreak()
            print("You take stock of your options")
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
        
            if choice in self.possibilities.keys():
                print(self.possibilities[choice].format(protag.fourth))
                if choice == 1:
                    self.setup = 9
            elif choice == 3:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 4 and self.weapon_available != False:
                self.weapon_available = weapon_swap(protag, self.weapon_available)
                if self.weapon_available == False:
                    del self.options[4]            
            elif choice == 6:
                game_classes.transition("Mess Hall")
                return 'mess_hall'
            else:
                game_classes.notnow()
                
###############################################################################                
class Mess_hall():
    
    weapon_available = knife
    
    options = {
            1: 'Look around the Mess Hall',
            2: 'Listen through the door to the Central Corridor',
            3: 'Listen through the door to the Main Body',
            4: 'Go into the Central Corridor',
            5: 'Go into the Main Body',
            6: 'Go into the Crew Lounge',
            7: 'Read the ship manual',
            8: 'Pickup the {}'.format(weapon_available.name),
            9: 'Do the dishes',
            }   
    
    possibilities = {
                    1: game_text.mess_la,
                    2: game_text.mess_cc_door,
                    3: game_text.mess_mb_door,
                    7: game_text.manual1
                     }
    
    setup = 7
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        print(game_text.mess_enter)
               
        while True:
            game_classes.linebreak()
            print('You take stock of your options:')
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice in self.possibilities.keys():
                print(self.possibilities[choice])
                if choice == 1:
                    self.setup = 10
                elif choice == 7:
                    protag.pages += 1
            elif choice == 4:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 5:
                game_classes.transition("Main Body")
                return 'main_body'
            elif choice == 6:
                game_classes.transition("Lounge")
                return 'lounge'
            elif choice == 8 and self.weapon_available != False:
                self.weapon_available = weapon_swap(protag, self.weapon_available)
                if self.weapon_available == False:
                    del self.options[8]
                else:
                    self.options[8] = 'Pickup the {}'.format(self.weapon_available.name)
            else:
                game_classes.notnow()
                                        
###############################################################################
class Bridge():
    
    invaders = [kevin, dave]
    
    weapon_available = rifle
    
    options = {
            1: 'Look Around the Bridge',
            2: 'Go into the Main Hall',
            3: 'Inspect the Navigators station',
            4: 'Inspect the Weapon Officers station',
            5: 'Inspect the Helmsmans Station',
            6: 'Inspect the Communication Station',
            7: 'Inspect the Ships Diagnostics',
            8: 'Inspect the Security Station',
            9: 'Inspect the Captains Station',
              }
    
    possibilities = {
                    1: game_text.bridge_la,
                    3: game_text.bridge_navigators,
                    4: game_text.bridge_gunnery,
                    5: game_text.bridge_helmsman,
                    6: game_text.lore2,
                    7: game_text.brige_diag,
                    8: game_text.bridge_sec
                    }
    
    setup = 3
    def enter(self, protag):        
        game_classes.linebreak(big = True)        
        if self.invaders != False:
            print("You enter the bridge expecting to find a full host of \nWar Beetles but there are only two waiting for you \n\nTHEY ATTACK")
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
        else:
            print("You enter the bridge, greeted by emptiness and darkness.")
                
        game_classes.linebreak()
        print(game_text.bridge_enter)
            
        while True:
            game_classes.linebreak()
            print('You take stock of your options: ')
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice in self.possibilities.keys():
                print(self.possibilities[choice])
                if choice == 1:
                    self.setup = 10                
            elif choice == 2:
                game_classes.transition("Main Body")
                return 'main_body'
            elif choice == 9:
                if self.weapon_available != False and protag.triggers == 0:
                    print("You approach the familiar captains chair and find your secret button.")
                    print("Upon pushing it, the back of the chair opens up to reveal a {}!".format(self.weapon_available.name))
                    self.weapon_available = weapon_swap(protag, self.weapon_available)
                
                if protag.triggers == 0:
                   print("If your ship was functioning, you could restart the ship and pilot your way out of here, but as of now, its still broken.")
                elif protag.triggers == 1:
                    print("The ship is fixed! You can pilot your way home from here!")
                    done = input("Are you ready to go home?\n >> ")
                    if "y" in done.lower():
                        return 'finished'
                    else:
                        print("Alright finish up then come back here later") 
            else:
                game_classes.notnow()
                
###############################################################################################################################
class Main_body():
    
    invaders = [shawn]
    final_boss = [BBEG]
    
    options = {
            1: 'Go into the Central Corridor',
            2: 'Go into the Med Bay',
            3: 'Go into the Bridge',
            4: 'Go into the Mess Hall',
            5: 'Look around the Main Body'
              }
    
    def enter(self, protag):
        game_classes.linebreak(big = True)       
        if self.invaders != False:
            print("You enter the ships Main Body and come face to face with a terrifying Zhendojan War Beetle \n\nIT CHARGES AT YOU")
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
        else:
            print("You enter the darkness of the Main Body")
            
        if self.final_boss != False and protag.triggers == 1:
            print(game_text.mainbody_boss)
            input('Ready or not here he comes (hit enter) ')
            boss_battle = combat(protag, self.final_boss)
            if boss_battle == 1:
                return 'death'
            elif boss_battle == 2:
                return 'lounge'
            else:
                self.final_boss = False
        
        while True:
            game_classes.linebreak()
            print('You take stock of your options: ')
            game_classes.rangecheck(self.options, 5)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                game_classes.transition("Med Bay")
                return 'med_bay'
            elif choice == 3:
                game_classes.transition("Bridge")
                return 'bridge'
            elif choice == 4:
                game_classes.transition("Mess Hall")
                return 'mess_hall'
            elif choice == 5:
                print(game_text.mainbody_la)
            else:
                game_classes.notnow()

###############################################################################################################################
class Med_bay():
    
    weapon_available = scalpel
    healing_available = True
    
    options= {
            1: 'Look around the Med Bay',
            2: 'Go to the Main Body',
            3: 'Go to the Science Labs',
            4: 'Go to the Central Corridor',
            5: 'Read the Ships Manual',
            6: 'Use the Medijector',
            7: 'Pick up the {}'.format(weapon_available.name),                  
            }
    
    posibilities = {1: game_text.medbay_la,
                    5: game_text.manual2}
    setup = 5
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        print("You enter the Med bay to find it empty and dormant.")
        
        while True:            
            game_classes.linebreak()
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice in self.posibilities.keys():
                print(self.posibilities[choice])
                if choice == 1:
                    self.setup = 8
                elif choice == 5:
                    protag.pages +=1
            elif choice == 2:
                game_classes.transition("Main Body")
                return 'main_body'
            elif choice == 3:
                game_classes.transition("Science Labs")
                return 'sci_labs'
            elif choice == 4:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 6 and self.healing_available == True:
                self.healing_available = heal(protag, 80)
                if self.healing_available == False:
                    del self.options[6]
            elif choice == 7 and self.weapon_available != False:
                self.weapon_available = weapon_swap(protag, self.weapon_available)
                if self.weapon_available == False:
                    del self.options[7]
                else:
                    self.options[7] = 'Pickup the {}'.format(self.weapon_available.name)
            else:
                game_classes.notnow()
                
###############################################################################################################################
class Sci_labs():
    
    options = {
            1: 'Look around the Lab',
            2: 'Go to the Med Bay',
            3: 'Read the Report',
            4: 'Read the Ships Manual',
            5: "Read the 'History of Colonization'",
            6: 'Look a the star chart',
            7: 'Touch the instruments anyways'
                      }
    
    possiblities = {1: game_text.scilab_la,
                    3: game_text.lore3,
                    4: game_text.manual3,
                    5: game_text.lore4,
                    6: game_text.lore8,
                    7: game_text.scilab_device}
    
    setup = 3  
    def enter(self, protag):
        game_classes.linebreak(big = True)
        print("You enter the Science Lab to find it empty and dormant.")   
             
        while True:
            game_classes.linebreak()
            print('You take stock of your options: ')
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()

            if choice in self.possiblities.keys():
                print(self.possiblities[choice])
                if choice == 1:
                    self.setup = 8
                elif choice == 4:
                    protag.pages += 1
            elif choice == 2:
                game_classes.transition("Med Bay")
                return 'med_bay'
            else:
                game_classes.notnow()

###############################################################################################################################
class Observation():
    
    weapon_available = bust
    
    options = {
               1: 'Return to the Central Corridor',
               2: 'Pick up the {}'.format(weapon_available.name),
               3: "Read 'Space Warfare'",
               4: 'Remember that time you banged that Green Skinned Hottie in here'
               }
    
    possibilities = {3: game_text.lore5,
                     4: 'Yeah that was hot'}
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        print(game_text.odeck_enter)
        while True:
            game_classes.linebreak()
            print('You take stock of your options: ')
            game_classes.rangecheck(self.options, 5)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice in self.possibilities.keys():
                print(self.possibilities[choice])
            elif choice == 1:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 2 and self.weapon_available != False:
                self.weapon_available = weapon_swap(protag, self.weapon_available, joke = True)
                if self.weapon_available == False:
                    del self.options[2]
                else:
                    self.options[2] = 'Pickup the {}'.format(self.weapon_available.name)
            else:
                game_classes.notnow()

###############################################################################################################################
class Docking():
    
    invaders = [gus]
    
    options = {
            1: 'Return to the Central Corridor',
            2: 'Read the tablet',
            3: 'Knock on the hatch'
            }
    
    def enter(self, protag):        
        game_classes.linebreak(big = True)
        
        if self.invaders != False:
            print("You enter the Docking Bay and come face to face with a terrifying Zhendojan War Beetle\n\nIT CHARGES AT YOU")
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
    
        
        print(game_text.docking_enter)
        
        knocks = 10       
        while True:
            game_classes.linebreak()
            print("You take stock of your options:")
            game_classes.rangecheck(self.options, 4)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                print(game_text.lore6)
            elif choice == 3:
                print("You knock on the hatch")
                print("...")
                print("A War Beetle jumps out and attack you!")
                k_strategy = combat(protag, [game_classes.Beetle('The Beetle', 30 + knocks, 8, 101, None)])
                knocks += 5
                if k_strategy == 1:
                    return 'death'
                elif k_strategy == 2:
                    return 'lounge'
            else:
                game_classes.notnow()

###############################################################################################################################
class Security():
    
    options = {
            1: 'Look around the Security Offices',
            2: 'Return to the Central Corridor',
            3: 'Read the Security Dossier',
            4: 'Look at the Map',
            5: 'Try to enter the Armory'
            }
    
    possibilities ={
                    1: game_text.sec_la,
                    3: game_text.lore7,
                    4: game_classes.ship
                    }
    
    alarm = 0
    armory_open = False
    setup = 3 
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        print(game_text.sec_enter)
                     
        while True:
            game_classes.linebreak()
            print('You take stock of your options: ')
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice in self.possibilities.keys():
                print(self.possibilities[choice])
                if choice == 1:
                    self.setup = 6
            elif choice == 2:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 5 and self.alarm < 3:
                print(game_text.sec_door)
                code = "891" + protag.fourth + "7"
                code_guess = ''                
                while code != code_guess and self.alarm < 3:
                    code_guess = input("Enter the Five Digit Code: ")
                    if code == code_guess:
                        self.armory_open = True
                        game_classes.transition("Armory")
                        return 'armory'
                    else:
                        print("BEEPBEEP" * self.alarm)
                        self.alarm += 1
                
                if self.alarm == 3:
                    print("You feel a sharp ZAP as the keypad shocks you for getting the code wrong, AGAIN")
                    print("The Door now locks itself down even more, and you realize it will be impossible to get in")
                    del self.options[5]
                    if protag.health <= 5:
                        pass
                    else:
                        protag.health -= 5
           
            elif choice == 5 and self.armory_open == True:
                game_classes.transition("Armory")
                return 'armory'
            else:
                game_classes.notnow()

###############################################################################################################################
class Central_c():
    
    invaders = [lassie]
    
    options = {            
            1: 'Go into the Lounge',
            2: 'Go into the Mess Hall',
            3: 'Go into the Main Body',
            4: 'Go into the Med Bay',
            5: 'Go onto the Observation Deck',
            6: 'Go into the Security Offices',
            7: 'Go onto the Cargo Hold Catwalk',
            8: 'Go into the Cargo Hold',
            9: 'Try to access the barricaded Crew Quarters',
           10: 'Go into the Docking Bay',   
           }
    
    def enter(self, protag):        
        game_classes.linebreak(big = True)
        if self.invaders != False:
            print("You enter the Central Corridor to find complete darkness")
            print("Suddenly you feel a WHACK and fall down face first!")
            if protag.health <= 5:
                pass
            else:
                protag.health -= 5
            print("YOU ARE UNDER ATTACK")
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
        else:
            print("You enter the central Corridor to find complete darkness")
            
        print(game_text.cc_enter)
        while True:
            game_classes.linebreak()
            print('You take stock of your options:')
            game_classes.rangecheck(self.options, 11)      
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1:
                game_classes.transition("Lounge")
                return 'lounge'
            elif choice == 2:
                game_classes.transition("Mess Hall")
                return 'mess_hall'
            elif choice == 3:
                game_classes.transition("Main Body")
                return 'main_body'
            elif choice == 4:
                game_classes.transition("Med Bay")
                return 'med_bay'
            elif choice == 5:
                game_classes.transition("Observation Deck")
                return 'observation'
            elif choice == 6:
                game_classes.transition("Security Offices")
                return 'security'
            elif choice == 7:
                game_classes.transition("Catwalk")
                return 'catwalk'
            elif choice == 8:
                game_classes.transition("Cargo Hold Access")
                return 'cargo_a'
            elif choice == 9:
                print("You approach the barricaded door")
                return 'quarter_a'
            elif choice == 10:
                game_classes.transition("Docking Bay")
                return 'docking'
            else:
                game_classes.notnow()
            
###############################################################################################################################
class Armory():
    
    weapon_available = rifle
    suit_available = suit
    healing_available = True
    
    options = {
            1: 'Pick up the {}'.format(weapon_available.name),
            2: 'Return to the Security Offices',
            3: 'Put on the {}'.format(suit_available.name),
            4: 'Use the Medipack'
            }
       
    def enter(self, protag):        
        game_classes.linebreak(big = True)
        print(game_text.armory_enter)        
        while True:
            game_classes.linebreak()
            print("You take stock of your options: ")
            game_classes.rangecheck(self.options, 5)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1 and self.weapon_available != False:
                self.weapon_available = weapon_swap(protag, self.weapon_available)
                if self.weapon_available == False:
                    del self.options[1]
                else:
                    self.options[1] = 'Pickup the {}'.format(self.weapon_available.name)
            elif choice == 2:
                game_classes.transition("Security Offices")
                return 'security'
            elif choice == 3 and self.suit_available != False:
                self.suit_available = weapon_swap(protag, self.suit_available)
                if self.suit_available == False:
                    del self.options[3]
                else:
                    self.options[3] = 'Pickup the {}'.format(self.weapon_available.name)
            elif choice == 4 and self.healing_available == True:
                self.healing_available = heal(protag, 40)
                if self.healing_available == False:
                    del self.options[4]
            else:
                game_classes.notnow()

###############################################################################################################################
class Cargo_a():
    
    weapon_available = tool
    
    options = {
            1: 'Return to the Central Corridor',
            2: 'Proceed to the Cargo Hold',
            3: 'Pick up the {}'.format(weapon_available.name)
            }
    
    def enter(self, protag):        
        game_classes.linebreak(big = True)                
        print(game_text.cagroa_enter)       
        while True:
            game_classes.linebreak()
            print("You take stock of your options: ")
            game_classes.rangecheck(self.options, 4)              
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
           
            if choice == 1:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                game_classes.transition("Cargo Hold")
                return 'cargo_h'
            elif choice == 3 and self.weapon_available != False:
               self.weapon_available = weapon_swap(protag, self.weapon_available, joke = True)
               if self.weapon_available == False:
                   del self.options[3]
               else:
                   self.options[3] = 'Pickup the {}'.format(self.weapon_available.name)
            else:
                game_classes.notnow()

###############################################################################################################################
class Cargo_h():
    
    invaders = [jim, paul]
    weapon_available = axe
    healing_available = True
    
    options = {
            1: 'Return to the Central Corridor',
            2: 'Look around the Cargo Hold',
            3: 'Take a closer look at your cargo',
            4: 'Read the newspaper',
            5: 'Pick up the {}'.format(weapon_available.name),
            6: 'Use the Medipack',
            }
    
    possibiliies = {2: game_text.cargoh_la,
                    3: game_text.lore9,
                    4: game_text.lore10}   
    setup = 3
    
    def enter(self, protag):        
        game_classes.linebreak(big = True)
        if self.invaders != False:
            print("You are ambushed by two Zhendojan War Beetles!")
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
        else:
            print("You enter the Cargo Hold")
                
        while True:
            game_classes.linebreak()
            print("You take stock of your options:")
            game_classes.rangecheck(self.options, self.setup)                 
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1:
                game_classes.transition("Cargo Access")
                return 'cargo_a'
            elif choice in self.possibiliies.keys():
                print(self.possibiliies[choice])
                if choice == 2:
                    self.setup = 7
            elif choice == 5 and self.weapon_available != False:
                self.weapon_available = weapon_swap(protag, self.weapon_available)
                if self.weapon_available == False:
                    del self.options[5]
                else:
                    self.options[5] = 'Pickup the {}'.format(self.weapon_available.name)
            elif choice == 6 and self.healing_available == True:
                self.healing_available = heal(protag, 40)
                if self.healing_available == False:
                    del self.options[6]
            else:
                game_classes.notnow()

###############################################################################################################################
class Catwalk():
    
    invaders = [john, george]
    
    options = {1: 'Return to the Central Corridor',
               2: 'Proceed into the Engine Room'}
    
    setup = 3 
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        
        if self.invaders != False:
            print("You walk out onto the catwalk and see two Zhendojan Beetles standing guard over the Engine Room")
            print("They see you and start angrilly clicking")
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
        else:
            print("You walk onto the catwalk overlooking the Cargo Hold")

        while True:
            game_classes.linebreak()
            print("You take stock of your options: ")
            game_classes.rangecheck(self.options, self.setup)
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1:
                game_classes.transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                game_classes.transition("Engine Room")
                return 'eng_room'
            else:
                game_classes.notnow()
                
###############################################################################################################################
class Eng_room():
     
    invaders = [ringo, ben, chris]
    
    options = {
            1: 'Return to the Catwalk',
            2: 'Take a look around the Engine Room',
            3: 'Read the Ships Manual',
            4: 'Repair the Engine '
            }
    
    possibilities = {2: game_text.eng_la,
                     3: game_text.manual4}
    
    setup = 3 
    def enter(self, protag):       
        if self.invaders != False: 
            print(game_text.eng_attack)
            strategy = combat(protag, self.invaders)
            if strategy == 1:
                return 'death'
            elif strategy == 2:
                return 'lounge'
            else:
                self.invaders = False
        else:
            print("You enter the engine room and take a look around.")
            
        while True:
            game_classes.linebreak()
            print('You take stock of your options: ')
            game_classes.rangecheck(self.options, self.setup)                      
            choice = game_classes.intcheck("Pick the number of your choice > ")
            game_classes.linebreak()
            
            if choice == 1:
                game_classes.transition("Catwalk")
                return 'catwalk'
            elif choice in self.possibilities.keys():
                print(self.possibilities[choice])
                if choice == 2:
                    self.setup = 5
                elif choice == 3:
                    protag.pages += 1
            elif choice == 4 and protag.triggers == 0:
                print(game_text.eng_repair)
                yn = game_classes.intcheck("Fix Engine?  1 = Yes, 2 = No: ")
                if yn == 1:
                    while True:
                        low_end = min(protag.pages, 4)
                        if protag.armed == tool:
                            low_end += 1
                        
                        attempt = rn.randrange(low_end, 11)
                        if attempt == 7:
                            protag.triggers = 1
                            print(game_text.eng_fix)
                            del self.options[4]
                            break
                        else:
                            print('\nA Beetle found you while you were working!\n')
                            e_strategy = combat(protag, [game_classes.Beetle('The Beetle', 30, 8, 101, None)])
                            if e_strategy == 1:
                                return 'death'
                            elif e_strategy == 2:
                                return 'lounge'   
            else:
                game_classes.notnow()
        
###############################################################################################################################
class Quarter_a():
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        print(game_text.cc_qa)
        return 'central_c'

###############################################################################################################################
class Finished():
    
    def enter(self, protag):
        game_classes.linebreak(big = True)
        if protag.health > 0:
            print(game_text.victory)
        else:
            print('Try again')
        game_classes.linebreak(big = True)

###############################################################################################################################
class Map():
    
    scenes = {
            'bridge': Bridge(),
            'main_body': Main_body(),
            'med_bay': Med_bay(),
            'mess_hall': Mess_hall(),
            'sci_labs': Sci_labs(),
            'observation': Observation(),
            'lounge': Lounge(),
            'docking': Docking(),
            'security': Security(),
            'central_c': Central_c(),
            'armory': Armory(),
            'cargo_a': Cargo_a(),
            'cargo_h': Cargo_h(),
            'catwalk': Catwalk(),
            'eng_room': Eng_room(),
            'quarter_a': Quarter_a(),
            'death': Death(),
            'finished': Finished()
            }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def run_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.run_scene(self.start_scene)

###############################################################################################################################

a_map = Map('lounge')
a_game = Engine(a_map)
a_game.play()       