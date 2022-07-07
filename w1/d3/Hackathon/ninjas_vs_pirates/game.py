from Character import Character
from Character import Ninja
from Character import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()
# jack_sparrow.attack(michelangelo)
# michelangelo.show_stats()
michelangelo.battle(jack_sparrow)