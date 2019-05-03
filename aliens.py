# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:13:30 2017

@author: Devlin
"""

### Aliens Attack

import random as rn
from sys import exit


armed = 0
lose = 0
health = 100
kills = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ship = "broken"
start = 0
weapon = "Bare Fists"
h_obs = [0, 0, 0, 0, 0, 0]
t_obs = [0, 0, 0, 0]
l_obs = [0, 0, 0, 0, 0]
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
z = 'Zhendojan'
fourth = str(rn.randrange(1,9))

################################################################################################################################
def combat(enemies):
    global health
    global weapon
    global kills
    global armed
    global lose
    
    e_health = 30 * enemies
    
    while e_health > 0 and health > 0:
        
        print("Health: %d" %health)
        print("Enemies Health: %d" %e_health)
        print("\n")
        print("Attack or Run")
        action = input("> ")
        
        if action == "Attack" or action == "attack" or action == "1":
            if armed == 0:
                print("You slug your enemies across the 'face' with your fist")
                e_health -= rn.randrange(1,5)
                
                print("Your enemies attack you with ferocity")
                health -= rn.randrange(1,8) * enemies


            elif armed == 1 or armed == 2 or armed == 3:
                print("You brandish your %s with skill and attack your opponent" %weapon)
                e_health -= rn.randrange(1,7) * armed
                
                print("Your enemies attack you with ferocity")
                health -= rn.randrange(1,8) * enemies
                stun = rn.randrange(1,101)
                if stun == 50:
                    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
                    print("They attack you so viciously, they cause you to drop your %s!" %weapon)
                    armed = 0
                    weapon = "Bare Fists"
            
            elif armed == 4:
                shots = rn.randrange(2,7)
                print("Your Blaster Rifle hums as it charges up, then releases %d shots" %shots)
                print("with a series of PEWs that can only sound like pain")
                e_health -= rn.randrange(2,5) * shots
            
                print("Your enemies attack you with ferocity")
                health -= rn.randrange(1,8) * enemies
                stun = rn.randrange(1,101)
                if stun == 50:
                    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
                    print("They attack you so viciously, they cause you to drop your %s!" %weapon)
                    armed = 0
                    weapon = "Bare Fists"
                
            elif armed == 5:
                print("Your Exo-Suit releases a volley of shots from guns and cannons hidden")
                print("in places where you didnt thing a such a thing could fit")
                e_health -= rn.randrange(10,51)
                
                print("Your enemies attack you with ferocity")
                print("But your armor absorbs most of the blow")
                health -= rn.randrange(0,2) * enemies 
                stun = rn.randrange(1,101)
                if stun == 50:
                    print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
                    print("They sucker punch you and get another cheap shot in")
                    health -= rn.randrange(0,2) * enemies
                
        elif action == "Run" or action == "run" or action =="2":
            lose = 2
        
        else:
            print("Thats not going to help and neither is wasting time!")
            health -= rn.randrange(0,2) * enemies
                
    if health <= 0:
        lose = 1
    elif health <= 0 and armed == 5:
        armed = 0
        health += 50
        print("Your Exo Suit breaks down and spits you out unarmed!")
    elif e_health <= 0:
        print("Health: %d" %health)
        print("VICTORY")
                
################################################################################################################################
def weapon_swap(new_weapon, level, index):
    global armed
    global weapon
    global yn
    global ones
    if level == armed:
        print("Give up you %s for the %s? This will have no impact on combat" %(weapon, new_weapon))
        yn = int(input("1 = Yes, 2 = No: "))
        if yn == 1:
            armed = level
            weapon = new_weapon
            ones[index] = 1
            print("Your are now equiped with a %s" %weapon)
        else:
            print("You decide to keep your %s. You can come back for the %s later" %(weapon, new_weapon))
    elif level > armed:
        print("Give up your %s for the %s? This will make you Stronger in combat" %(weapon, new_weapon))
        yn = int(input("1 = Yes, 2 = No: "))
        if yn == 1:
            armed = level
            weapon = new_weapon
            ones[index] = 1
            print("Your are now equiped with a %s" %weapon)
        else:
            print("You decide to keep your %s. You can come back for the %s later" %(weapon, new_weapon))
    elif level < armed:
        print("Give up your %s for the %s? This will make you weaker in combat" %(weapon, new_weapon))
        yn = int(input("1 = Yes, 2 = No: "))
        if yn == 1:
            armed = level
            weapon = new_weapon
            ones[index] = 1
            print("Your are now equiped with a %s" %weapon)
        else:
            print("You decide to keep your %s. You can come back for the %s later" %(weapon, new_weapon))

################################################################################################################################
def heal(factor, index):
    global health
    global ones
    print("Health: %d" %health)
    print("This will heal you by %s, up to full health. Would you like to heal?" %factor)
    yn = int(input("1 = Yes, 2 = No: "))
    if yn == 1:
        if 100 - health < factor:
            health = 100
            ones[index] = 1
            print("Health: %d" %health)
        elif 100 - health > factor:
            health += factor
            ones[index] = 1
            print("Health: %d" %health)
        elif health == 100:
            print("You do not need any healing you lucky duck!")
    else:
        print("You can come back for it later")
         
################################################################################################################################
def notnow():
    print("That doesn't seem very helpful right now")

################################################################################################################################
def transition(name):
    global cleared

    cleared = 1
    print("You pry open the door to the %s, it opens smoothly and quietly" %name)
        
################################################################################################################################    
class Scene(object):
    
    def enter(self):
        print("There should be a subclass here")
        exit(0)
        
################################################################################################################################
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()

################################################################################################################################        
class Death(Scene):

    quips = [
            "Death is for pussies and youre a pussy",
            "You lose",
            "You died. Now you'll never get to see that cool new movie",
            "There aren't 72 virgins where YOURE going",
            "I've seen monkeys masturbate with greater skill than you played this game",
            "You must really suck at life because this game is easy and you REALLY suck at this",
            "DED"]
    
    def enter(self):
        

        print(Death.quips[rn.randrange(0, len(self.quips) - 1)])

        
################################################################################################################################
class Lounge(Scene):
        
    def enter(self):
        global health
        global armed
        global start
        global weapon
        global h_obs
        global ones
        global yn
        if start == 0:
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
        if start == 1:
            print("You enter the crew lounge, the area where the crew relaxes on their breaks")
        
        cleared = 0
        setup = 0
        
        while cleared == 0:
            
            if setup == 0:
                print("-" * 65)
                print("""You take stock of your options
            1. Look around the Lounge
            2. Listen through the door to the Central Corridor
            3. Walk out into the Central Corridor
              """)
            elif setup == 1 and ones[0] == 0:
                print("-" * 65)
                print("""You take stock of your options
            1. Look around the Lounge
            2. Listen through the door to the Central Corridor
            3. Walk out into the Central Corridor
            4. Pick up the lamp to use as a blunt weapon
            5. Read 'The History of the UEA'
            6. Go into the Mess Hall
            7. Clean the Lounge
            8. Scream for help
              """)
            elif setup ==1 and ones[0] == 1:
                print("-" * 65)
                print("""You take stock of your options
            1. Look around the Lounge
            2. Listen through the door to the Central Corridor
            3. Walk out into the Central Corridor
            5. Read 'The History of the UEA'
            6. Go into the Mess Hall
            7. Clean the Lounge
            8. Scream for help
              """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
        
            if choice == 1:
                print("""                                
