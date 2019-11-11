from nose.tools import *
from gothonweb.planisphere import * #Room # from gothonweb.planisphere import Room

# The set of tests that are functions starting with _test. Inside each test
# case there's a bit of code that makes a room or a set of rooms, then makes
# sure the room work the way you expect them to work. It tests out the basic
# room features, then the paths, then tries out a whole map.

# The important functions here are assert_equal, which makes sure that the
# variables you have to set or paths you have built in a Room are actually
# what you think they are. If you get wrong result, the nosetest will print
# out an error message sou can go figure it out.

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a door to
                the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go wet and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)

    room = start_room.go('tell a joke')
    assert_equal(room, laser_weapon_armory)

# TODO: To complete the map and make the automated test completely validate
# the whole map. This includes fixing all the generic_death objects to be
# real endings.