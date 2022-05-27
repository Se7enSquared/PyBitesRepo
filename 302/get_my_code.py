import os
from pathlib import Path
from urllib.request import urlretrieve
import json

filename = "my_code.json"
url = "https://bites-data.s3.us-east-2.amazonaws.com/{filename}"
tmp = Path(os.getenv("TMP", "/tmp"))
json_input_file = tmp / filename

if not json_input_file.exists():
    urlretrieve(url.format(filename=filename), json_input_file)


def get_json_data():
    with open(json_input_file) as file_in:
        return json.load(file_in)

def process_bite_data(bite_data):
    bite_code = bite_data['passing_code']
    bite_title_lst = bite_data['bite'].split(' ')[:2]
    bite_title = ''.join(bite_title_lst).strip('.')

    return bite_code, bite_title

def write_bite(title, code):
    with open(f'{tmp}/{title}.py', 'w') as f:
        f.write(code)

json_data = get_json_data()


def get_passing_code(json_data=json_data):
    """Get all passing code and write the code for each bite to individual files.
       Output file names should be the bite name and number with a .py extension,
       but not including the description.  For example, if the bite name is
       'Bite 124. Marvel data analysis' the output file name should be Bite124.py.
       Remove any/all spaces from the file name.
       Write to /tmp (tmp variable).
    """

    bite1 = json_data['bites'][0]
    bite1_code, bite1_title = process_bite_data(bite1)

    bite2 = json_data['bites'][1]
    bite2_code, bite2_title = process_bite_data(bite2)

    write_bite(bite1_title, bite1_code)
    write_bite(bite2_title, bite2_code)
