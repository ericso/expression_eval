import unittest
import expression_eval


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

    def testSingleCharacterResultNumber(self):
        input_str = "5"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(5, result)

    def testSingleCharacterResultOperator(self):
        input_str = "*"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(None, result)

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
        input_str = "+5+4*6/2/"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(17, result)

    def testSequentialOperators(self):
        """
        When there are sequentail operators in the expression, the algorithm
        should fail and evaluate should return None.
        """
        input_str = "5+4**6/2"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(None, result)

    def testParenthesis(self):
        """
        Groups of expressions enclosed in parens should be evaluated first.
        """
        input_str = "(5+4)*(6/2)"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(27, result)

    def testNestedParenthesis(self):
        """
        Groups of expressions enclosed in parens should be evaluated first.
        """
        input_str = "(5+4)*((6/2)+10)"
        result = expression_eval.evaluate(input_str)
        self.assertEqual(117, result)

if __name__ == "__main__":
    unittest.main()
