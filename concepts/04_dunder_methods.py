class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass(value={self.value})"

    def __repr__(self):
        return f"MyClass(value={self.value})"

    def __len__(self):
        return len(self.value)

    def __getitem__(self, index):
        return self.value[index]

    def __setitem__(self, index, value):
        self.value[index] = value

    def __delitem__(self, index):
        del self.value[index]

    def __iter__(self):
        return iter(self.value)


my_obj = MyClass([1, 2, 3])
print(str(my_obj))  # Output: MyClass(value=[1, 2, 3])
print(len(my_obj))  # Output: 3
print(my_obj[0])  # Output: 1
my_obj[0] = 10
print(my_obj[0])  # Output: 10
del my_obj[0]
print(my_obj)  # Output: MyClass(value=[2, 3])



################### Customizing ###################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x + other, self.y + other)
        else:
            raise ValueError("Invalid operand type for addition.")

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(x=4, y=6)

p4 = p1 + 5
print(p4)  # Output: Point(x=6, y=7)
