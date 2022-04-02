def uncommon_cities(my_cities, other_cities):
   """Compare my_cities and other_cities and return the number of different
      cities between the two"""
   my_unique = list(set(my_cities) - set(other_cities))
   other_unique = list(set(other_cities) - set(my_cities))
   return len(my_unique) + len(other_unique)