from functools import partial

rounder_int =  partial(round, ndigits=0)
rounder_detailed =  partial(round, ndigits=4)