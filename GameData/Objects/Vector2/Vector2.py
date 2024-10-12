from ..Vector3.Vector3 import Vector3

class Vector2(Vector3):
    def __init__(self, x:int = 0, y:int = 0):
        z = 0
        super().__init__(x, y, z)

    def getZ(self):
        return None
    
    def setZ(self, newZ:int):
        pass

    def set_value(self, newX, newY):
        return super().set_value(newX, newY, 0)
    
    def get_value(self) -> tuple[int, int]:
        x = self.getX()
        y = self.getY()
        return (x, y)

    def add(self, vector):
        if not isinstance(vector, Vector2):
            return
        x = self.getX() + vector.getX()
        y = self.getY() + vector.getY()
        return Vector2(x, y)

    def print(self):
        print(f"X: {self.x}, Y: {self.y}")