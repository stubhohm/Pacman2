from ..Vector3.Vector3 import Vector3

class Vector2(Vector3):
    """
    Represents a 2D vector.

    Inherits from Vector3, providing a simplified version for 2D operations.
    """
    def __init__(self, x:int = 0, y:int = 0):
        """
        Initializes a Vector2 object.

        Args:
            x (int): The x-component of the vector. Defaults to 0.
            y (int): The y-component of the vector. Defaults to 0.
        """
        z = 0
        super().__init__(x, y, z)

    def getZ(self) -> None:
        """
        Returns the z-component of the vector.

        Returns:
            int: The z-component of the vector. Always None
        """
        return None
    
    def setZ(self, newZ:int):
        """
        Passes.

        Args:
            newZ (int): The new z-component value.
        """
        pass

    def set_value(self, newX, newY):
        """
        Sets the x and y components of the vector.

        Args:
            newX (int): The new x-component value.
            newY (int): The new y-component value.
        
        Returns:
            Vector2: A new Vector2 object with updated values.
        """
        return super().set_value(newX, newY, 0)
    
    def get_value(self) -> tuple[int, int]:
        """
        Returns the x and y components of the vector as a tuple.

        Returns:
            tuple[int, int]: A tuple containing the x and y components.
        """
        x = self.getX()
        y = self.getY()
        return (x, y)

    def add(self, vector):
        """
        Adds another Vector3 to the current vector.

        Args:
            vector (Vector3): The Vector3 object to add.

        Returns:
            Vector2: A new Vector2 object representing the sum.
        """
        if not isinstance(vector, Vector3):
            return
        x = self.getX() + vector.getX()
        y = self.getY() + vector.getY()
        return Vector2(x, y)

    def differnece(self, vector):
        """
        Subtracts another Vector3 from the current vector.

        Args:
            vector (Vector3): The Vector3 object to subtract.

        Returns:
            Vector2: A new Vector2 object representing the difference.
        """
        if not isinstance(vector, Vector3):
            return
        x = self.getX() - vector.getX()
        y = self.getY() - vector.getY()
        return Vector2(x, y)

    def scale(self, scaler:int):
        """
        Scales the vector by a given scalar value.

        Args:
            scaler (int): The scalar value to scale by.
        
        Returns:
            Vector2: A new Vector2 object representing the scaled vector.
        """
        if not self.is_int(scaler):
            return
        x = self.getX() * scaler
        y = self.getY() * scaler
        return Vector2(x, y)

    def quick_magnitude(self):
        """
        Gives magnitude prior to sqrt. For compairing two vectors not for normalization
        """
        x = self.getX()
        y = self.getY()
        return ((x*x) + (y*y))

    def print(self):
        """
        Prints the x and y components of the vector.
        """
        print(f"X: {self.x}, Y: {self.y}")