The Lounge is the area where your crew goes to relax on their breaks,
close enough to the Mess and the Quarters for easy relaxation, but close enough
to the Bridge to come back quickly in case of emergency.

There are many sofas and armchairs spread over the room, including the one you were just sleeping in.
The room is messy with many books, magazines, empty plates and glasses strewn about.

There is a door to the Central Corridor behind you and a door to the Mess hall to your left.
The wall in front of you is adorned with monitors for entertainment and the wall to the right
is a window that shut its blast door when the power cut off.

The power is out so the Ships onboard Computer is not responsive
The automated doors are not working either, meaning they will need to be
pryed open. The life support is hooked up to auxillery power and seems to be working.
With no power there is no way to call for help or contact your crew without screaming.

You notice a small lamp that can easily be used as a club and a book titled
'The History of the UEA'. This forces you wonder who on your crew is a closet dork
""")
                setup = 1
            elif choice == 2:
                print("You approach the door and listen for a while")
                print("A rush of fear runs through you when you hear a faint clicking")
                print("Clicking is the primary communication method of Zhendojan War Beetles")
                print("Known for beheading enemies with their powerful jaws, climbing on walls,")
                print("running at upwards of 30 miles an hour, and having near impenetrable armor")
                print("Their only real weakness is a distaste for light")
                print("Of course without visual confirmation you cannot be sure what you're hearing")
            elif choice == 3:
                start = 1
                transition("Central Corridor")
                return 'central_c'
            elif choice == 4 and ones[0] == 0:
                weapon_swap("Heavy Lamp", 1, 0)
            elif choice == 5:
                print("""
                      The UEA (United Earth Alliance) was formed in 2187 after first contact by the Galminorans.
                      The five member nations, The United States, China, India, Japan, and Germany, were all determined
                      to spearhead the first manned mission into Galminoran space in order to initiate trade proceedings.
                      For each country, allowing another country to beat them to Galminoran space posed a serious security
                      threat, so they formed an economic alliance, devoted to creating a spacecraft capable of deep space
                      travel, jointly manning that craft, and begining trade negotiations as a single entity. As the founding
                      nations reaped the benefits of Iter-Galactic trade, the UEA transitioned from a trade partnership
                      into a shared government, and was soon adopted by all 155 earth nations.
                      """)
                h_obs[0] = 1
            elif choice == 6:
                start = 1
                transition("Mess Hall")
                return 'mess_hall'
            else:
                notnow()
                
################################################################################################################################                
class Mess_hall(Scene):
    
    def enter(self):
        global health
        global armed
        global weapon
        global t_obs
        global ones
        print("""
You enter the Mess Hall of the ship, basically the ships kicthen.
It has access to the Central Corridor and the Main Body of the Ship
""")
        
        cleared = 0
        setup = 0
        
        while cleared == 0:
            
            if setup == 0:
                print("-" * 65)
                print("""
You take stock of your options:
            1. Look around the Mess Hall
            2. Listen through the door to the Central Corridor
            3. Listen through the door to the Main Body
            4. Go into the Central Corridor
            5. Go into the Main Body
            6. Go to the Crew Lounge
            """)
            if setup == 1 and ones[1] == 0:
                 print("-" * 65)
                 print("""
You take stock of your options:
            1. Look around the Mess Hall
            2. Listen through the door to the Central Corridor
            3. Listen through the door to the Main Body
            4. Go into the Central Corridor
            5. Go into the Main Body
            6. Go into the Crew Lounge
            7. Read the ship manual
            8. Pickup the kitchen knife
            9. Do the dishes
            """)    
            if setup == 1 and ones[1] == 1:
                 print("-" * 65)
                 print("""
You take stock of your options:
            1. Look around the Mess Hall
            2. Listen through the door to the Central Corridor
            3. Listen through the door to the Main Body
            4. Go into the Central Corridor
            5. Go into the Main Body
            6. Go into the Crew Lounge
            7. Read the ship manual
            9. Do the dishes
            """)    
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                print("""
Looking around the mess hall you notice the dirty dishes and 
cant help but think you hired a bunch of slobs. There is bread
and open bags of chips left open on the counter, probably stale at this
point. They go stale much faster in the highly oxygenated environment
of the ship. 

On the countertop you notice a copy of the ships manual, opened to the 
first chapter. You also notice a kitchen knife sitting in the sink.

There are three doors in the Mess Hall: one to the Central Corridor that runs
horrizonatlly accross the ship, one to the Main Body that runs Vertically
from the Central Corridor up to the bridge, and one that leads to the Crew Lounge
where the crew relaxes in their free time.
                    """)
                setup = 1
            elif choice == 2:
                print("""
You hear a faint clicking sound and the scurrying of multiple legs on the ground. Occasionally
the clicking is punctuated by the sound of a clanging or a trilling. The invaders sound like
insects!
                    """)
            elif choice == 3:
                print("""
You hear a tapping sound coming from the halway and the sound of a heavy metal door being 
pryed open. Only the Bridge has a door that heavy. If the invaders have made it to the Bridge
you're in bad shape.                          
                      """)
            elif choice == 4:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 5:
                transition("Main Body")
                return 'main_body'
            elif choice == 6:
                transition("Lounge")
                return 'lounge'
            elif choice == 7:
                print("""
                      Congratulations on purchasing a Strong-Man Class Freighter!
                      We at BLG believe that this class of freighter represents the 
                      most important advancement in space travel technology: 
                                              SAFETY
                      There was a time when travelers had to fear every bumb and jostle
                      of their trip, but those times are far behind us. The Strong-Man
                      is built to hold together, and, if necessary, be put back together.
                      There is no part of the Strong-Man that is not easily fixed with
                      tools found in every mechanics war chest. Even the first of its kind
                      engine is capable of being fixed with just a handfull of tools.
                      """)
                t_obs[0] = 1
            elif choice == 8 and ones[1] == 0:
                weapon_swap("Kitchen Knife", 2, 1)
            else:
                notnow()
                                        
###############################################################################################################################
class Bridge(Scene):
    
    def enter(self):
        global health
        global weapon
        global armed
        global h_obs
        global l_obs
        global ship
        
        print("-" * 65)
        
        if kills[1] == 0 and kills[2] == 0:
            print("""
