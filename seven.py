class knowledge:
    rdf = namedtuple("RDF", ["source", "relation", "target"])
    def __init__(self):
        self.bank = []

    def match(self, pattern):
        # The idea here is that we are abstracting away from 
        # how we are storing the knowledge and instead simply
        # accessing whatever underlying data there is
        pass

    
        

