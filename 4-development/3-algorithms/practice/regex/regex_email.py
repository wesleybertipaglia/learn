import re

pattern = r'[a-zA-Z0-9]+[@]+[a-zA-Z0-9]+[\.]+[a-zA-Z]' # letters or numbers + @ + letters + . + letters

def test_pettern(test):
    valid = re.match(pattern, test) is not None
    print(f'{test}: is {"valid" if valid else "invalid"}')

# test cases
test_pettern('bdeblasio0@ebay.com')
test_pettern('sdinsale1@nyu.edu')
test_pettern('bblanket2@askcom')
test_pettern('bblanket2ask.com')