You enter the bridge expecting to find a full host of War Beetles but there are only two waiting for you
THEY ATTACK              
              """)
            combat(2)
            if lose == 1:
                return 'death'
            elif lose == 2:
                return 'lounge'
            elif lose != 1 and lose != 2:
                kills[1] = 1
                kills[2] = 1
        elif kills[1] == 1 and kills[2] == 1:
            print("""
You enter the bridge, greeted by emptiness and darkness.                  
            """)
        
        cleared = 0
        setup = 0
        
        print("-" * 65)
        print("""
You look around the bridge of your ship. Backup power is  running the central consoles 
and there doesn't seem to be any damage done by the invader.
You struggle to determine what exactly the Beetle was doing here.      
            """)
            
        while cleared == 0:

            if setup == 0:
                print("-" * 65)
                print("""
You take stock of your options:
            1. Look Around the Bridge
            2. Go into the Main Hall
              """)
            if setup == 1:
                print("-" * 65)
                print("""
You take stock of your options:
            1. Look Around the Bridge
            2. Go into the Main Hall
            3. Inspect the Navigators station
            4. Inspect the Weapon Officers station
            5. Inspect the Helmsmans Station
            6. Inspect the Communication Station
            7. Inspect the Ships Diagnostics
            8. Inspect the Security Station
            9. Inspect the Captains Station
              """)

            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                setup = 1
                print("""
The bridge is a large open room, mostly full of chairs and screens. The Walls and floors are all
an uninteresting grey, in order to avoid distraction and the front wall is a large window out the front
of the ship. 

In the center of the room sits the primary console, the seats of the Navigator, Gunnery Officer,
and Helmsman. The communication console was on the edge of the room, next to the ships diagnostics.
The ships secuirty center was opposite the communication center, its many monitors  taking up most of the wall.
In the center of the room sat the captains chair and console.

Out the window at the helm, you could see the infinite darkness of space.                      
                
                      """)
            elif choice == 2:
                transition("Main Body")
                return 'main_body'
            elif choice == 3:
                print("""
You observe the navigators station, a system of computers designed to plot courses through warp-space.
Warp-space is incredibly dangerous to travel through, but necessary in order to reach distant planets in
a decent amount of time. Looking at the course plotted, you notice an anomaly. The Navigator had you taking
an unusual route to Thiressa IX, bearing abnormally close to an unexplored system of planets. Typically
navigators take pains to veer as far away from objects as possible in warp-space. It's probably just
a quirk of your Navigator, but you make a copy of the course and pocket it, just in case.                    
                      """)
                l_obs[2] = 1
            elif choice == 4:
                print("""
Upon examining the Gunnery Officers console it becomes apparent what one Beetle was up to.
The console is broken, and the ship is unable to operate its weaponry without it.                      
                      """)
            elif choice == 5:
                print("""
It seems one Beetle adjusted the settings at the helmsman station. You don't recognize the
coordinates but write them down, just to be safe.

                      57815  16278  93214
                      """)
            elif choice == 6:
                print("""
The communications log is open to a file descibing the structure of the UEA:

                      The UEA is a loosely structured economic alliance. It possess a military made up of rotating
                      batallions from the militaries of its member nations. These donated batallions spend 3-5
                      years fighting for the UEA, then return to their home countries and pursue the ambitions
                      of their local governments and cultures.
                      
                      On the civilian side, The UEA directly governs only its colonies. Governing at home is left
                      to national governments. People are incentivized into settling on new colonies with generous
                      subsidies and homesteads. The colonies had the advantage of being closer to Galactic Society
                      than Earth, meaning better trade, but being so far from home bore its own challenges.
                      They cannot grow enough food to sustain themselves and cannot manufacture enough to 
                      support their lifestyles. Colonies rely upon UEA supply drops to maintain their people
                      and equipment.
                      
                      As of 2289, only 350,000 people had settled in colonies.
                      """)
                h_obs[1] = 1               
            elif choice == 7:
                print("""
The ships diagnostic network runs throughout the walls and tells the central computer when a peice of
the ship is broken. The diagnotic system indicates that the engines are malfunctioning and that there is a
breach in the docking bay. It does not indicate the cause of the extent of the damage without primary power

You can guess that the Beetles have sabotaged the engines in order to cut the power, and entered the ship through
the breach in the docking bay                      
                      """)   
            elif choice == 8:
                print("""
The security station possessed a number of monitors, the only one powered by the backup generator was
the security camera access. You can flip through the various rooms of the ship.
""")

                print("""
The bridge is empty, except for you
The Main Body is empty and dark
The Mess Hall is Empty
The Lounge is Empty
The Med Bay is empty
The Science Labs are empty
The Observation Deck is empty
The Security Offices are empty
The camera in the Armory is broken""")
                if kills[7] == 0:
                    print("There is one Beetle in the Central Corridor")
                elif kills[7] == 1:
                    print("The Central Corridor is empty")
                if kills[3] == 0:
                    print("There are two Beetles in the Cargo Hold")
                elif kills[3] == 1:
                    print("The Cargo Hold is empty")
                if kills[5] == 0:
                    print("There are two Beetles on the Cat Walk")
                elif kills[5] == 1:
                    print("The catwalk is clear")
                print("""The camera in the Engine Room is broken
The camera in the Docking Bay is broken""")
                
                
                print("""      
You can see the most crew pounding on the door to the upper deck,
the Beetles must've barricaded the door. The Navigator is sitting in
his bed with his head in his hands and the Doctor is in the Gunnery
Officers room, setting what looks to be a broken arm. Your crew needs you!
                      """)
            elif choice == 9:
                if ones[2] == 0:
                    print("""
You approach the familiar captains chair and find your secret button. Upon pushing it, the
back of the chair opens up to reveal a blaster rifle!                     
                      """)
                    weapon_swap("Blaster Rifle", 4, 2)
                if ship == "broken":
                   print("""
If your ship was functioning, you could restart the ship and pilot your way out of here, but as of
now, its still broken.                          
                   """)
                elif ship == "fixed":
                    print("""
The ship is fixed! You can pilot your way home from here!                          
                    """)
                    done = input("Are you ready to go home: ")
                    if "yes" in done.lower():
                        cleared = 1
                        return 'finished'
                    else:
                        print("Alright finish up then come back here later")
                    
            else:
                notnow()
                
###############################################################################################################################
class Main_body(Scene):
    
    def enter(self):
        global health
        global weapon
        global armed
        print("-" * 65)
        
        if kills[0] == 0:
            print("""
You enter the ships Main Body and come face to face with a terrifying Zhendojan War Beetle
IT CHARGES AT YOU
              """)
            combat(1)
            if lose == 1:
                return 'death'
            elif lose == 2:
                return 'lounge'
            elif lose != 1 and lose != 2:
                kills[0] = 1
        else:
            print("You enter the darkness of the Main Body")
        
        cleared = 0
        
        while cleared == 0:
            print("-" * 65)
            print("""
