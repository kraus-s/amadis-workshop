from fuzzywuzzy import fuzz
from constants import PREFILTER

def leven_worker(combinations):
    for x,y in combinations:
        leven = fuzz.partial_ratio(x, y)
        if leven > 80:
            yield x, y

def pre_cleaning(book: str) -> str:
    res = book
    for i in PREFILTER:
        if i == "\n":
            res = res.replace(i, " ")
        else:
            res = res.replace(i, "")
    return res