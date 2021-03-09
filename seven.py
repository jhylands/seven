class knowledge:
    def __init__(self):
        self.bank = []

    def match(self, pattern):
        # The idea here is that we are abstracting away from 
        # how we are storing the knowledge and instead simply
        # accessing whatever underlying data there is
        pass

class InputHandler:
    def __init__(self, command):
        self.command = command

    def parse(self):
        pass

def mv_thought(origin, destination):
    def _(thought):
        # type: (thought)->thought
        inflight = thought[origin]
        thought[desintation] = inflight
        thought[origin] = None
        return thought
    return _

def cmp_thought():
    def _(thought):
        # type: (thought)->thought
        
        return thought
    return _

def rm_thought(position):
    def _(thought):
        # type: (thought)->thought
        thought[position] = NonThought()
        return thought
    return _


"""
For this test we want the full enumeration of possible mvs

I can't be doing this right
I'm actually adding ∑i rather than just using the formula
"""
def test_mv_thought():
    pass

def test_cmp_thought():
    pass

"""
Explore your thoughts...
This needs the combination of all the thinkers possible
that is the same sort of thing as the generation of the 
text file where I named them all

75 - 2*6 = 63
"""
def test_rm_thought():
    pass
    
        

"""
One issue we are having here is that we are having to define a whole language
a small language but a whole language all the same.

Here we are progressing along a long list of items it would surly be better
to try and just focus on a single element at a time. If there are longer quries
they can be be worked.

To that end we can move an entity from one place to another.
And we can query/create an entity.
"""
@pytest.mark.parametrize("command, semantics", [
"""
"\d>\d", moving an entity from one place to another
"\d=\d", considering the comparison between two nodes
"=", considering the left right comparison
"c\d", remove the enity from position
# One of the issues here is the type of inferencec
# This, like everything else eventually, will be infered but it'll need to be specific here
"\d", focus on the element, if it doesnt exist try to infer it
"""
])
def test_input_handler(command, thought_in, thought_out):
    handled_input = InputHandler(command)
    handled_input.parse()
    assert handled_input(thought_in) == thought_out
    
