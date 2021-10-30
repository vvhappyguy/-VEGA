def lensort(arr):
    return sorted(arr, key = lambda word: len(word))

if __name__ == "__main__":
    print(lensort(["123","1", "12"]))
    print(lensort(["123","1", "12", "312312312", "11", "0"]))