class Vector3():
    """Represents a 3D vector with x, y, and z components.

    Attributes:
        _x (int): The x-component of the vector.
        _y (int): The y-component of the vector.
        _z (int): The z-component of the vector.
    """
    def __init__(self, x:int = 0, y:int = 0, z:int = 0):
        """
        Initializes a Vector3 object.

        Args:
            x (int): The x-component of the vector. Defaults to 0.
            y (int): The y-component of the vector. Defaults to 0.
            z (int): The z-component of the vector. Defaults to 0.
        """
        self._x = x
        self._y = y
        self._z = z

    def is_int(self, test_int):
        """
        Checks if a given value is an integer.

        Args:
            test_int: The value to check.

        Returns:
            bool: True if the value is an integer, False otherwise.
        """
        if type(test_int) != int:
            print("not int")
            return False
        return True
    
    def getX(self):
        """
        Returns the x-component of the vector.

        Returns:
            int: The x-component of the vector.
        """
        return self._x
    
    def getY(self):
        """
        Returns the y-component of the vector.

        Returns:
            int: The y-component of the vector.
        """
        return self._y

    def getZ(self):
        """
        Returns the z-component of the vector.

        Returns:
            int: The z-component of the vector.
        """
        return self._z

    def get_value(self):
        """
        Returns the vector as a tuple of (x, y, z) components.

        Returns:
            tuple: A tuple containing the x, y, and z components of the vector.
        """
        return (self._x, self._y, self._z)
    
    def set_value(self, newX:int, newY:int, newZ:int):
        """
        Sets the vector's components to new values.

        Args:
            newX (int): The new x-component.
            newY (int): The new y-component.
            newZ (int): The new z-component.
        """
        self.setX(newX)
        self.setY(newY)
        self.setZ(newZ)

    def setX(self, newX:int):
        """
        Sets the x-component of the vector.

        Args:
            newX (int): The new x-component.
        """
        if not self.is_int(newX):
            return
        self._x = newX

    def setY(self, newY:int):
        """
        Sets the y-component of the vector.

        Args:
            newY (int): The new y-component.
        """
        if not self.is_int(newY):
            return
        self._y = newY

    def setZ(self, newZ:int):
        """
        Sets the z-component of the vector.

        Args:
            newZ (int): The new z-component.
        """
        if not self.is_int(newZ):
            return
        self._z = newZ

    def add(self, vector):
        """
        Adds another Vector3 object to this vector.

        Args:
            vector (Vector3): The Vector3 object to add.

        Returns:
            Vector3: A new Vector3 object representing the sum of the two vectors.
        """
        if not isinstance(vector, Vector3):
            return
        x = self.getX() + vector.getX()
        y = self.getY() + vector.getY()
        z = self.getZ() + vector.getZ()
        return Vector3(x, y, z)

    def differnece(self, vector):
        """
        Subtracts another Vector3 object from this vector.

        Args:
            vector (Vector3): The Vector3 object to subtract.

        Returns:
            Vector3: A new Vector3 object representing the difference of the two vectors.
        """
        if not isinstance(vector, Vector3):
            return
        x = self.getX() - vector.getX()
        y = self.getY() - vector.getY()
        z = self.getZ() - vector.getZ()
        return Vector3(x, y, z)

    def scale(self, scaler:int):
        """
        Scales the vector by a given scalar value.

        Args:
            scaler (int): The scalar value to multiply the vector by.

        Returns:
            Vector3: A new Vector3 object representing the scaled vector.
        """
        if not self.is_int(scaler):
            return
        x = self.getX() * scaler
        y = self.getY() * scaler
        z = self.getZ() * scaler
        return Vector3(x, y, z)

    def quick_magnitude(self):
        """
        Gives magnitude prior to sqrt. For compairing two vectors not for normalization
        """
        x = self.getX()
        y = self.getY()
        z = self.getZ()
        return ((x*x) + (y*y) + (z*z))
    
    def print(self):
        """
        Prints the vector's components to the console.
        """
        print(f"X: {self._x}, Y: {self._y}, Z: {self._z}")