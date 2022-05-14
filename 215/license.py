import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    pattern = re.compile('^PB-.{8}-.{8}-.{8}-.{8}$')
    return bool(re.search(pattern, key))