You take stock of your options:
            1. Go into the Central Corridor
            2. Go into the Med Bay
            3. Go into the Bridge
            4. Go into the Mess Hall
            5. Look around the Main Body
              """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                transition("Med Bay")
                return 'med_bay'
            elif choice == 3:
                transition("Bridge")
                return 'bridge'
            elif choice == 4:
                transition("Mess Hall")
                return 'mess_hall'
            elif choice == 5:
                print("""
The Main Body is a Central Area of the ship, but there isnt much here besides doors to more important areas.                       
                      """)
            else:
                notnow()

###############################################################################################################################
class Med_bay(Scene):
    
    def enter(self):
        global health
        global armed
        global weapon
        global ones
        global t_obs
        print("-" * 65)
        print("""
You enter the Med bay to find it empty and dormant.""")
        
        cleared = 0
        setup = 0
        
        while cleared == 0:
            
            if setup == 0:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Med Bay
            2. Go to the Main Body
            3. Go to the Science Labs
            4. Go to the Central Corridor                  
                      """)
            elif setup == 1 and ones[3] == 0 and ones[8] == 0:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Med Bay
            2. Go to the Main Body
            3. Go to the Science Labs
            4. Go to the Central Corridor
            5. Read the Ships Manual
            6. Use the Medijector
            7. Pick up the Scalpel                  
                      """)
            elif setup == 1 and ones[3] == 1 and ones[8] == 0:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Med Bay
            2. Go to the Main Body
            3. Go to the Science Labs
            4. Go to the Central Corridor
            5. Read the Ships Manual
            6. Use the Medijector                 
                      """)
            elif setup == 1 and ones[3] == 0 and ones[8] == 1:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Med Bay
            2. Go to the Main Body
            3. Go to the Science Labs
            4. Go to the Central Corridor
            5. Read the Ships Manual
            7. Pick up the Scalpel                  
                      """)
            elif setup == 1 and ones[3] == 1 and ones[8] == 1:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Med Bay
            2. Go to the Main Body
            3. Go to the Science Labs
            4. Go to the Central Corridor
            5. Read the Ships Manual               
                      """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                setup = 1
                print("""
The medbay is the ships operating room, emergency room, and doctors office all rolled into one.
In the back corner is the Doctors desk, covered in medical papers, anatomical busts, and equiment.
In the center of the room is a large steel table upon which he performs both surgeries and 
check ups. In the corner opposite his desk are a pair of loveseats and a small coffe table, for anyone
who needs to wait. 

You look around the medbay and see the Medijector sitting on the desk. This could heal you, should
you need it. Hopefully you won't, but you shoudl wait until absolutely necessary as it's a one off
without the Doctor around to operate it. 

There is a copy of the ships manual open on the coffee table in the waiting area. The Doctor appears
to be using it as reading material for his patients. 

On the desk is small glass box with the Doctor's operating equipment, including a small scalpel. It's
small but may be useful in fighting off those ugly things. Scalpels these days cut at the atomic level
and almost never go sharp, they're scary business.

In the corner is a door to the Science Labs. On the wall perpendicular to it is a door to the central 
corridor.                  
                      """)
            elif choice == 2:
                transition("Main Body")
                return 'main_body'
            elif choice == 3:
                transition("Science Labs")
                return 'sci_labs'
            elif choice == 4:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 5:
                t_obs[1] = 1
                print("""
                      The Strong-Man class freighter is equipped with the latest in anti-piracy
                      weaponry and defenses! On the front end of the ship come tow MGX-III heavy
                      ion cannons, designed to designed to shut down the critical systems of an enemy
                      ship to give you escape time. The top and bottom of the ship are both equipped
                      with a single manned turret, capable of swiveling about in order to discourage 
                      a small-single manned fighter from being any real threat (We learned our lesson
                      in the 70's). Finally the rear end of the ship is equipped with a flack cannon
                      that fires shots that explode into a cloud of deadly shrapnell in order to dicourage
                      pursuit. 
                      
                      As if that all wasnt too much already, the hull of the Strong-Man is tested 
                      against military strangth rail guns in order to ensure the maximum amount
                      of protection for your precious cargo. 
                      """)
            elif choice == 6:
                heal(80, 8)
            elif choice == 7:
                weapon_swap("Scalpel", 3, 3)
            else:
                notnow()
                
###############################################################################################################################
class Sci_labs(Scene):
    
    def enter(self):
        global h_obs
        global t_obs
        global l_obs
        print("-" * 65)
        print("""
You enter the Science Lab to find it empty and dormant.""")   
        
        cleared = 0
        setup = 0
        
        while cleared == 0:
            if setup == 0:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Lab
            2. Go to the Med Bay
            3. Go to the Central Corridor                  
                      """)
            elif setup == 1:
                print("-" * 65)
                print("""
You take stock of your options:

            1. Look around the Lab
            2. Go to the Med Bay
            3. Go to the Central Corridor
            4. Read the Report
            5. Read the Ships Manual
            6. Read the 'History of Colonization'
            7. Touch the instruments anyways
                      """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65) 

            if choice == 1:
                setup = 1
                print("""
Many people question why a freighter would have a Science Lab. But people also tend to overestimate 
just how much we know about outer space. In reality, we know nothing, and a well equipped science lab
keeps a ship prepared to deal with the unexpected and the never before encountered. There is a lot of
demand for research into the strangeness of the galaxy, many ships bring hire Science Officers in 
exchange for a cut of their grant money or publication royalties from any papers they write while on
board. This is the case of 'The Resilience'. 

As you look around your Science Lab, you notice that backup power has not activated any of the consoles
in the room. Let's hope the Science Officer remembered to save his work before going to bed last night!

There are a great many printed reports laying about his desks and a lot of complicated scientific
instruments that you'd rather not touch. On a desk to your right, you see a copy of the Ships Manual.
On the desk at the far left wall, you see a report entitled 'The History of Colonization'. On the
main desk you see a report that seems to be recent.

