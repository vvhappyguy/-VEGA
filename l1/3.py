def my_enumerate(arr):
    return [(i, a) for a, i in zip(arr, range(len(arr)))]

if __name__ == "__main__":
    print(my_enumerate(["123","1", "12", "1", "123"]))