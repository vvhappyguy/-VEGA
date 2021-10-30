import time

def time_measurement_decorator(func):
    def the_wrapper_around_the_original_function(arr):
        time_point = round(time.time() * 1000)
        res = func(arr) 
        print(round(time.time() * 1000) - time_point)
        return res 
    return the_wrapper_around_the_original_function

@time_measurement_decorator
def forPow(arr):
    res = []
    for a in arr:
        res.append(a*a)
    return res

@time_measurement_decorator
def listComprPow(arr):
    return [a*a for a in arr]

@time_measurement_decorator
def mapPow(arr):
    return list(map(lambda x: x * x, arr))
    

if __name__ == "__main__":
    numbers = [i for i in range(10000000)]
    forPow(numbers)
    listComprPow(numbers)
    mapPow(numbers)
    
