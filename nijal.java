```python
class Calculator:
    def __init__(self):
        self._a = 0
        self._b = 0

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an integer or float")
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an integer or float")
        self._b = value

    def display_sum(self):
        print(self._a + self._b)
    
    def multiply(self):
        return self._a * self._b

if __name__ == "__main__":
    calculator_instance = Calculator()
    calculator_instance.a = 1
    calculator_instance.b = 0
    calculator_instance.display_sum()
    print(calculator_instance.multiply())
```