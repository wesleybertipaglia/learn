import re

# registro de identidade (RI) is a brazilian document that substitutes the RG (Registro Geral).

pattern = r'(\d{10})[-](\d{2})' # 0000000000-00

def test_pettern(test):
    valid = re.match(pattern, test) is not None
    print(f'{test}: is {"valid" if valid else "invalid"}')

# test cases
test_pettern('000000000-00')
test_pettern('000000000000')
test_pettern('0000000000-0')
test_pettern('0000000000-00')
