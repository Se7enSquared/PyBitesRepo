import itertools

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
    lines/words/chars, and returns a string of these numbers + file, e.g.:
    3 12 60 /tmp/somefile
    (both tabs and spaces are allowed as separator)"""
    file_name = ''
    words = []
    chars = []
    lines = ''
    with open(file_, 'r') as f:
        chars = f.read()
        lines = chars.splitlines()
        for line in lines:
            words.append(line.split())
        words = list(itertools.chain(*words))
        file_name = str(f.name).split('\\')[-1]
    return f'{len(lines)}\t{len(words)}\t{len(chars)}\t{file_name}'

if __name__ == "__main__":
    # make it work from cli like original unix wc
    import sys
