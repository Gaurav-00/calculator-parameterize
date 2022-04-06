import Calculate
import pytest


#@pytest.mark.skip   #to skip testcases we use this   1:40
@pytest.mark.xfail
@pytest.mark.parametrize("a,b,c",[(3,2,5),(2,4,6),(10,2,22),(2,4,5),(5,6,7),(7,8,15)])
#@pytest.mark.skip(reason="currently no need to execute")  #to do not run a function
#expected failure-:the failure is expected and we got and unexpected pass-:we get error but we also get pass

#to stop at amxfail we use command-: pytest --maxfail=2
def test_add(a,b,c):
    #x=32
    #y=22
    result=Calculate.add(a,b)
    assert a+b==c
@pytest.mark.parametrize("a1,b1,c1",[(9,9,18),(2,3,5),(3,3,6)])
def test_sub(a1,b1,c1):
    #x=32
    #y=22
    result=Calculate.sub(a1,b1)
    assert a1-b1==c1

@pytest.mark.parametrize("a3,b3,c3",[(2,2,0),(3,4,5),(9,8,1)])
def test_mul(a3,b3,c3):
    #x=32
    #y=22
    result=Calculate.mul(a3,b3)
    assert a3*b3==c3

@pytest.mark.parametrize("a4,b4,c4",[(2,3,1),(6,2,3),(3,3,1)])
def test_div(a4,b4,c4):
    #x=32
    #y=22
    result=Calculate.div(a4,b4)
    assert a4/b4==c4

    #1.find area of rec
    #2. find perimeter of rec take appropriate value from user
    #3.find area of square
    #4.also wr ite a pytest for it

#how to stroke test cases after getting failures

