def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} should not contain {1}".format(collection, item)
    
def test_number_is_between(number, low_limit, high_limit):
    assert number >= low_limit and number <= high_limit, "{0} is not in between {1} and {2}".format(number, low_limit, high_limit)