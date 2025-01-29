import re

# Registro Geral (RG) is a brazilian document

pattern = r'(\d{2})[\.](\d{3})[\.](\d{3})[-](\d{1})' # 00.000.000-0

def test_pettern(test):
    valid = re.match(pattern, test) is not None
    print(f'{test}: is {"valid" if valid else "invalid"}')

# test cases
test_pettern('0.000.000-0')
test_pettern('00000.000-0')
test_pettern('00.00.000-0')
test_pettern('00.000000-0')
test_pettern('00.000.00-0')
test_pettern('00.000.0000')
test_pettern('00.000.000-')
test_pettern('00.000.000-0')
