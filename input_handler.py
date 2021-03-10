from thinking import ThoughtPosition, Thought
import re

thought_names = [e.name for e in list(ThoughtPosition)]
"""
One issue we are having here is that we are having to define a whole language
a small language but a whole language all the same.

Here we are progressing along a long list of items it would surly be better
to try and just focus on a single element at a time. If there are longer quires
they can be be worked.

To that end we can move an entity from one place to another.
And we can query/create an entity.
"""
class InputHandler:
    def __init__(self, command):
        self.command = command

    @staticmethod
    def mv(source, destination):
        def mv_function(thinker):
            thinker.mv(source, destination)
        return mv_function

    @staticmethod
    def rm(index):
        def rm_function(thinker):
            thinker.rm(index)
        return rm_function

    @staticmethod
    def to_position(index):
        try:
            return ThoughtPosition(int(index))
        except ValueError:
            if index.upper() in thought_names:
                return getattr(ThoughtPosition, index.upper()) 
            else:
                raise Exception("Index could not be produced for value {}".format(index))


    @staticmethod
    def mk(location, representation):
        def mk_function(thinker):
            thinker.mk(location, representation)
        return mk_function

    @staticmethod
    def cp(source, destination):
        def cp_function(thinker):
            thinker.cp(source, destination)
        return cp_function

    def parse(self):
        #This should be moved to a register based code
        #mv 1, 2
        #mv source source_comparison

        # 1>2
        # source > source_comparison
        mv = re.match(r"mv (\d|\w+) (\d|\w+)", self.command) or re.match(r"(\d|\w+)\s?>\s?(\d|\w+)", self.command)
        if mv:
            source = self.to_position(mv.group(1))
            destination = self.to_position(mv.group(2))
            return self.mv(source, destination)

        cp = re.match(r"cp (\d|\w+) (\d|\w+)", self.command)
        if cp:
            source = self.to_position(cp.group(1))
            destination = self.to_position(cp.group(2))
            return self.cp(source, destination)
        

        rm = re.match(r"rm (\d|\w+)", self.command)
        if rm:
            index = self.to_position(rm.group(1))
            return self.rm(index)
        if self.command in ["cmp", "="]:
            raise Exception("Unimplemented")

        mk = re.match(r"mk (\d|\w+) (.*)", self.command)
        if mk:
            location = self.to_position(mk.group(1))
            representation = mk.group(2)
            return self.mk(location, representation)


        if self.command == "help":
            print("Need to think of a good way to implement this but you can currently use mv, mk, cp, rm")
            return lambda x:x


        focus = re.match(r"(\d|\w+)", self.command)
        if focus:
            # The regex for this is perhaps a little too general 
            raise Exception("Unimplemented")

        raise Exception("Not a valid command")

