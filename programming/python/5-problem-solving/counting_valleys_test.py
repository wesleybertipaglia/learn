from counting_valleys import counting_valleys

def assert_counting_valleys(input_path: str, expected_output: int):
    result = counting_valleys(input_path)
    assert result == expected_output, f"Test failed: {input_path} -> {result}, expected {expected_output}"

def test_counting_valleys():
    assert_counting_valleys("UDDDUDUU", 1)
    assert_counting_valleys("DDUUDDUDUUUD", 2)    
