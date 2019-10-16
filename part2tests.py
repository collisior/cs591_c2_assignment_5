from unittest import TestCase
from part2 import shapeCalculator
import math as math

class ShapeTest(TestCase):
    def text_test(self):
        self.assertEqual(shapeCalculator.askUser(), 'Choose a shape: (C)ircle or (R)ectangle or (S)quare')

    def shape_test(self):
        self.assertEqual(shapeCalculator.whichShape('R'),'Rectangle')
        self.assertEqual(shapeCalculator.whichShape('C'),'Circle')
        self.assertEqual(shapeCalculator.whichShape('S'),'Square')
    
    def questionTest(self):
        self.assertEqual(shapeCalculator.getQuest('R'), "Rectangle length?"+"Rectangle Breadth?")
        self.assertEqual(shapeCalculator.getQuest('C'), "Circle Circumference?")
        self.assertEqual(shapeCalculator.getQuest('S'), "Square Breadth?")
    
    def measurementTests(self):
        self.assertEqual(shapeCalculator.getRectMeasure(4, 5), 20)
        self.assertEqual(shapeCalculator.getCircletMeasure(6), (9)*math.pi)
        self.assertEqual(shapeCalculator.getSquareMeasure(6), 36)

if __name__ == '__main__':
    s = ShapeTest()
    s.text_test()
    s.shape_test()
    s.questionTest()
    s.measurementTests()

