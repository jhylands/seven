from input_handler import InputHandler
from thinking import Thinker
from collections import namedtuple

class knowledge:
    rdf = namedtuple("RDF", ["source", "relation", "target"])
    def __init__(self):
        self.bank = []

    def match(self, pattern):
        # The idea here is that we are abstracting away from 
        # how we are storing the knowledge and instead simply
        # accessing whatever underlying data there is
        pass

    
        

def main():
    """
    A main look that allows for graph creation and editing.
    This should allow for the user to input items and relations
    -------------------------
    The purpose here is to be able to work out how the network should
    progress of its own accord
    """
    exit = False
    thinker = Thinker()
    while not exit:
        print(thinker)
        command = input(">")
        if command == "exit":
            exit = True
        else:
            handler = InputHandler(command)
            handler.parse()(thinker)
            
    print("Bye")

if __name__=="__main__":
    main()
