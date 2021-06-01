from sys import exit


class Sequence(object):
    def enter(self):
        exit(1)

class Engine(object): #engine works through map

    def __init__(self, sequence_map):
        self.sequence_map = sequence_map

    def play(self):
    #opening sequence is a_map is-a Engine has-a 'truthtable'
    #initiated in _map = 'truthtable'. object(self)
        current_sequence = self.sequence_map.opening_sequence()
        last_sequence = self.sequence_map.next_sequence("the end")

    #actual engine.
        while current_sequence != last_sequence:
            next_sequence_name = current_sequence.enter()
            current_sequence = self.sequence_map.next_sequence(next_sequence_name)

    #statrts the game from truthtable only.
        current_sequence.enter()

class Map(object):

    sequences = {
            'truth_table': Truthtable(),
            'string_formats': Stringformats(),
            'dict_onary': Dictionary(),
            'phrase_drill': Phrasedrill(),
            'the_end': Theend()
    }

    def __init__(self, start_sequence):
        self.start_sequence = start_sequence

    def next_sequence(self, sequence_name):
        val = Map.sequences.get(sequence_name)
        return val

    def opening_sequence(self):
        return self.next_sequence(self.start_sequence)


a_map = Map('truth_table')
a_game = Engine(a_map)
a_game.play()
