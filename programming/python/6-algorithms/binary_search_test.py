from binary_search import binary_search

def assert_binary_search(items: list, target: int, expected_output: int):
    result = binary_search(items, target)
    assert result == expected_output, f"Test failed: list = {items}, target = {target} -> {result}, expected {expected_output}"

def test_binary_search():
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 4)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 9)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 0)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, -1)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, -1)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7, 6)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 1)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 2)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8, 7)
    assert_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 8)