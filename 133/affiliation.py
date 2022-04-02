def generate_affiliation_link(url):
    first_part = 'http://www.amazon.com/dp/'
    last_part = '/?tag=pyb0f-20'
    first_delim = url.index('/dp/') + len('/dp/')
    get_middle = url[first_delim:]
    try:
        last_delim = get_middle.index('/')
    except:
        return first_part + get_middle + last_part
    else:
        middle_part = get_middle[:last_delim]
        return first_part + middle_part + last_part

generate_affiliation_link('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/1449340377/')