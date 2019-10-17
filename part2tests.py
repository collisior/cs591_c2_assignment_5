import unittest 
import part2
import math as math

class ShapeTest(unittest.TestCase):

    def text_test(self):
        s = ShapeCalculator()
        self.assertEqual(s.askUser(), 'Choose a shape: (C)ircle or (R)ectangle or (S)quare')

    def shape_test(self):
        s = ShapeCalculator()
        self.assertEqual(s.whichShape('R'),'Rectangle')
        self.assertEqual(s.whichShape('C'),'Circle')
        self.assertEqual(s.whichShape('S'),'Square')
    
    def questionTest(self):
        s = ShapeCalculator()
        self.assertEqual(s.getQuest('R'), "Rectangle length?"+"Rectangle Breadth?")
        self.assertEqual(s.getQuest('C'), "Circle Circumference?")
        self.assertEqual(s.getQuest('S'), "Square Breadth?")
    
    def measurementTests(self):
        s = ShapeCalculator()
        self.assertEqual(s.getRectMeasure(4, 5), 20)
        self.assertEqual(s.getCircletMeasure(6), (9)*math.pi)
        self.assertEqual(s.getSquareMeasure(6), 36)

if __name__ == "__main__":
    unittest.main()
    
