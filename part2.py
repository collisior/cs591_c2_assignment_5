import math as math

class shapeCalculator:
    def __init__(self): pass

    def askUser(self):
        return 'Choose a shape: (C)ircle or (R)ectangle or (S)quare'
    
    def whichShape(self, input):
        s = ''
        if input == "R":
            s = "Rectangle"
        elif input == "C":
            s = "Circle"
        elif input == "S":
            s = "Square"
        return s
    
    def getQuest(self, input):
        s = ''
        if input == "R":
            s = "Rectangle length?"+"Rectangle Breadth?"
        elif input == "C":
            s = "Circle Circumference?"
        elif input == "S":
            s = "Square Breadth?"
        return s
    
    def getRectMeasure(self, height, width):
        return height*width
    
    def getCircletMeasure(self, circumference):
        return math.pi*math.pow(circumference/2, 2)
    
    def getSquareMeasure(self, height):
        return math.pow(height, 2)
