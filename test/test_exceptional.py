
import unittest
from multi_inh import Result
from magic_methods import Point
from test.TestUtils import TestUtils
class ExceptionalTest(unittest.TestCase):
    def test_type_error_on_details(self):
        test_obj = TestUtils()
        try:
            obj=Result()
            obj.set_details(101)
            test_obj.yakshaAssert("TestTypeErrorOnDetails", False, "exception")
            print("TestTypeErrorOnDetails = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorOnDetails", True, "exception")
            print("TestTypeErrorOnDetails = Passed")

    def test_type_error_on_marks(self):
        test_obj = TestUtils()
        try:
            obj=Result()
            obj.set_marks(43,65,76,54)
            test_obj.yakshaAssert("TestTypeErrorOnMarks", False, "exception")
            print("TestTypeErrorOnMarks = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorOnMarks", True, "exception")
            print("TestTypeErrorOnMarks = Passed")

    def test_type_error_on_add(self):
        test_obj = TestUtils()
        try:
            p1=Point('5')
            p2=Point(2)
            result=p1.__add__(p2)
            test_obj.yakshaAssert("TestTypeErrorOnAdd", False, "exception")
            print("TestTypeErrorOnAdd = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorOnAdd", True, "exception")
            print("TestTypeErrorOnAdd = Passed")

    def test_type_error_on_sub(self):
        test_obj = TestUtils()
        try:
            p1=Point(5)
            p2=Point('2')
            result=p1.__sub__(p2)
            test_obj.yakshaAssert("TestTypeErrorOnSub", False, "exception")
            print("TestTypeErrorOnSub = Failed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorOnSub", True, "exception")
            print("TestTypeErrorOnSub = Passed")
