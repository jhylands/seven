from visugraph import print_graph
from seven import thinker, thinkmaker

def test_print_graph():
    thing_thought = thinkmaker("thing", "compare", "compare_result")
    out = print_graph(thing_thought)
    assert out.replace(" ","").replace("\n", "") == "thingcomparecompare_result"
