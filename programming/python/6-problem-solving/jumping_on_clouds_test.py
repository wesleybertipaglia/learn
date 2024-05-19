from jumping_on_clouds import jumping_on_clouds

def assert_jumping_on_clouds(input_clouds: list, expected_output: int):
    result = jumping_on_clouds(input_clouds)
    assert result == expected_output, f"Test failed: {input_clouds} -> {result}, expected {expected_output}"

def test_jumping_on_clouds():
    assert_jumping_on_clouds([0, 0, 1, 0, 0, 1, 0], 4)
    assert_jumping_on_clouds([0, 0, 0, 0, 1, 0], 3)
    assert_jumping_on_clouds([0, 0, 0, 1, 0, 0], 3)
    assert_jumping_on_clouds([0, 0, 0, 0, 0, 0], 3)