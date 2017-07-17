# Basic Object-Oriented Analysis and Design

# I'm going to describe a process to use when you want to build something using Python,
# specifically with object-oriented programming (OOP).

# The process is as follows:
# 1. Write or draw about the problem.
# 2. Extract key concepts from 1 and research them.
# 3. Create a class hierarchy and object map for the concepts.
# 4. Code the classes and a test to run them.
# 5. Repeat and refine.

# The way to look at this process is that it is "top down,"
# meaning it starts from the very abstract loose idea and then slowly refines it
# until the idea is solid and something you can code.

# Then I go through these notes, drawings, and descriptions,
# and I pull out the key concepts.
# There's a simple trick to doing this:
# Simply make a list of all the nouns and verbs in your writing and drawings,
# then write out how they're related.
# This gives me a good list of names for classes, objects, and functions in the next step.

# You can usually take your list of nouns and start asking
# "Is this one like other concept nouns?
# That means they have a common parent class, so what is it called?"
# Keep doing this until you have a class hierarchy that's just a simple tree list or a diagram.
# Then take the verbs you have and see if those are function names for each class and put them in your tree.

# With this class hierarchy figured out, I sit down and write some basic skeleton code that has just the classes,
# their functions, and nothing more.
# I then write a test that runs this code and makes sure the classes I've made make sense and work right.

# The Analysis of a Simple Game Engine

# 1. Write or Draw About the Problem

# I'm going to write a little paragraph for the game:

# "Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them
# so he can escape into an escape pod to the planet below.
# The game will be more like a Zork or Adventure type game with text outputs and funny ways to die.
# The game will involve an engine that runs a map full of rooms or scenes.
# Each room will print its own description when the player enters it
# and then tell the engine what room to run next out of the map."

# Now I want to describe each scene:
# Death
# This is when the player dies and should be something funny.

# Central Corridor
# This is the starting point and has a Gothon already standing there that the players have to defeat with a joke before continuing.

# Laser Weapon Armory
# This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad the hero has to guess the number for.

# The Bridge
# Another battle scene with a Gothon where the hero places the bomb.

# Escape Pod
# Where the hero escapes but only after guessing the right escape pod.

# 2. Extract Key Concepts and Research Them

# I now have enough information to extract some of the nouns and analyze their class hierarchy.
# First I make a list of all the nouns:
# Alien
# Player
# Ship
# Maze
# Room
# Scene
# Gothon
# Escape Pod
# Planet
# Map
# Engine
# Death
# Central Corridor
# Laser Weapon Armory
# The Bridge

# 3. Create a Class Hierarchy and Object Map for the Concepts

# Once I have that I turn it into a class hierarchy by asking
# "What is similar to other things?"
# I also ask "What is basically just another word for another thing?"

# Right away I see that "Room" and "Scene" are basically the same thing depending on how I want to do things.
# I'm going to pick "Scene" for this game.
# Then I see that all the specific rooms like "Central Corridor" are basically just Scenes.
# I see also that Death is basically a Scene, which confirms my choice of "Scene" over "Room" since you can have a death scene, but a death room is kind of odd.
# "Maze" and "Map" are basically the same so I'm going to go with "Map" since I used it more often.
# I don't want to do a battle system, so I'm going to ignore "Alien" and "Player" and save that for later.
# The "Planet" could also just be another scene instead of something specific.

# * Map
# * Engine
# * Scene
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

# I would then go through and figure out what actions are needed on each thing based on verbs in the description.
# For example, I know from the description
#   I'm going to need a way to "run" the engine,
#   "get the next scene" from the map,
#   get the "opening scene,"
#   and "enter" a scene.
# I'll add those like this:

# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

# Notice how I just put -enter under Scene
# since I know that all the scenes under it will inherit it
# and have to override it later.

# 4. Code the Classes and a Test to Run Them

# Once I have this tree of classes and some of the functions
# I open up a source file in my editor and try to write the code for it.

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

# 5. Repeat and Refine

# The last step in my little process isn't so much a step as it is a while-loop.
# You don't ever do this as a one-pass operation.
# Instead you go back over the whole process again
# and refine it based on information you've learned from later steps.

# Top Down versus Bottom Up

# The process is typically labeled "top down" since it starts at the most abstract concepts (the top)
# and works its way down to actual implementation.

# The other way is labeled "bottom up."
# Here are the general steps you follow to do this:

# 1. Take a small piece of the problem; hack on some code and get it to run barely.
# 2. Refine the code into something more formal with classes and automated tests.
# 3. Extract the key concepts you're using and try to find research for them.
# 4. Write a description of what's really going on.
# 5. Go back and refine the code, possibly throwing it out and starting over.
# 6. Repeat, moving on to some other piece of the problem.

# I find this process is better once you're more solid at programming and are naturally thinking in code about problems.
# This process is very good when you know small pieces of the overall puzzle, but maybe don't have enough information yet about the overall concept.
# Breaking it down in little pieces and exploring with code then helps you slowly grind away at the problem until you've solved it.