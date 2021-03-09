from seven import thinker
def print_graph(thinker, width=40):
    # type: (thinker)->str
    acc = []
    source = thinker.source
    source_comparison = thinker.source_comparison
    acc.append(source + " " * (width- len(source) - len(source_comparison)) + source_comparison)
    acc.append(thinker.relation)
    acc.append(" " * (width-len(thinker.relation_comparison)) + thinker.relation_comparison)
    target = thinker.target
    target_comparison = thinker.target_comparison
    acc.append(target + " " * (width- len(target) - len(target_comparison)) + target_comparison)
    return "\n".join(acc)

def main():
    """
    A main look that allows for graph creation and editing.
    This should allow for the user to input items and relations
    -------------------------
    The purpose here is to be able to work out how the network should
    progress of its own accord
    """
    commmand = input(">")
    
