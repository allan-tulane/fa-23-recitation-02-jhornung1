from main import *

def test_simple_work():

  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650

  assert simple_work_calc(40, 2, 2) == 224
  assert simple_work_calc(50, 3, 2) == 881
  assert simple_work_calc(60, 4, 2) == 2660

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300

  assert work_calc(40, 2, 2, lambda n: 1) == 63
  assert work_calc(50, 3, 2, lambda n : n*n) == 7615
  assert work_calc(10, 3, 2, lambda n: n + 1) == 110
