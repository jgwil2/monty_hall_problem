import random

class Game(object):
    '''
    A game to be simulated. The game consists of three doors; behind
    one door is a car and behind the other two are goats. The
    contestant picks one door, and then the host, who knows what is
    behind the doors, picks one of the other two doors, which the
    contestant has not picked, and reveals that it has a goat behind it.
    The contestant may now choose to change doors and select the door
    that was initially not picked, or the contestant can stay with the
    initial choice.
    '''
    def __init__(self, contestant):
        size = 3
        self.contestant = contestant
        self.host = Host()
        self.doors = [Door('goat') for i in range(size - 1)]
        self.doors.append(Door('car'))
        random.shuffle(self.doors)

    def play(self):
        self.contestant.makeChoice(self.doors)
        self.host.reveal(self.doors)
        self.contestant.reviseChoice(self.doors)
        for door in self.doors:
            if door.chosen == True and door.prize == 'car':
                return 'win'
        return 'lose'

class Door(object):
    '''
    A door either conceals a car or a goat behind it. A door can be
    chosen by a contestant or not, and revealed by the host or not.
    '''
    def __init__(self, prize):
        self.prize = prize
        self.chosen = False
        self.revealed = False

class Host(object):
    '''
    The gameshow host. The host knows what is behind each door, and
    will reveal a goat at random given certain constraints after the
    contestant has selected a door.
    '''
    def reveal(self, doors):
        possibleDoors = [door for door in doors if door.chosen == False and door.prize != 'car']
        revealedDoor = random.choice(possibleDoors)
        revealedDoor.revealed = True

class Contestant(object):
    '''
    The contestant will randomly choose one door, and after the host
    has revealed a goat will use a strategy to decide whether to change
    choice or not (stay, random, switch).
    '''
    def __init__(self, strategy):
        self.strategy = strategy

    def makeChoice(self, doors):
        choice = doors[random.randint(0, len(doors) - 1)]
        choice.chosen = True

    def reviseChoice(self, doors):
        if self.strategy == 'stay':
            pass
        elif self.strategy == 'random':
            possibleDoors = [door for door in doors if door.revealed == False]
            chosenDoor = random.choice(possibleDoors)
            for door in doors:
                door.chosen = False
            chosenDoor.chosen = True
        elif self.strategy == 'switch':
            possibleDoors = [door for door in doors if door.revealed == False and door.chosen == False]
            chosenDoor = possibleDoors[0]
            for door in doors:
                door.chosen = False
            chosenDoor.chosen = True

def simulate(strategy, number):
    wins = 0
    losses = 0
    for i in range(number):
        contestant = Contestant(strategy)
        game = Game(contestant)
        if game.play() == 'win':
            wins += 1
        else:
            losses += 1

    return wins / (wins + losses)

def main():
    print('Winning Percentage by Strategy (1000 games):')
    print('Stay:  ', simulate('stay', 1000))
    print('Random:', simulate('random', 1000))
    print('Switch:', simulate('switch', 1000))
    print()
    print('Winning Percentage by Strategy (10000 games):')
    print('Stay:  ', simulate('stay', 10000))
    print('Random:', simulate('random', 10000))
    print('Switch:', simulate('switch', 10000))
    print()
    print('Winning Percentage by Strategy (100000 games):')
    print('Stay:  ', simulate('stay', 100000))
    print('Random:', simulate('random', 100000))
    print('Switch:', simulate('switch', 100000))


if __name__ == '__main__':
    main()
