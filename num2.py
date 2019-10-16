import math as math

class shapeCalculator:
    def askUser():
        return 'Choose a shape: (C)ircle or (R)ectangle or (S)quare'
    
    def whichShape(input):
        s = ''
        if input == "R":
            s = "Rectangle"
        elif input == "C":
            s = "Circle"
        elif input == "S":
            s = "Square"
        return s
    
    def getQuest(input):
        s = ''
        if input == "R":
            s = "Rectangle length?"+"Rectangle Breadth?"
        elif input == "C":
            s = "Circle Circumference?"
        elif input == "S":
            s = "Square Breadth?"
        return s
    
    def getRectMeasure(height, width):
        return height*width
    
    def getCircletMeasure(circumference):
        return math.pi*math.pow(circumference/2, 2)
    
    def getSquareMeasure(height):
        return math.pow(height, 2)
