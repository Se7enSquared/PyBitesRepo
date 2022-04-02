
def running_mean(sequence):
   """Calculate the running mean of the sequence passed in,
   returns a sequence of same length with the averages.
   You can assume all items in sequence are numeric."""
   lst = []
   sum = 0
   for i in range(len(sequence)):
      sum += sequence[i]
      lst.append(round(sum / (i + 1), 2))
   return lst
