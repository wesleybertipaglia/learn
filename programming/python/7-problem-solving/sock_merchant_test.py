from sock_merchant import sock_merchant

def assert_sock_merchant(input_stock: list, expected_output: int):
    result = sock_merchant(input_stock)
    assert result == expected_output, f"Test failed: {input_stock} -> {result}, expected {expected_output}"

def test_sock_merchant():
    assert_sock_merchant(["Red", "Red"], 1)
    assert_sock_merchant(["Green", "Green", "Green"], 1)
    assert_sock_merchant(["Red", "Red", "Blue", "Blue"], 2)
    assert_sock_merchant(["Red", "Red", "Red", "Green", "Green", "Green", "Blue"], 2)
    assert_sock_merchant(["Red", "Red", "Red", "Red", "Green", "Green", "Green", "Green"], 4)
    assert_sock_merchant([], 0)
    assert_sock_merchant(["Blue", "Blue", "Blue", "Blue"], 2)
    assert_sock_merchant(["Red", "Red", "Blue", "Blue"], 2)
    assert_sock_merchant(["Red"] * 1000 + ["Blue"] * 1000, 1000)
    assert_sock_merchant(["Red", "Red", "Blue", "Green", "Yellow", "Yellow", "Blue", "Red", "Green", "Red"], 5)

