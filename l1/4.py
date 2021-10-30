def read_and_dict(filename):
    res = {}
    with open(filename,'r') as file:
        for line in file:
            for word in line.split():
                res.setdefault(word, 0)
                res[word] += 1
    print(res)
                

if __name__ == "__main__":
    read_and_dict("4.py")