from repeated_string import repeated_string

def assert_repeated_string(input_clouds: str, repetitions: int, expected_output: int):
    result = repeated_string(input_clouds, repetitions)
    assert result == expected_output, f"Test failed: {input_clouds} -> {result}, expected {expected_output}"

def test_repeated_string():
    assert_repeated_string('aba', 10, 7)
    assert_repeated_string('a', 1000000000000, 1000000000000)
