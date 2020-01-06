I want to create a simulation of the [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem)
that I first read about in [The Curious Incident of the Dog in the
Night-Time](https://en.wikipedia.org/wiki/The_Curious_Incident_of_the_Dog_in_the_Night-Time).

I start by defining a number of classes for each object that I want to
represent. The objects in this simulation are Game, Door, Host, and
Contestant. The simulation will work by running a number of games with
randomly generated parameters. The Contestant in each game will follow a
strategy. After running a number of games and recording the results of
following each strategy, we will be able to see what the best strategy
is and the rough probability of winning by following each strategy.

To initialize a game, three doors have to be created: two with goats
and one with a car. These games are stored in a list in random order.
A game is also initialized with a contestant so that each game can be
simulated with a given strategy.

The door is the workhouse object; a door tracks what prize it conceals,
whether or not it has been chosen, and whether or not it has been
revealed (the program doesn't need to be so object-oriented; for
example, the host object is pretty superfluous as its only role is to
reveal an unchosen door with a goat behind it).

The game object has a method play that is invoked to simulate a game.
It creates three doors, including one with a car and two with a goat,
and randomizes their order. It then asks the contestant to choose a
door. The host then reveals a goat behind one door, and the contestant
revises the initial choice according to a strategy. The strategies are
stay (leave the initial choice unchanged), random (choose randomly
between the two doors that do not conceal a goat), and switch (change
the initial choice and choose the door that was not chosen initially
and does not conceal a goat). The play method then reports whether the
contestant has won or lost the game.

The play method can then be run any number of times to test the
effectiveness of each strategy. I currently show the winning percentage
for each strategy after playing 1000, 10,000, and 100,000 times. The
results line up with what we would expect based on the math (see link),
but some may be better able to convince themselves of this result when
seeing empirical evidence.
