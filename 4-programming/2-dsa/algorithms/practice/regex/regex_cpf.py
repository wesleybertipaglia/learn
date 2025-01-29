import re

pattern = r'(\d{3})[.](\d{3})[.](\d{3})[-](\d{2})' # 000.000.000-00

def test_pettern(test):
    valid = re.match(pattern, test) is not None
    print(f'{test}: is {"valid" if valid else "invalid"}')

# test cases
test_pettern('000.000.000-00')
test_pettern('000.000.00000')
test_pettern('000.000000-00')
test_pettern('000000.000-00')
