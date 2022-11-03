# Example 1 - define lambda (getting a number and return the number + 10)
my_lambda = lambda num: num + 10

# Example 2 - call to lambda
res1 = my_lambda(10)
print(res1)     # 20
res2 = my_lambda(2)
print(res2)     # 12


# Example 3 - two arguments
foo = lambda a, b: a * b
print(foo(5, 6))  # 30


# Example 4 - filtering list
is_score_pass = lambda score: score >= 70
scores = [70, 60, 80, 90, 50]
results = filter(is_score_pass, scores)
print(list(results))   # [70, 80, 90]

# Same as above without variables
results2 = filter(lambda score: score >= 70, [70, 60, 80, 90, 50])

res = is_score_pass(50)     # res = False
res2 = is_score_pass(90)     # res = True

