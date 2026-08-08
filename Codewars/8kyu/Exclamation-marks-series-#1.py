def remove(s):
    listik=list(s)
    try:
        if listik[-1] is "!":
            del listik[-1]
        return "".join(listik)
    except IndexError:
        return "".join(listik)
