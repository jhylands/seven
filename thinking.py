from collections import namedtuple
from enum import Enum

class Thought:
    def __repr__(self):
        return "Thought"

class NonThought(Thought):
    def __eq__(self, other):
        if isinstance(other, NonThought):
            return True
        elif isinstance(other, Thought):
            return False
        else:
            return False
            raise Exception("Not comparable types! {} {}".format(type(self), type(other)))

    # Some kind of singleton pattern needed so there is only one way to not think
    def __repr__(self):
        #overwrite the parent 
        return "NonThought"

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
        source = self[ThoughtPosition.SOURCE]
        source_comparison = self[ThoughtPosition.SOURCE_COMPARISON]
        acc.append(source + " " * (width- len(source) - len(source_comparison)) + source_comparison)
        acc.append(self[ThoughtPosition.RELATION])
        acc.append(" " * (width-len(self[ThoughtPosition.RELATION_COMPARISON])) + self[ThoughtPosition.RELATION_COMPARISON])
        target = self[ThoughtPosition.TARGET]
        target_comparison = self[ThoughtPosition.TARGET_COMPARISON]
        acc.append(target + " " * (width- len(target) - len(target_comparison)) + target_comparison)
        return "\n".join(acc)


    def __repr__(self):
        return self.print_graph()
