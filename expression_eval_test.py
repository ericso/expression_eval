import unittest
import expression_eval


# expression = "+20/4+5+*1000+9--*" # 50.5


class StackExpressionEvaluatorTestCase(unittest.TestCase):

    def testWellFormedExpression(self):
        input_str = "5+4*6/2"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(17, result)

    def testDecimalResult(self):
        input_str = "2/4+5*5*5"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(125.5, result)

    def testMultiDigitExpression(self):
        input_str = "20/4+5*1000+9"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(5014, result)

    def testUnrecognizedOperator(self):
        input_str = "20/4+5^1000+9"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(None, result)

    def testHangingOperators(self):
        """
        When there are hanging operators in the expression, the algorithm
        currently will still return the correct result as if they were not
        there.
        """
        input_str = "5+4*6/2"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(17, result)

if __name__ == "__main__":
    unittest.main()