The Science Labs have access to the Med Bay and the Central Corridor.                       
                      """)
            elif choice == 2:
                transition("Med Bay")
                return 'med_bay'
            elif choice == 3:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 4 and setup == 1:
                l_obs[0] = 1
                print("""
                      ----ATMOSPHERIC REPORT: THIRESSA IX----
                      
                      SPECTRUM ANALYSIS:
                      
                          OXYGEN:       3%
                          NITROGEN:    24%
                          HYDROGEN:    12%
                          NEON:        41%
                          ARGON:        2%
                          METHANE:     18%
                          
                          ATMOSPHERIC MASS: 2.12 E 7
                          KARMAN LINE:      70 KM
                      
                      REPORT SUMMARY:
                          
                          ATMOSPHERE INHOSPITABLE
                          COLONIZATION NOT RECOMENDED
                      """)
            elif choice == 5 and setup == 1:
                t_obs[2] = 1
                print("""
                    Your Strong-Man Class freighter comes equipped with some of the most advanced
                    long-range scanners on the market, enabling you to fly your way through dense 
                    nebulae and electromagnetic storms. Given the unpredictable nature of space,
                    we at BLG belive that your safety hinges on staying one step ahead of whatever
                    the frontier can throw at you.
                    
                    USING YOUR MARK VII ELECTROGRAPHIC SCANNERS
                    1.......
                    
                    the page turns to scientific mumbo jumbo that you can't make heads or tails of
                    """)
            elif choice == 6 and setup == 1:
                h_obs[2] = 1
                print("""
                      Colonization began as an attempt to ease trade with the Galminorans. The first
                      UEA colony was on Hyracules XXI, a small moon on a planet roughly halfway between
                      Earth and Galminora. Though this colony proved essential in providing trade 
                      logistics, it did not prove appealing to potential settlers. Life on the frontier 
                      was difficult, and not many people desired to leave the comforts of earth. The 
                      UEA desired more colonies, however, partly in order to reduce overcrowding and
                      resource strain on Earth, but also in order to increase UEA revenues. Colonies
                      are the only territories subject to direct UEA governance and taxation. The UEA
                      offers a variety of so called colonization incentives, and has made a grand 
                      showing of shipping off colonists on big ships with great fanfare, and yet, as 
                      of 2302, no colony has grown beyond 70,000 people. 
                          There is a great deal of mystery surrounding UEA colony numbers, however.
                      Logs appear to be altered multiple times, people appear on logs twice, some people
                      have simply disapeared. Many believe this to be due to beaurocratic mismanagement,
                      in the massive undertaking of shipping thousands of people across the galaxy, 
                      you can expect to miscount once or twice. Others suggest the ammount of miscounting
                      goes beyond simple incompetence, but there has never been any evidence to suggest
                      otherwise. 
                """)
            elif choice == 7 and setup == 1:
                print("""
You flick a switch and push some buttons on what looks to be a high-tech centrufuge. Nothing happens
because the power is out.                      
                """)
            else:
                notnow()
            
        

###############################################################################################################################
class Observation(Scene):
    
    def enter(self):
        global ones
        global h_obs

        cleared = 0
        
        while cleared == 0:
            print("-" * 65)
            print("""
The observation deck is a room on the far edge of the ship, whose sole purpose is to have a big window
for people to look out of. Right now the window is shut, covered by the emergency blast doors that go
up while the power is out, and the room just seems ... pointless. Regardless, you notice a small bust
of a former president that might make a good blunt weapon and a book on Galactic Warfare. 

You take stock of your options:
            
            1. Return to the Central Corridor
            2. Pick up the Small Bust
            3. Read 'Space Warfare'
            4. Remember that time you banged that Green Skinned Hottie in here
                  """)
                
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65) 
            
            if choice == 1:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                weapon_swap('Small Bust', 1, 4)
                if weapon == 'Small Bust':
                    print("Thats what she said")
            elif choice == 3:
                print("""
                      Fortunately for all, the UEA has never been in a military conflict with an
                      alien race. The UEA does not have a large navy, mostly because the few resources
                      remaining on earth are better spent on transports and communication relays, not
                      war vessels that will likey never be used. The UEA does field a large number of
                      marines on every transport, as civilian protection, and does equip almost all ships
                      with weaponry to serve as protection while abroad. 
                          The few warships the UEA does posses are deadly and dangerous machines. The 
                      largest and newest is 'The Jupiter', a massive warship capable of erasing
                      cities at a time, and ripping apart smaller ships with a single shot from one
                      of its two massive railguns. Each of its two signature cannons fires shells the
                      size of tanks, but have never been used in combat. The Jupiter also possess the
                      ability to feild several squadrons fo fighter craft, though such fighter craft
                      have yet to be manufactured, and make hyperspace jumps unaided by relays. 
                          'Such warships are important deterents' say UEA leaders 'not every intergalactic
                      society is as dedicated to peace as the Galminorans'. Despite this, no UEA warship
                      has seen combat, and few marines have ever had a reason to discharge their 
                      rifles.
                      
                      in the margins you see someone tried to write a note but scribbled it out.
                      you can just barely make out:
                           armory 
                          access 
                           code 
                           894~7
                      The fourth number is too obscured to make out
                """)
            elif choice == 4:
                print("Yeah that was hot")
            else:
                notnow()

###############################################################################################################################
class Docking(Scene):
    
    def enter(self):
        global ones
        global health
        global kills
        global l_obs
        global armed
        global weapon
        
        print("-" * 65)
        
        if kills[8] == 0:
            print("""
You enter the Docking Bay and come face to face with a terrifying Zhendojan War Beetle
IT CHARGES AT YOU
              """)
            combat(1)
            if lose == 1:
                return 'death'
            elif lose == 2:
                return 'lounge'
            elif lose != 1 and lose != 2:
                kills[8] = 1
        else:
            print("You enter the Docking Bay")
            
        cleared = 0
        knocks = 0
        
        while cleared == 0:
            print("""
The one Beetle having been dispatched, you can see the access to the Zhendojan ship. The hatch is closed
and locked so you cannot enter it, not that you would want to anyways. It's eerie, how close you are 
to their ship. You can also see a tablet on the floor, dropped by the Beetle gaurding the ship.                
            """)
            print("-" * 65)
            print("""
You take stock of your options:
            1. Return to the Central Corridor
            2. Read the tablet
            3. Knock on the hatch
              """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                l_obs[4] = 1
                print("""
                      jack.gretzik@olympuscollege.edu ------> hoosierdood76@UEA.gov
                
                      Alright, I'm in
                      
                      ------------------------------------------------------------------------------
                      hoosierdood76@UEA.gov ------> jack.gretzik@olympuscollege.edu
                      
                      Don't worry about that, we have you covered. Did I mention this would make you
                      rich? Imagine what Tessa would say about that...
                
                      ------------------------------------------------------------------------------
                      jack.gretzik@olympuscollege.edu ------> hoosierdood76@UEA.gov
                      
                      I dunno, Jimmy. It sounds illegal and dangerous. What exactly happened to 
                      your last crew?
                      
                      Jack Gretzik
                      Associate Proffesor of Physics
                      Olympus College
                
                      ------------------------------------------------------------------------------
                      hoosierdood76@UEA.gov ------> jack.gretzik@olympuscollege.edu
                      
                      Hey Jack, Newman told me you just took a job as the Navigator on board
                      'The Resiliance'. Thats great news for us because we need a new courrier. 
                      Our last ones ... well they're not up for the job anymore. We need this
                      cargo delivered in order to properly support our colonies on the edge of 
                      Klimmt space. Those hairy freaks will tear our colonists apart without
                      some support, but those dumbass Galminorans won't let us declare war on
                      a member of their trade council. I won't burden you with the details of 
                      our solution, just take the cargo to Thiressa IX on the course that follows.
                      DON'T FIGHT BACK, just wait it out pateintly and you'll get picked up at
                      the rendez-vous. THE UEA will graciously cover the costs of your losses, plus
                      some more for 'emotional distress' lol.
                      
                      Message me back if you're interested
                      
                      Jimmy
                """)
            elif choice == 3:
                print("You knock on the hatch")
                print("...")
                if knocks == 0:
                    print("A Zhendojan War Beetle jumps out at you!")
                elif knocks >= 1:
                    print("%s War Beetles jump out and attack you!" %(knocks + 1))
                knocks += 1
                combat(knocks)
                if lose == 1:
                    cleared = 1
                    return 'death'
            else:
                notnow()

###############################################################################################################################
class Security(Scene):
    
    def enter(self):
        global l_obs
        global h_obs
        global health
        global fourth
        print("-" * 65)
        
        cleared = 0
        alarm = 0
        setup = 0
        
        while cleared == 0:
            print("""
