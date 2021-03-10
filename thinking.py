from collections import namedtuple
from enum import Enum

class Thought:
    def __init__(self, representation="Thought"):
        self.representation = representation
    def __repr__(self):
        return self.representation

class NonThought(Thought):
    # Some kind of singleton pattern needed so there is only one way to not think

    def __init__(self):
        self.representation = "NonThought"

    def __eq__(self, other):
        if isinstance(other, NonThought):
            return True
        elif isinstance(other, Thought):
            return False
        else:
            return False
            raise Exception("Not comparable types! {} {}".format(type(self), type(other)))


class ThoughtPosition(Enum):
    FOCUS = 0
    SOURCE = 1
    SOURCE_COMPARISON = 2
    TARGET_COMPARISON = 3
    TARGET = 4
    RELATION = 5
    RELATION_COMPARISON = 6

class Thinker:
    think_type = namedtuple("ThinkType", ["focus", "source", "source_comparison", "target_comparison", "target", "relation", "relation_comparison"])

    def __init__(self, *args):
        self.thinker = self.thinkmaker(*args)
        assert self.thinker is not None

    @staticmethod
    def thinkmaker(s=NonThought(), l=NonThought(), j=NonThought(), f=NonThought(), d=NonThought(), k=NonThought()):
        # type: (Thought, Thought, Thought, Thought, Thought, Thought) -> thinker
        """
        s     l
          d 
            k 
        f     j
        """
        return Thinker.think_type(NonThought(), s, l , j, f, d, k)

    def rm(self, index):
        self[index] = NonThought()

    def mv(self, source, destination):
        inflight = self[source]
        self[source] = NonThought()
        self[destination] = inflight

    def mk(self, location, representation):
        self[location] = Thought(representation)

    def cp(self, source, destination):
        cp = self[source]
        self[destination] = cp

    def __getitem__(self, index):
        if isinstance(index, ThoughtPosition):
            index = index.value
        thoughts = list(self.thinker)
        return thoughts[index]
        
    def __setitem__(self, index, value):
        if isinstance(index, ThoughtPosition):
            index = index.value
        thoughts = list(self.thinker)
        thoughts[index] = value
        self.thinker = Thinker.think_type(*thoughts)

    def cmp(self):
        pass

    def print_graph(self, width=40):
        # type: (thinker)->str
        acc = []
        source = str(self[ThoughtPosition.SOURCE])
        source_comparison = str(self[ThoughtPosition.SOURCE_COMPARISON])
        acc.append(source + " " * (width- len(source) - len(source_comparison)) + source_comparison)
        acc.append(str(self[ThoughtPosition.RELATION]))
        relation_comparison = str(self[ThoughtPosition.RELATION_COMPARISON])
        acc.append(" " * (width-len(relation_comparison)) + relation_comparison)
        target = str(self[ThoughtPosition.TARGET])
        target_comparison = str(self[ThoughtPosition.TARGET_COMPARISON])
        acc.append(target + " " * (width- len(target) - len(target_comparison)) + target_comparison)
        return "\n".join(acc)


    def __repr__(self):
        return self.print_graph()
