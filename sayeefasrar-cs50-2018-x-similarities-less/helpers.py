from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    aline_list = a.split("\n")
    bline_list = b.split("\n")

    common_list = {i for i in aline_list if i in bline_list}
    return list(common_list)


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    asent_list = sent_tokenize(a)
    bsent_list = sent_tokenize(b)

    common_list = {i for i in asent_list if i in bsent_list}
    return list(common_list)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    asubs_list = [a[i:i + n] for i in range(len(a)) if len(a[i: i + n]) == n]
    bsubs_list = [b[i:i + n] for i in range(len(b)) if len(b[i: i + n]) == n]

    common_list = {j for j in asubs_list if j in bsubs_list}
    return list(common_list)
