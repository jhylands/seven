from collections import namedtuple

thinker = namedtuple("Thinker", ["focus", "source", "source_comparison", "target_comparison", "target", "relation", "relation_comparison"])

rdf = namedtuple("RDF", ["source", "relation", "target"])

def thinkmaker(s="", l="", j="", f="", d="", k=""):
    """
    s     l
      d 
        k 
    f     j
    """
    return thinker("", s, l , j, f, d, k)


class knowledge:
    def __init__(self):
        self.bank = []

    def match(self, pattern):
        # The idea here is that we are abstracting away from 
        # how we are storing the knowledge and instead simply
        # accessing whatever underlying data there is
        pass
