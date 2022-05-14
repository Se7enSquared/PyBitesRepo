from collections import Counter
import requests

CAR_DATA = "https://bites-data.s3.us-east-2.amazonaws.com/cars.json"

# pre-work: load JSON data into program
with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
    the highest number of new car models"""
    maker_counts = {}
    for entry in data:
        maker = entry['automaker']
        if int(entry["year"]) == year:
            if maker in maker_counts.keys():
                maker_counts[maker] += 1
            else:
                maker_counts[maker] = 1
    return max(maker_counts, key=maker_counts.get)


def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
    return a set of models (a 'set' to avoid duplicate models)"""
    models = []
    for entry in data:
        data_automaker = entry['automaker']
        data_year = entry['year']
        if data_automaker == automaker and int(data_year) == year:
            models.append(entry['model'])
    return set(models)