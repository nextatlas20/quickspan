"""QuickSpan - candidate span proposal for annotation queues."""

def candidates(tokens, tags, min_len=2):
    """Group consecutive tagged tokens into candidate spans."""
    spans, start = [], None
    for i, tag in enumerate(tags):
        if tag != "O" and start is None:
            start = i
        elif tag == "O" and start is not None:
            if i - start >= min_len:
                spans.append((start, i, " ".join(tokens[start:i])))
            start = None
    return spans
