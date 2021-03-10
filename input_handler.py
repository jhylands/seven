import re
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
            

    def parse(self):
        #mv 1, 2
        #mv source source_comparison

        # 1>2
        # source > source_comparison
        mv = re.match(r"mv (\d|\w+) (\d|\w+)", self.command) or re.match(r"(\d|\w+)\s?>\s?(\d|\w+)", self.command)
        if mv:
            source = mv.group(1)
            destination = mv.group(2)
            return self.mv(source, destination)
        

        rm = re.match(r"rm (\d|\w+)", self.command)
        if rm:
            index = rm.group(1)
            return self.rm(index)
        if self.command in ["cmp", "="]:
            raise Exception("Unimplemented")

        focus = re.match(r"(\d|\w+)", self.command)
        if focus:
            raise Exception("Unimplemented")
        raise Exception("Not a valid command")

