def encode(strs):
    encoded_str = ''
    for item in strs:
        encoded_str += item + ':>:>'
    return encoded_str
"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(str):
    return str.split(':>:>')[:-1]

if __name__ == '__main__':
    str = encode(['lint', 'code', 'love'])
    print(decode(str))