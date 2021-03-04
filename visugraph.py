from seven import thinker
def print_graph(thinker, width=40):
    # type: (thinker)->str
    acc = []
    source = thinker.source
    source_comparison = thinker.source_comparison
    acc.append(source + " " * (width- len(source) - len(source_comparision)) + source_comparision)
    acc.append(thinker.relation)
    acc.append(" " * (width-len(thinker.relation_comparison)) + thinker.relation_comparison)
    target = thinker.target
    target_comparison = thinker.target_comparison
    acc.append(target + " " * (width- len(target) - len(target_comparision)) + target_comparision)
    return "\n".join(acc)
    
