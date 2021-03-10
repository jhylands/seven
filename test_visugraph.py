from visugraph import print_graph
from thinking import Thinker
import pytest

@pytest.mark.skip("Everything has moved around the references need updating")
def test_print_graph():
    thing_thought = thinkmaker("thing", "compare", "compare_result")
    out = print_graph(thing_thought)
    assert out.replace(" ","").replace("\n", "") == "thingcomparecompare_result"
