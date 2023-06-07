from timeit import timeit

# ========== ** ==========
pow1 = """
2**30
"""
elapsed_time1 = timeit(pow1, number=100_000)  
# запускаем код pow1 100к раз чтобы уменьшить погрешность
print(elapsed_time1)

# ========== pow() ==========
pow2 = """
pow(2, 30)
"""
elapsed_time2 = timeit(pow2, number=100_000)  
# запускаем код pow1 100к раз чтобы уменьшить погрешность
print(elapsed_time2)

# ========== math.pow() ==========
pow3 = """
math.pow(2, 30)
"""
elapsed_time3 = timeit(pow3, number=100_000, setup="import math")  # запускаем код pow2 100к раз
print(elapsed_time3)


# ========== numpy.power() ==========
pow4 = """
numpy.power(2, 30)
"""
elapsed_time4 = timeit(pow4, number=100_000, setup="import numpy")  # запускаем код pow2 100к раз
print(elapsed_time4)


print(0 ** 0)