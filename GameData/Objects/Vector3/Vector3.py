class Vector3():
    def __init__(self, x:int = 0, y:int = 0, z:int = 0):
        self._x = x
        self._y = y
        self._z = z

    def is_int(self, test_int):
        if type(test_int) != int:
            print("not int")
            return False
        return True
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def getZ(self):
        return self._z

    def get_value(self):
        return (self._x, self._y, self._z)
    
    def set_value(self, newX:int, newY:int, newZ:int):
        self.setX(newX)
        self.setY(newY)
        self.setZ(newZ)

    def setX(self, newX:int):
        if not self.is_int(newX):
            return
        self._x = newX

    def setY(self, newY:int):
        if not self.is_int(newY):
            return
        self._y = newY

    def setZ(self, newZ:int):
        if not self.is_int(newZ):
            return
        self._z = newZ

    def add(self, vector):
        if not isinstance(vector, Vector3):
            return
        x = self.getX() + vector.getX()
        y = self.getY() + vector.getY()
        z = self.getZ() + vector.getZ()
        return Vector3(x, y, z)

    def differnece(self, vector):
        if not isinstance(vector, Vector3):
            return
        x = self.getX() - vector.getX()
        y = self.getY() - vector.getY()
        z = self.getZ() - vector.getZ()
        return Vector3(x, y, z)

    def scale(self, scaler:int):
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
        print(f"X: {self._x}, Y: {self._y}, Z: {self._z}")