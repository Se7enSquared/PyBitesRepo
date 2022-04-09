from collections import defaultdict
from decimal import *

def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    counter = defaultdict(int)

    for letter in sequence:
        counter[letter] += 1

    total_seq = sum(counter.values())
    g_c = sum(v for k, v in counter.items() if k.lower() in ('g', 'c'))
    gc_content = round(Decimal((g_c / total_seq) * 100), 2)

    return gc_content