from time_conversion import time_conversion

def assert_time_conversion(input_time: str, expected_output: str):
    result = time_conversion(input_time)
    assert result == expected_output, f"Test failed: {input_time} -> {result}, expected {expected_output}"

def test_time_conversion():
    assert_time_conversion("07:05:45PM", "19:05:45")
    assert_time_conversion("12:00:00AM", "00:00:00")
    assert_time_conversion("12:00:00PM", "12:00:00")
    assert_time_conversion("11:59:59PM", "23:59:59")
    assert_time_conversion("11:59:59AM", "11:59:59")
    assert_time_conversion("01:00:00PM", "13:00:00")
