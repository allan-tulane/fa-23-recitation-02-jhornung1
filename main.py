"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
  if n == 0:
    return 0
  return (a * simple_work_calc(n // b, a ,b) + n)

def work_calc(n, a, b, f):
    result = 0
    while n > 1:
        result += f(n)  # Add f(n) at each step
        n //= b
    result += a * f(n)  # Add the final term a * f(n) when n becomes 1
    return result

def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  # TODO
  pass



def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((
      n,
      work_fn1(n),
      work_fn2(n)
      ))
  return result

def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
  Compare the values of different recurrences for
  given input sizes.
  Returns:
  A list of tuples of the form
  (n, work_fn1(n), work_fn2(n), ...)
  """
  result = []
  for n in sizes:
    # compute W(n) using current a, b, f
    result.append((
      n,
      span_fn1,
      span_fn2
      ))
  return result


def print_results(results):
  print(tabulate.tabulate(results,
              headers=['n', 'W_1', 'W_2'],
              floatfmt=".3f",
              tablefmt="github"))

def test_compare_work():
  # curry work_calc to create multiple work
  # functions that can be passed to compare_work
  def work_fn1():
    return 1 * 1
  def work_fn2():
    return 1 + 1 + 1

  return compare_work(work_fn1, work_fn2)

def test_compare_span():
  # TODO
  pass

# Decide value for work calc
a = 2
b = 2

# Define the function being used
def f(n):
    return math.log(n)

# Multiple values for n
nums = [10,20,30,40,50,60,70,80,90,100]
for val in nums:
  print(work_calc(val, a, b, f))

