#Jon Williams
#CIS 400 Data Mining
#Assignment 1
#Feb 28th 2021

import random #For later use
#Player Class. Saves Name Race, and Class. 
class Player:
    def __init__(self,name,race,pclass):
        self.name=name
        self.race=race
        self.pclass=pclass
    #Method returns name
    def getName(self):
        return self.name
    #Method returns race.
    def getRace(self):
        return self.race
    #method gets pclass
    def getPclass(self):
        return self.pclass
    #method displays name and race.
    def display(self):
        print(str(player[name] + player[race] + player[pclass]))
#Method to display Racial Options    
def displayRaceOptions():
    print("Select a Race")
    print("1: Azonian")
    print("2: Carcharian")
    print("3: Elf")
    print("4: Kyranian")
    print("5: Imperial")
    print("6: Sinai")
    print()
#Method to display Class Options
def displayClassOptions():
    print("Select a Class")
    print("1: Fighter")
    print("2: Ranger")
    print("3: Warlock")
    print()
#Method to accept user input about creating their character based on the two display functions
def charGen():#Custom races from my Homebrew DnD Game
    name = input("Enter Name: ")
    print()
    race = int(input("Enter Race: "))
    if race == 1:
        race = "Azonian Human"
    elif race == 5:
        race = "Imperial Human"
    elif race == 4:
        race = "Kyranian Human"
    elif race == 2:
        race = "Carcharia"
    elif race == 3:
        race = "Elf"
    elif race == 6:
        race = "Sinai"
    else:
        print("Invalid Selection. Try again.")
        charGen()

    print() #Player Class
    pclass = int(input("Enter Class: "))
    if pclass == 1:
        pclass = "Fighter"
    elif pclass == 2:
        pclass = "Ranger"
    elif pclass == 3:
        pclass = "Warlock"
    else:
        print("Invalid Selection. Try again.")
        charGen()
    print(name) 
    print(race)
    print(pclass)
    return pclass, name, race

#Dictionary of items a player might have
def itemDict():
    itemdict = {
        "Sword" : "Stabber", 
        "Dagger" : "Sticker", 
        "Staff" : "Spell Flinger"
    }
    print("The weapons are:" + str(itemdict)) #Shows the dictionary of weapons
    sword = itemdict.get("Sword") #Gets the sword's name
    print("The sword's name is: " + sword) #Tells us what the sword is named
    print("The staff's name is: " + itemdict.get("Staff")) #Tells us what the staff is named
    print("Lets add a new weapon!") 
    itemdict2 = { 'Bow' : 'Stick Thrower'} #Adds a bow to the weapon dictionary
    print("The new weapon is: " + itemdict2.get("Bow")) #Prints the new weapon's name
    itemdict.update(itemdict2) #Updates the original dictionary with the new key and value
    print(itemdict) 
    print("These are the keys: ")
    print(itemdict.keys()) #prints the keys in the dictionary
    return itemdict, sword

#List of items a player currently has
def itemList():
    fruit = ["apple", "orange", "kiwi"]
    print("The fruit basket has: " + str(fruit))
    newFruit = str(input("Add a new fruit: "))
    items = []
    items.append(newFruit) #Append the user's fruit to the fruit list
    for item in fruit:
        items.append(item) #Put the fruit list into the items list
    print("The fruit list is: " + str(items))

def monster():#A little summoning game. Don't summon the demon!
    print("Monsters are scary!")
    monster = ["Goblin", "Blobfish", "Bigfoot", "Jabberwocky", "Skeleton", "Zombie", "Witch", "Doppleganger", "Dragon", "Bat", "Giant Sewer Rat", "Homunculus"] #Monster Table
    try:
        spell = int(input("Use a number or letter to perform the summoning ritual: ")) #Enter a number, summon a monster
        print("You've summoned a: " + random.choice(monster))
    except:
        print("You've summoned a Demon, oh dear... You are dead!") #Enter a letter, summon a demon and die

#Main     
if __name__ == "__main__":
    displayRaceOptions()
    displayClassOptions()
    player = charGen()
    npc = Player("Ted", "Azonian", "Fighter") #Ted is our Player Class Object
    print("The enemy is:")
    print(npc.getName() + " the " + npc.getRace() + " " + " " + npc.getPclass()) #These are the getter functions from the Class
    print()
    itemDict = itemDict()
    itemList() 
    monster()
    