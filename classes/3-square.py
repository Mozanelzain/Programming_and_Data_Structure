class Square:
    """Class Square that defines a square with area calculation"""
    def __init__(self, size=0):
        """Initialize square with optional size
        
        Args:
            size (int, optional): size of the square. Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """Calculate the area of the square
        
        Returns:
            int: The square area
        """
        return self.__size ** 2