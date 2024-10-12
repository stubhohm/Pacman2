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

    def print(self):
        print(f"X: {self._x}, Y: {self._y}, Z: {self._z}")