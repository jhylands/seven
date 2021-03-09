from all_thought_generator import set_of_thoughts

def test_set_of_thoughts():
    """
    Currently not working because it doesn't consider
    two identical thoughts to be the same.
    """
    assert len(list(set_of_thoughts())) == 63
