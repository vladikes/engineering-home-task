# Field Designer

This program attempts to design a battlefield for different types of ships, and to hold the ship state for further developments.

### Walkthrough

A general Walkthrough of the different functionalities

* `field.py`: This module is responsible for the field range creation
* `fleet.py`: This module is responsible to hold the state of the ships such as their type and position in a dataclass
* `battleship.py`: The class is responsible for the battleship creation as well as checkups
* `main.py`: This is where the magic of battleship happens, the creation and configuration

### Instructions:

Run the main.py file by typing python(version number) main.py

That should run and generate the ships and the field.

It works as follows:

battlefield and fleet properties are created within a dict.

field class is initiated with the design.field method that accepts width and height.

Then the different types of ships can be instantiated from within the Battleship class and stored within the fleet_inventory dataclass

an example of an output:

Fleet(Ships=[Ship(type='submarine', direction=None, position=[2, 4], length=1), Ship(type='cruiser', direction='horizontal', position=[4, 5], length=3), Ship(type='destroyer', direction='horizontal', position=[8, 5], length=2), Ship(type='carrier', direction='vertical', position=[3, 7], length=4)])
['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '~', '~', '~', '~', '~', '~', '~']
['~', '~', '#', '~', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '~', '#', '#', '#', '~', '#', '#']
['~', '~', '~', '#', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '#', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '#', '~', '~', '~', '~', '~', '~']
['~', '~', '~', '#', '~', '~', '~', '~', '~', '~']

