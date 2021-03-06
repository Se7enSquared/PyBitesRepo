names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
   """Outputs:
      1. Julian     Australia
      2. Bob        Spain
      3. PyBites    Global
      4. Dante      Argentina
      5. Martin     USA
      6. Rodolfo    Mexico"""
   for i in range(0, len(names)):
      print(f'{i+1}. {names[i]: <10} {countries[i]}')

enumerate_names_countries()
