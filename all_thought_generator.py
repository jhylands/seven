from combinatorics import perm_unique
from thinking import Thought, NonThought, Thinker


def print_range_of_thoughts():
    for i in range(1, 7):
        print("# " , i)
        print("|".join(map(str, range(1, 7))))
        for comb in perm_unique("*"*i + " "*(6-i)):
            print("|".join(comb))


def set_of_thoughts():
    for i in range(1, 7):
        # Using strings not objects here because the equivalence of thoughts
        # is harder to pin down.
        for comb in perm_unique("*"*i + " "*(6-i)):
            yield Thinker(*[Thought() if char=="*" else NonThought() for char in comb])
