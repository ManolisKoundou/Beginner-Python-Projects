import random


class Pokemon:

    def __init__(self,species, name, type, max_hp, attack, max_stamina, owner):
        self.species = species
        self.name = name
        self.type = type
        self.hp = max_hp
        self.max_hp = max_hp
        self.attack = attack
        self.stamina = max_stamina
        self.max_stamina = max_stamina
        self.owner = owner

    def __str__(self):
        
        return f"Name: {self.name} ({type})"

    def feed(self):

        if self.hp+10 > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += 10

        if self.stamina + 10 > self.max_stamina:
            self.stamina = self.max_stamina
        else:
            self.stamina += 10

        

    
    def weakness(self,type1, type2):

        result = {-1:"Lose",0:"Tie",1:"Win" }
        game_map = {"grass":-1,"water":0,"fire":1}

        #rock-paper-scissors logic 
        matrix = [
            [0,1,-1],# grass
            [-1,0,1],# water
            [1,-1,0],# fire
        ]

    def getCurrentStamina(self):
        return self.stamina

    def getCurrentHp(self):
        return self.hp

    def isDead(self):
        if self.hp == 0:
            return True

        return False

class Battle:

    def __init__(self,player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def __str__(self):
        print(self.player1.__str__())
        print(self.player2.__str__())

    def change_turn(self, player):
        if player is self.player1:
            return self.player2

        return self.player1

    def lost_battle(self,player):
        if self.player.pokemon.isDead():
            return True
        
        return False

    
    
    def attack(self,player1,player2):#pokemon 1 belongs to the player that is being attacked
        attack = str(input(f'{player1.name} Choose Attack: '))
        print(f'{player1.pokemon.species} used {attack}')

        if player1.pokemon.stamina - 5 < 0:
            player1.pokemon.stamina = 0
            print(f'{player1.pokemon.name}s stamina is: {player1.pokemon.getCurrentStamina()}')
        else:
            player1.pokemon.stamina-=5
            print(f'{player1.pokemon.name}s stamina is: {player1.pokemon.getCurrentStamina()}')


        if player2.pokemon.hp - 10 < 0 :
            player2.pokemon.hp = 0
            print(f'{player2.pokemon.name}s HP is: {player2.pokemon.getCurrentHp()}')
        else:
            player2.pokemon.hp -=10
            print(f'{player2.pokemon.name}s HP is: {player2.pokemon.getCurrentHp()}')


    
class Player:

    def __init__(self,name,pokemon):
        self.name = name
        self.pokemon = pokemon

    def __str__(self):
        return f'{self.name} chooses {self.pokemon.species} : {self.pokemon.type}'

   
        




def create_player_and_pokemon():

    pokemon_list = ('bulbasaur', 'charmander', 'torchic', 'blaziken', 'starfish','squirtle', 'pyrohorse', 'ludicolo')

    pokemon = random.choice(pokemon_list)#pokemon of player one 
    pokemon2 = random.choice(pokemon_list)#pokemon of player two 

    name1 = str(input('Please enter the name of first player: '))
    name2 = str(input('\nPlease enter the name of second player: '))

# a bunch of if statements-------------------------------------------------------------------------------------------------------------------------------------------

    if pokemon == 'bulbasaur':
            bulbasaur = Pokemon("Bulbasaur","Bulbi","Grass",100,"Grassy_attack",100,name1)
            player1 = Player(name1,bulbasaur)
    elif pokemon == 'charmander':
            charmander = Pokemon('Charmander','Charmi','Fire',95,'Fireball',105,name1)
            player1 = Player(name1,charmander)
    elif pokemon == 'torchic':
            torchic = Pokemon('Torchic','torchie','Fire',80,'Firefart',80,name1)
            player1 = Player(name1,torchic)
    elif pokemon == 'blaziken':
            blaziken = Pokemon('Blaziken','blaze','Grass',120,'Depressed leaves',90,name1)
            player1 = Player(name1,blaziken)
    elif pokemon == 'starfish':
            starfish = Pokemon('Starfish','Stario','Water',150,'Holy water',150,name1)
            player1 = Player(name1,starfish)
    elif pokemon == 'squirtle':
            squirtle = Pokemon('Squirtle','Squirt','Water',85,'Squirting',90,name1)
            player1 = Player(name1,squirtle)
    elif pokemon == 'pyrohorse':
            pyrohorse = Pokemon('Pyrohorse','Pyro','Fire',110,'Fucking fire',110,name1)
            player1 = Player(name1,pyrohorse)
    else:
            ludicolo = Pokemon('Ludicolo','Ludi','Grass',85,'Horny grass', 85,name1)
            player1 = Player(name1,ludicolo)

# another bunch of if statements-------------------------------------------------------------------------------------------------------------------------------------------


    if pokemon2 == 'bulbasaur':
            bulbasaur = Pokemon("Bulbasaur","Bulbi","Grass",100,"Grassy_attack",100,name2)
            player2 = Player(name2,bulbasaur)
    elif pokemon2 == 'charmander':
            charmander = Pokemon('Charmander','Charmi','Fire',95,'Fireball',105,name2)
            player2 = Player(name2,charmander)
    elif pokemon2 == 'torchic':
            torchic = Pokemon('Torchic','torchie','Fire',80,'Firefart',80,name2)
            player2 = Player(name2,torchic)
    elif pokemon2 == 'blaziken':
            blaziken = Pokemon('Blaziken','blaze','Grass',120,'Depressed leaves',90,name2)
            player2 = Player(name2,blaziken)
    elif pokemon2 == 'starfish':
            starfish = Pokemon('Starfish','Stario','Water',150,'Holy water',150,name2)
            player2 = Player(name2,starfish)
    elif pokemon2 == 'squirtle':
            squirtle = Pokemon('Squirtle','Squirt','Water',85,'Squirting',90,name2)
            player2 = Player(name2,squirtle)
    elif pokemon2 == 'pyrohorse':
            pyrohorse = Pokemon('Pyrohorse','Pyro','Fire',110,'Fucking fire',110,name2)
            player2 = Player(name2,pyrohorse)
    else:
            ludicolo = Pokemon('Ludicolo','Ludi','Grass',85,'Horny grass', 85,name2)
            player2 = Player(name2,ludicolo)

    return player1, player2
        


def main():


    player1,player2 = create_player_and_pokemon()
   
    battle = Battle(player1,player2)

    battle.__str__()

    


    while player1.pokemon.isDead() is not True and player1.pokemon.stamina > 0 and \
        player2.pokemon.isDead() is not True and player2.pokemon.stamina >0:

        
        battle.attack(player1,player2)
        next_attacker = battle.change_turn(player1)
        battle.attack(next_attacker,player1)



    

if __name__ == "__main__":
    main()