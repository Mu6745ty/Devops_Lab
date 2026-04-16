# 1. Import module
import calculator


# 2. Test add function
def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0
    print("test_add PASSED")


# 3. Test subtract function
def test_subtract():
    assert calculator.subtract(10, 3) == 7
    assert calculator.subtract(0, 5) == -5
    print("test_subtract PASSED")


# 4. Test multiply function
def test_multiply():
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10
    print("test_multiply PASSED")


# 5. Test divide function
def test_divide():
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(7, 2) == 3.5
    print("test_divide PASSED")


# 6. Main execution block
if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()

    print("\nAll tests PASSED!")
