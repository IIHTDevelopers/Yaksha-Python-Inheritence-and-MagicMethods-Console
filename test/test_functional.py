import unittest
from multi_inh import Result
from magic_methods import Point
from test.TestUtils import TestUtils
class FuctionalTests(unittest.TestCase):
    def test_is_tuple(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_details(101,"Aravind")
        result=obj.get_details()
        if type(result)==type((1,)):
            test_obj.yakshaAssert("TestIsTuple", True, "functional")
            print("TestIsTuple = Passed")
        else:
            test_obj.yakshaAssert("TestIsTuple", False, "functional")
            print("TestIsTuple = Failed")

    def test_tuple_elements(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_details(102,"Pavan")
        result=obj.get_details()
        if result!=None:
            if result[0]==102 and result[1]=="Pavan":
                test_obj.yakshaAssert("TestTupleElements", True, "functional")
                print("TestTupleElements = Passed")
            else:
                test_obj.yakshaAssert("TestTupleElements", False, "functional")
                print("TestTupleElements = Failed")
        else:
            test_obj.yakshaAssert("TestTupleElements", False, "functional")
            print("TestTupleElements = Failed")

    def test_tuple_elements_type(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_details(102,"Pavan")
        result=obj.get_details()
        if result!=None:
            if type(result[0])==type(1) and type(result[1])==type(""):
                test_obj.yakshaAssert("TestTupleElementsType", True, "functional")
                print("TestTupleElementsType = Passed")
            else:
                test_obj.yakshaAssert("TestTupleElementsType", False, "functional")
                print("TestTupleElementsType = Failed")
        else:
            test_obj.yakshaAssert("TestTupleElementsType", False, "functional")
            print("TestTupleElementsType = Failed")

    def test_marks(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_marks(78,86,98,66,87)
        result=obj.get_marks()
        if type(result)==type((1,)):
            test_obj.yakshaAssert("TestMarks", True, "functional")
            print("TestMarks = Passed")
        else:
            test_obj.yakshaAssert("TestMarks", False, "functional")
            print("TestMarks = Failed")

    def test_count_subjects(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_marks(78,86,98,66,87)
        result=obj.get_marks()
        if result!=None:
            if len(result)==5:
                test_obj.yakshaAssert("TestCountSubjects", True, "functional")
                print("TestCountSubjects = Passed")
            else:
                test_obj.yakshaAssert("TestCountSubjects", False, "functional")
                print("TestCountSubjects = Failed")
        else:
            test_obj.yakshaAssert("TestCountSubjects", False, "functional")
            print("TestCountSubjects = Failed")

    def test_result(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_marks(50,50,50,50,50)
        result=obj.get_result()
        if result!=None:
            if result[0]==250 and result[1]=="Passed":
                test_obj.yakshaAssert("TestResult", True, "functional")
                print("TestResult = Passed")
            else:
                test_obj.yakshaAssert("TestResult", False, "functional")
                print("TestResult = Failed")
        else:
            test_obj.yakshaAssert("TestResult", False, "functional")
            print("TestResult = Failed")

    def test_result_fail(self):
        test_obj = TestUtils()
        obj=Result()
        obj.set_marks(50,25,50,50,50)
        result=obj.get_result()
        if result!=None:
            if result[0]==225 and result[1]=="Failed":
                test_obj.yakshaAssert("TestResultFail", True, "functional")
                print("TestResultFail = Passed")
            else:
                test_obj.yakshaAssert("TestResultFail", False, "functional")
                print("TestResultFail = Failed")
        else:
            test_obj.yakshaAssert("TestResultFail", False, "functional")
            print("TestResultFail = Failed")

    def test_add(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__add__(p2)
        if result==7:
            test_obj.yakshaAssert("TestAdd", True, "functional")
            print("TestAdd = Passed")
        else:
            test_obj.yakshaAssert("TestAdd", False, "functional")
            print("TestAdd = Failed")

    def test_sub(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__sub__(p2)
        if result==3:
            test_obj.yakshaAssert("TestSub", True, "functional")
            print("TestSub = Passed")
        else:
            test_obj.yakshaAssert("TestSub", False, "functional")
            print("TestSub = Failed")

    def test_mul(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__mul__(p2)
        if result==10:
            test_obj.yakshaAssert("TestMul", True, "functional")
            print("TestMul = Passed")
        else:
            test_obj.yakshaAssert("TestMul", False, "functional")
            print("TestMul = Failed")

    def test_mod(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__mod__(p2)
        if result==1:
            test_obj.yakshaAssert("TestMod", True, "functional")
            print("TestMod = Passed")
        else:
            test_obj.yakshaAssert("TestMod", False, "functional")
            print("TestMod = Failed")

    def test_floordiv(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__floordiv__(p2)
        if result==2:
            test_obj.yakshaAssert("TestFloorDiv", True, "functional")
            print("TestFloorDiv = Passed")
        else:
            test_obj.yakshaAssert("TestFloorDiv", False, "functional")
            print("TestFloorDiv = Failed")

    def test_truediv(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__truediv__(p2)
        if result==2.5:
            test_obj.yakshaAssert("TestTrueDiv", True, "functional")
            print("TestTrueDiv = Passed")
        else:
            test_obj.yakshaAssert("TestTrueDiv", False, "functional")
            print("TestTrueDiv = Failed")

    def test_power(self):
        test_obj = TestUtils()
        p1=Point(5)
        p2=Point(2)
        result=p1.__pow__(p2)
        if result==25:
            test_obj.yakshaAssert("TestPower", True, "functional")
            print("TestPower = Passed")
        else:
            test_obj.yakshaAssert("TestPower", False, "functional")
            print("TestPower = Failed")