You enter the security office. The room is dark and the backup generator has not restored power to 
this room. 
            """)
            print("-" * 65)
            if setup == 0:
                print("""
You take stock of your options:
            
            1. Look around the Security Offices
            2. Return to the Central Corridor
                """)
            elif setup == 1 and alarm < 3:
                print("""
You take stock of your options:
            
            1. Look around the Security Offices
            2. Return to the Central Corridor
            3. Read the Security Dossier
            4. Look at the Map
            5. Try to enter the Armory
                """)
            elif setup == 1 and alarm >= 3:
                print("""
You take stock of your options:
            
            1. Look around the Security Offices
            2. Return to the Central Corridor
            3. Read the Security Dossier
            4. Look at the Map
                """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)         
            
            if choice == 1:
                setup = 1
                print("""
The Security Office is where the only security gaurd on board is set up. From here he can access and
direct all security camera on board, monitor all shipboard sensors and crew vitals, and maintain 
control over the armory, a vault full of weapons designed to be used in case of pirate attack or 
mutiny (both of which happen more often than the UEA likes to admit). 

You can see the Armory door, locked and bolted. It is protected by the only thing in the room that 
is powered by the backup generator: an old keypad. No Biometric scanners on this ship, keypads are 
easier to maintain and fix.

Looking around the rest of the office, you can see his main console, powered down of course, but next
to it is his personal annotaed star chart, and on his desk is a security dossier: a folder containing
his research and assesment of his duties on our mission.                     
                """)
            if choice == 2:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 3:
                l_obs[1] = 1
                print("""
                      MISSION ANALYSIS: SUPPLY RUN TO THIRESSA IX
                      SECURITY OFFICER ALEX O'HANNON
                      
                      My research for this trip has uncovered
                      something...strange. I have found numerous
                      records of flights to Thiressa IX, but these
                      records...many of them are impossible, the 
                      few that seem possible are the same that
                      end in disaster. Pirates, engine failures,
                      LIFE SUPPORT failures - that is odd all
                      on its own, life support is built with so
                      many redundancies to prevent failure but
                      I have found record of SEVEN instances
                      of life support failure on this route
                      alone. Passengers on these trips of misery
                      often wake up on a UEA rescue vessel with 
                      the promise of money in exchange for 
                      an NDA. The voyages that do make it are 
                      just as strange. Almost no passenger 
                      records exist, the few records that do
                      are the same passengers over and over again.
                      And to make matters stranger, all records
                      stop abrubtly, eight years ago, despite
                      the colony being supposedly thirteen years
                      old? No records of establishment voyages,
                      no records of initial backers, no records
                      of TAX COLLECTION on this rock. The only
                      reason the UEA ships people to these things
                      is to bilk them for taxes but there is no
                      record of anyone on Thiressa IX ever paying
                      a cent to the UEA. I have no idea what is 
                      going here but I refuse to ask any more
                      questions. Last thing I need is to uncover
                      a massive conspiracy and get tangled up
                      in the drama that follows. Lets just get 
                      home safely and forget about all this.
                """)
            elif choice == 4:
                h_obs[4] = 1
                print("""
                      -------------------------------------------------------
                      |          \                                /         |
                      |           \        Klimmt Space          /          |
                      |  Edge of   \                            /           |
                      |  Galminoran \                          /  Zhendojan |
                      |  Space       \                        /    Space    |
                      |               \                      /              |
                      |                \____________________/_______________|
                      |                /       o Mandalos     o Thiressa IX |
                      |               /  o Gugato                           |
                      |              /                                      |
                      |             /                 o Shirella            |
                      |            /    o Audeman                           |
                      |           /            UEA Colonial Space           |
                      -------------------------------------------------------
                      """)  
                if l_obs[2] == 0:
                      print("""
You look closely at the security officers map. He has drawn on the zones of 
control of alien races. The Galminorans control the largest area, of course.
The Zhendojan Beetles control an area on the other side of Klimmt Space, 
Klimmt space in turn neighbors many UEA Colonies. Thiressa IX is farther away
from most colonies and much closer to Zhendojan Space than you expected.
If the point is to trade with Galminorans, why colonize over here?
                      """)
                elif l_obs[2] == 1:
                    print("""
You look closely at the security officers map. He has drawn on the zones of 
control of alien races. The Galminorans control the largest area, of course.
The Zhendojan Beetles control an area on the other side of Klimmt Space, 
Klimmt space in turn neighbors many UEA Colonies. Thiressa IX is farther away
from most colonies and much closer to Zhendojan Space than you expected.
 If the point is to trade with Galminorans, why colonize over here?
                      
You remember the navigational chart you pulled from the bridge. Comparing the
two, you notice that the route you take actually takes you to Thiressa IX
from the Zhendojan side of the system! It seems more and more that someone
wanted you to have this encounter.
                    """)
            elif choice == 5:
                print("""
You approach heavily secured door and eye the keypad. You know that this system will lock you out
if you guess incorrectly 4 times in a row, and the only person allowed to have the access code is
the security guard. This is a rule you would regret, if you had time for regrets.                        
                """)
                code = "894" + fourth + "7"
                code_guess = input("Enter the Five Digit Code: ")
                
                while code != code_guess and alarm < 3:
                    alarm += 1
                    print("Nope thats not it")
                    code_guess = input("Enter the Five Digit Code: ")
                
                if alarm == 3:
                    print("You feel a sharp ZAP as the keypad shocks you for getting the code wrong, AGAIN")
                    print("The Door now locks itself down even more, and you realize it will be impossible to get in")
                    if health <= 5:
                        pass
                    else:
                        health -= 5
                    
                if code == code_guess:
                    transition("Armory")
                    return 'armory'
            else:
                notnow()

###############################################################################################################################
class Central_c(Scene):
    
    def enter(self):
        global armed
        global health
        global kills
        global weapon
        
        print("-" * 65)
        if kills[7] == 0:
            print("You enter the Central Corridor to find complete darkness")
            print("Suddenly you feel a WHACK and fall down face first!")
            if health <= 5:
                pass
            else:
                health -= 5
            print("YOU ARE UNDER ATTACK")
            combat(1)
            if lose == 1:
                return 'death'
            elif lose == 2:
                return 'lounge'
            elif lose != 1 and lose != 2:
                kills[7] = 1
        else:
            print("You enter the central Corridor to find complete darkness")
            
        cleared = 0
        
        while cleared == 0:
            print("""
