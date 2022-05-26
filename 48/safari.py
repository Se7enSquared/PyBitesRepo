import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)

def create_chart():
    current_date = ''
    with open(SAFARI_LOGS) as f:
        data = f.readlines()
        for i, line in enumerate(data):
            line_date = data[i].split(' ')[0]
            if line_date != current_date:
                print()
                current_date = line_date
                print(current_date, end=' ')
            if 'slack' in line:
                if 'python' in data[i-1] or 'Python' in data[i-1]:
                    print('🐍', end='')
                else:
                    print('.', end='')
