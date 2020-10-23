import unittest
# from exp_eval import *
import shutil
# import xlwt 
# from xlwt import Workbook 

class Project2Test(unittest.TestCase):

    def test_infix_to_postfix1(self):
        self.assertEqual(infix_to_postfix('( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )'), '5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^')
        self.assertEqual( infix_to_postfix('( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )'), '15 7 1 1 + - / 3 * 2 1 1 + + -')
        self.assertEqual(infix_to_postfix('10 + 3 * 5 / ( 16 - 4 )'),'10 3 5 * 16 4 - / +')
        self.assertEqual(infix_to_postfix('4 ^ ( 1 ) * 4'),'4 1 ^ 4 *')
    
    def test_infix_to_postfix2(self):
        self.assertEqual(infix_to_postfix('5 * 3 ^ ( 4 - 2 )'),'5 3 4 2 - ^ *')
        self.assertEqual(infix_to_postfix('( ( 1 * 2 ) + ( 3 / 4 ) )'),'1 2 * 3 4 / +')
        self.assertEqual(infix_to_postfix('( ( 2 * ( 3 + 4 ) ) / 5 )'), '2 3 4 + * 5 /')
    
    def test_infix_to_postfix3(self):
        self.assertEqual(infix_to_postfix('( 3 * ( 4 + 6 / 3 ) )'),'3 4 6 3 / + *')
        self.assertEqual(infix_to_postfix('3 * 3 + 9'),'3 3 * 9 +')
        self.assertEqual(infix_to_postfix('( 3 ) ^ 2 + 9'),'3 2 ^ 9 +')
        self.assertEqual(infix_to_postfix('3 ^ 2 + 9'),'3 2 ^ 9 +')
    
    def test_prefix_to_postfix4(self):
        self.assertEqual(prefix_to_postfix('+ + 3 * 3 3 3'),'3 3 3 * + 3 +')
        self.assertEqual(prefix_to_postfix('* + 2 2 + 2 2'),'2 2 + 2 2 + *')
        self.assertEqual(prefix_to_postfix('+ * 1 1 * 1 1'),'1 1 * 1 1 * +')
        self.assertEqual(prefix_to_postfix('+ + + 4 4 4 4'),'4 4 + 4 + 4 +')
    
    def test_prefix_to_postfix5(self):
        self.assertEqual(prefix_to_postfix('+ * 3 3 / 3 3'),'3 3 * 3 3 / +')
        self.assertEqual(prefix_to_postfix('/ * 1 + 2 3 4'),'1 2 3 + * 4 /')
        self.assertEqual(prefix_to_postfix('* 1 + 2 / 3 4'),'1 2 3 4 / + *')
    
    def test_prefix_to_eval6(self):
        self.assertEqual(prefix_to_postfix('+ + 1 * 2 3 4'),'1 2 3 * + 4 +')
        self.assertEqual(prefix_to_postfix('* + 8 7 + 6 5'),'8 7 + 6 5 + *')
        self.assertEqual(prefix_to_postfix('+ * 12 13 * 14 15'),'12 13 * 14 15 * +')
        self.assertEqual(prefix_to_postfix('+ + + 44 43 42 41'),'44 43 + 42 + 41 +')

    def test_postfix_eval7(self):
        self.assertAlmostEqual(postfix_eval('5 4 -'), 1)  # tests for -
        self.assertAlmostEqual(postfix_eval('6 2 1 * /'), 3) 
        self.assertAlmostEqual(postfix_eval('5 1 2 + 4 ^ + 3 -'), 83)  # tests for **
        self.assertAlmostEqual(postfix_eval('6 7 8 9 2 3 + 1 - 1 + 4 * 5 / + - + *'), 12)

    def test_postfix_eval8(self):
        self.assertEqual(postfix_eval('3 3 ^ 2 * 3 + 2 1 / -'), 55)
        self.assertEqual(postfix_eval("8 3 4 * + 6 2 2 ^ 6 3 / 1 - * - 6 - +"),16)
        self.assertEqual(postfix_eval('5 1 2 + 4 ^ + 3 -'),83)
        self.assertAlmostEqual(postfix_eval('5 4 -'), 1)  # tests for -
        self.assertAlmostEqual(postfix_eval('6 2 1 * /'), 3) 
    
    def test_postfix_eval9(self):
        self.assertEqual(postfix_eval("1 2 +"), 3)
        self.assertEqual(postfix_eval("2 3 2 ^ ^"), 512)
        self.assertEqual(postfix_eval("2 3 ^ 2 ^"), 64)
        with self.assertRaises(ValueError):
            postfix_eval("12 0 /")

    def test_postfix_eval10(self):
        try:
            postfix_eval("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval11(self):
        try:
            postfix_eval("b a .")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval12(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval13(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval14(self):
        try:
            postfix_eval("1 2 - 3 4 5 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

if __name__ == '__main__': 
    log_file = 'log_file.txt'
    with open(log_file, "w") as f: 
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

