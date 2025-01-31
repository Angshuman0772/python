class Point:  # classes to define new types
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        

point1 = Point()  # object/instance Point stored in variable point1
point1.x = 10  # attributes
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)