The Central Corridor is the middle-most area of the ship. It runs perpendicular to the bridge and 
connests to more rooms than any other. This, of course makes you more exposed but also gives you more
options. Besides a multitude of doors, the corridor is bare and ununteresting. 

You take stock of your options:
            
            1. Go into the Lounge
            2. Go into the Mess Hall
            3. Go into the Main Body
            4. Go into the Med Bay
            5. Go into the Science Labs
            6. Go onto the Observation Deck
            7. Go into the Security Offices
            8. Go onto the Cargo Hold Catwalk
            9. Go into the Cargo Hold
           10. Try to access the barricaded Crew Quarters
           11. Go into the Docking Bay                
            """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                transition("Lounge")
                return 'lounge'
            elif choice == 2:
                transition("Mess Hall")
                return 'mess_hall'
            elif choice == 3:
                transition("Main Body")
                return 'main_body'
            elif choice == 4:
                transition("Med Bay")
                return 'med_bay'
            elif choice == 5:
                transition("Science Labs")
                return 'sci_labs'
            elif choice == 6:
                transition("Observation Deck")
                return 'observation'
            elif choice == 7:
                transition("Security Offices")
                return 'security'
            elif choice == 8:
                transition("Catwalk")
                return 'catwalk'
            elif choice == 9:
                transition("Cargo Hold Access")
                return 'cargo_a'
            elif choice == 10:
                print("You approach the barricaded door")
                return 'quarter_a'
            elif choice == 11:
                transition("Docking Bay")
                return 'docking'
            else:
                notnow()
            
###############################################################################################################################
class Armory(Scene):
    
    def enter(self):
        global health
        global armed
        global ones
        global weapon
        
        print("-" * 65)
        
        print("""
The armory is surprisingly bare, but to you its a dream come true. There are blaster rifles mounted 
on all the walls and even a medipack on the table in the back. In the center of the room stands your
pride and joy. A BLG Exo-Suit. Designed to fend off atackers in space, underwater, or in any environment
you could possible find yourself in, this suit should be more than enough to fend off the attackers.              
        """)
        
        cleared = 0
        
        while cleared == 0:
            if ones[5] == 0 and ones[9] == 0:
                print("""
You take stock of your options:

            1. Pick up a Blaster Rifle
            2. Return to the Security Offices
            3. Put on the Exo-Suit
            4. Use the Medipack                  
                """)
            elif ones[5] == 1 and ones[9] == 0:
                print("""
You take stock of your options:

            1. Pick up a Blaster Rifle
            2. Return to the Security Offices
            4. Use the Medipack                  
                """)                
            elif ones[5] == 0 and ones[9] == 1:
                print("""
You take stock of your options:

            1. Pick up a Blaster Rifle
            2. Return to the Security Offices
            3. Put on the Exo-Suit                 
                """)
            elif ones[5] == 1 and ones[9] == 1:
                print("""
You take stock of your options:

            1. Pick up a Blaster Rifle
            2. Return to the Security Offices                
                """)
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                weapon_swap("Blaster Rifle", 4, 2)
            elif choice == 2:
                transition("Security Offices")
                return 'security'
            elif choice == 3 and ones[5] == 0:
                weapon_swap("Exo-Suit", 5, 5)
            elif choice == 4 and ones[9] == 0:
                heal(70, 9)
            else:
                notnow()

###############################################################################################################################
class Cargo_a(Scene):
    
    def enter(self):
        global armed
        global ones
        global weapon
        
        print("-" * 65)
        
        cleared = 0
        
        print("""
You enter the access halway for the Cargo Hold. There is nothing too interesting in here. You do see
your engineers toolbox, full of heavy metal tools.""")
        
        while cleared == 0:
            print("""
You take stock of your options:

            1. Return to the Central Corridor
            2. Proceed to the Cargo Hold
            3. Pick up a heavy tool from the toolbox                  
            """)
                
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
           
            if choice == 1:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                transition("Cargo Hold")
                return 'cargo_h'
            elif choice == 3:
               weapon_swap("Heavy Tool", 1, 7)
               if weapon == "Heavy Tool":
                   print("Thats what she said")
            else:
                notnow()

###############################################################################################################################
class Cargo_h(Scene):
    
    def enter(self):
        global h_obs
        global l_obs
        global kills
        global armed
        global health
        global ones
        
        print("-" * 65)
        if kills[3] == 0 or kills[4] == 0:
            print("You are ambushed by two Zhendojan War Beetles!")
            combat(2)
            if lose == 1:
                return 'death'
            elif lose == 2:
                return 'lounge'
            elif lose != 1 and lose != 2:
                kills[3] = 1
                kills[4] = 1
        elif kills[3] == 1 and kills[4] == 1:
            print("You enter the Cargo Hold")
                
        setup = 0
        cleared = 0
        
        while cleared == 0:
            print("-" * 65)
            if setup == 0:
                print("""
You take stock of your options:

            1. Return to the Central Corridor
            2. Look around the Cargo Hold                     
                """)
            if setup == 1 and ones[6] == 0 and ones[10] == 0:
                print(""""
You take stock of your options:

            1. Return to the Central Corridor
            2. Look around the Cargo Hold
            3. Take a closer look at your cargo
            4. Read the newspaper
            5. Pick up the Axe
            6. Use the Medipack                     
                """)  
            elif setup == 1 and ones[6] == 1 and ones[10] == 0:
                print(""""
You take stock of your options:

            1. Return to the Central Corridor
            2. Look around the Cargo Hold
            3. Take a closer look at your cargo
            4. Read the newspaper
            6. Use the Medipack                     
                """) 
            elif setup == 1 and ones[6] == 0 and ones[10] == 1:
                print(""""
You take stock of your options:

            1. Return to the Central Corridor
            2. Look around the Cargo Hold
            3. Take a closer look at your cargo
            4. Read the newspaper
            5. Pick up the Axe                    
                """) 
            elif setup == 1 and ones[6] == 1 and ones[10] == 1:
                print(""""
