import calculator


class TestCalculator:

    def test_add(self):

        assert 4 == calculator.add(2, 2)

    def test_subtract(self):

        assert 2 == calculator.subtract(4, 2)
    
    def test_multiplication(self):

        assert 100 == calculator.multiply(10, 10)
