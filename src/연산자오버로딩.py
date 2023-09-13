class Vector20 :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # + 연산에 대응 됩니다.
        return Vector20(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector20((self.x * other.x)+100, (self.y  * other.y) + 100)

v1 = Vector20(1, 2)
v2 = Vector20(3, 4)
v3 = Vector20(4, 5)

print(100 * 200)
print(100.1 * 200.1)
v3 = v1 + v2 * v3
print(v3.x, v3.y)