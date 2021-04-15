def flatten_list(l: list):
    for el in l:
        if isinstance(el, list):
            yield from flatten_list(el)
        else:
            yield el

def flatten(l: list) -> list:
    return list(flatten_list(l))