You take stock of your options:

            1. Return to the Central Corridor
            2. Look around the Cargo Hold
            3. Take a closer look at your cargo
            4. Read the newspaper                    
                """) 
                    
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                transition("Cargo Access")
                return 'cargo_a'
            elif choice == 2:
                setup = 1
                print("""
The Cargo Hold is the largest room on the ship, taking up the entire lower floor. It is full of crates
and boxes and containers, all of which are currently destined for Thiressa IX. 

There is a newspaper on the desk in the corner and an axe hanging on the wall. Finally you notice a
medipack on ground next a beetle.                       
                """)
            elif choice == 3:
                l_obs[3] == 1
                print("""
You approach the nearerest crate and use your %s top open it. To your surprise you don't find food
or fertilizer or clothes or anything that you would expect colonists to need, but instead contains
weapons! Shocked, you move to another one and pry off the lid, this ones is full of money! Inside this
container is an envelope bearing the official UEA seal.

                      Here is shipment 11. The Klimmt have been massing near Mandalos again, if we
                      lose more colonists, our colonies will never fully get off the ground. You have
                      been very successful in keeping them off our backs. Take this ship to the 
                      coordinates below for rescue but the cargo is yours.   
                      
                      RESCUE COORDINATES: 57815  16278  93214
                """ %weapon)
            elif choice == 4:
                h_obs = 1
                print("""
                      The fourth annual Galminoran peace summit was this past weekend in Gallian City.
                      The summit is the Galminorans attempt to foster a peaceful solution to the war
                      and aggression between the Zhendojans and the Klimmt, who have been warring over
                      a border dispute for the past eight years. The war, which came on suddenly, but
                      not surprisingly between the two warlike cultures, has resisted all attempts for
                      a brokerage of peace. This has not stopped Galminorans from trying; the peace-
                      loving aliens have hosted this confference every year proposing grander peace
                      incentives, but both parties consistently turn them down. This year was no 
                      different as Zhendojans walked out of the negotiations after fifteen minutes
                      of what would be considered small talk. A crushing blow to the Galminorans.
                """)
            elif choice == 5:
                weapon_swap("Axe", 3, 6)
            elif choice == 6:
                heal(50, 10)
            else:
                notnow()

###############################################################################################################################
class Catwalk(Scene):
    
    def enter(self):
        global health
        global armed
        print("-" * 65)
        
        if kills[5] == 0:
            print("You walk out onto the catwalk and see two Zhendojan Beetles standing guard over the Engine Room")
            print("You will have to attack them to get in")
            print("Would you like to attack?")

            atk = int(input("1 = Yes, 2 = No: "))
            if atk == 1:
                combat(2)
                if lose == 1:
                    return 'death'
                elif lose == 2:
                    return 'lounge'
                elif lose != 1 and lose != 2:
                    kills[5] = 1
                    kills[6] = 1
            elif atk == 2:
                transition("Central Corridor")
                return 'central_c'
            else:
                notnow()
        elif kills[5] == 1 and kills[6] == 1:
            print("You walk onto the catwalk overlooking the Cargo Hold")

        cleared = 0
            
        while cleared == 0:
            print("-" * 65)
            print("""
You take stock of your options:

            1. Return to the Central Corridor
            2. Proceed into the Engine Room                  
            """)
            
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                transition("Central Corridor")
                return 'central_c'
            elif choice == 2:
                transition("Engine Room")
                return 'eng_room'
            else:
                notnow()
                
###############################################################################################################################
class Eng_room(Scene):
     
    def enter(self):
        global health
        global weapon
        global armed
        global t_obs
        global ship
        global kills
        
        if sum(kills[9:12]) == 0: 
            print("""
You enter the Engine Room and are greeted by 3 War Beetles. They seen to be investigating your engine,
but when you come in they move to attack!                  
            """)
            combat(3)
            if lose == 1:
                return 'death'
            elif lose == 2:
                return 'lounge'
            elif lose != 1 and lose != 2:
                kills[9:12] = [1,1,1]
        elif sum(kills[9:12]) == 3:
            print("""
You enter the engine room and take a look around.                  
            """)
            
        cleared = 0
        setup = 0
        
        while cleared == 0:
            print("-" * 65)
            if setup == 0:
                print("""
You take stock of your options:
            
            1. Return to the Catwalk
            2. Take a look around the Engine Room                      
                """)
            elif setup == 1:
                print("""
You take stock of your options:
               
            1. Return to the Catwalk
            2. Take a look around the Engine Room
            3. Read the Ships Manual
            4. Repair the Engine                   
                """)
                        
            choice = int(input("Pick the number of your choice > "))
            print("-" * 65)
            
            if choice == 1:
                transition("Catwalk")
                return 'catwalk'
            elif choice == 2:
                setup = 1
                print("""
The engine room is full of panels and tubes and pipes that make the ship move. Its all very complicated
and at the same time, simple. You see where the Zhendojans cut through into the engine to diable the power.
It should be easy enough to fix, at least to get the engines back online. You can also see a cop of the
ships manual in the corner, that should assist you with some of the repairs, should you need it.                      
                """)
            elif choice == 3:
                t_obs[3] = 1
                print("""
                      The Engine of your Strong-Man class frighter is one of a kind! Its been specially
                      developed to be able to pull, push, or haul an exceptional ammount of weight
                      through warp space, while simultaneously being so easy to repair and maintain
                      that you could do it with half the crew of a much smaller star ship. The secret
                      lies in BLG's pattented tripple burn technology which makes the engine burn
                      ......
                      
                      at this point it turns into engineer babble and you cant understand a word
                """)
            elif choice == 4:
                ship = "fixed"
                print("""
After investing some time, you manage to get the engine working. Its not enough to restore primary
power but it is enough to get you the hell home! You should make your way to the bridge. Its through
the ships main body, and will be where you can pilot everyone to safety.                      
                """)
            else:
                notnow()
        
###############################################################################################################################
class Quarter_a(Scene):
    
    def enter(self):
        print("-" * 65)
        print("""
You approach the quarters access but cant get to close. There is a mangled peice of metal sitting in 
the way and the door looks like it was melted shut. There is no way your crew is getting out of there.

You can hear them pounding on the upstairs door, trying to het into the stairwell, but they're still
too far away to get a message to. Looks like you're on your own.              
        """)
        return 'central_c'

###############################################################################################################################
class Finished(Scene):
    
    def enter(self):
        
        score = ((sum(h_obs) + sum(l_obs) + sum(t_obs) + sum(kills) + armed + health) * 50) + 1400
        score_pct = round(((score / 8000) * 100), 4)
        print("-" * 65)
        print("""
Congratulations on winnig the game! 
You got a score of %d, which is completion of %s!
I hope you had fun!               
        """ %(score, score_pct))
        print("-" * 65)
        
        return 'finished'

###############################################################################################################################
class Map(object):
    
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
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

###############################################################################################################################
a_map = Map('lounge')
a_game = Engine(a_map)
a_game.play()       