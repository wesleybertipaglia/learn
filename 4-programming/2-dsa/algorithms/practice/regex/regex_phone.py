import re

pattern = r'\+([0-9]{2}) \(([0-9]{2,3})\) ([0-9]{3,})-([0-9]{4})' # +00 (000) 000-0000 or +00 (00) 0000-0000 or +00 (00) 00000-0000

def test_pettern(test):
    valid = re.match(pattern, test) is not None
    print(f'{test}: is {"valid" if valid else "invalid"}')

# test cases
test_pettern('+00 (000) 000-0000')
test_pettern('+00 (000) 0000-0000')
test_pettern('+00 (00) 0000-0000')
test_pettern('+00 (00) 00000-0000')
test_pettern('00 (00) 00000-0000')
test_pettern('+0 (00) 00000-0000')
test_pettern('+00 (0) 00000-0000')
test_pettern('+00 (00) 00-0000')
test_pettern('+00 (00) 000-000')
