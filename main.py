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
  if n <= 1:
    return 0  # Base case, no span
  else:
    return max(
      span_calc(n / b, a, b, f),  # Recursive span
      work_calc(n / b, a, b, f) / a  # Work per processor
    )

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
  sizes = [10, 100, 1000, 10000]
  a_values = [2, 3]
  b_values = [2, 3]
  c_values = [1, 2, 3]

  for a in a_values:
    for b in b_values:
      for c in c_values:
        print(f"a = {a}, b = {b}, c = {c}:")
                
        # Define a custom work function based on the recurrence relation
        def custom_work_function(n):
          return work_calc(n, a, b, lambda x: x**c)
                
        # Compare the custom work function with a reference function
        reference_function = lambda n: n  # For example, linear function
                
        comparison_result = compare_work(custom_work_function, reference_function, sizes)
                
        # Print the comparison result
        for item in comparison_result:
          n, custom_v, reference_v = item
          print(f"W({n}) (Custom): {custom_v}, W({n}) (Reference): {reference_v}")
                
      print()

def test_compare_span():
  sizes = [10, 100, 1000, 10000]
  a_values = [2, 3]
  b_values = [2, 3]
  c_values = [1, 2, 3]

  for a in a_values:
    for b in b_values:
      for c in c_values:
        print(f"a = {a}, b = {b}, c = {c}:")
        for n in sizes:
          # Define the custom work function based on the recurrence relation
          def custom_work_function(x):
            return work_calc(x, a, b, lambda x: x**c)
                    
          # Calculate the span using the custom work function
          span_result = span_calc(n, a, b, lambda x: x**c)
          print(f"Span({n}) = {span_result}")
        print()

def test_work_calc_question_3():
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


test_compare_span()