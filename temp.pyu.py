def encode(strs):
    return ''.join(f'{item}:>:>' for item in strs)
"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(str):
    return str.split(':>:>')[:-1]

if __name__ == '__main__':
    str = encode(['lint', 'code', 'love'])
    print(decode(str))