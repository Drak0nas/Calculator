from calculator import add, subtract, multiply, divide

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(5, 3) == 2

def test_multiply():
	assert multiply(4, 3) == 12

def test_divide_uneven():
	#Arrange
	a, b = 6, 4
	#Act
	result = divide(a, b)
	#Assert
	assert result == 1.5

def test_subtract_negative():
	#Arrange
	a, b = -6, -7
	#Act
	result = subtract(a, b)
	#Assert
	assert result == 1

def test_multiply_zero():
	a, b = 999, 0
	result = multiply(a, b)
	assert result == 0

def test_add_negative():
	a, b = -99, -1
	result = add(a, b)
	assert result == -100
