import json
import argparse
import sys
import os

filename = "storage.data"

def parse(args):
    if(args.value == None):
        with open(filename,'r') as file:
            data = dict(json.load(file))
            res = data.get(args.key)
            if(res == None):
                print(None)
                return
            print(res[0], end = '')
            if(len(res)) != 1:
                for i in res[1:]:
                    print(', {}'.format(i), end = '')
            print()
    else:
        print(args.key, args.value)
        data = None
        with open(filename,'r') as file:
            data = dict(json.load(file))
        res = data.get(args.key)
        if(res == None):
            data[args.key] = []    
        data[args.key].append(args.value)
        with open(filename,'w+') as file:
            json.dump(data, file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Key-value storage')
    parser.add_argument("--key", metavar="KEY")
    parser.add_argument("--value", metavar="VALUE")
    a = parser.parse_args(sys.argv[1:])
    parse(a)

