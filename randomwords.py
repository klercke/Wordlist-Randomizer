import sys
import argparse
import random
import time
import math


def buildOutput(data, len, ratio, head, train, test):
    output = []

    trainLen = math.ceil((ratio / 100) * len)

    for item in head:
        output.append(item.strip())
    
    random.seed(time.time())
    random.shuffle(data)
    
    output.append("===Begin Training Words===")

    for item in train:
        output.append(item.strip())

    for i in range(trainLen):
        output.append(data[i].strip())
    
    output.append("===Begin Testing Words===")

    for item in test:
        output.append(item.strip())
    
    for j in range(i + 1, len):
        output.append(data[j].strip())

    for line in output:
        print(line)


def main():
    parser = argparse.ArgumentParser(description=
        "Genrate wordlists for training AI based on input text files")
    parser.add_argument('infile', 
                        metavar="file", 
                        type=str, 
                        default=sys.stdin, 
                        help="The input file to randomize")
    parser.add_argument('-t', '--top',
                        dest='head',
                        metavar="header",
                        type=str,
                        help="A header file to add to the top of the output")
    parser.add_argument('-l', '--length',
                        dest='len',
                        metavar='length',
                        type=int,
                        default=15,
                        help="The lengh of the random wordlist to generate")
    parser.add_argument('-r', '--ratio',
                        dest='ratio',
                        metavar="ratio",
                        type=int,
                        default=80,
                        help="The percentage of words to go in the training list")
    parser.add_argument('-i', '--train',
                        dest='train',
                        metavar="list",
                        help="A file containing words that will always be in the training category")
    parser.add_argument('-s', '--test',
                        dest='test',
                        metavar="list",
                        type=str,
                        help="A file containing words that will always be in the testing category")                       

    args = parser.parse_args()

    
    # Open file, then close it once we're done reading the input
    with open(args.infile, 'r') as file:
        # Make list of each line
        data = file.readlines()

    head=[]
    if (args.head):
        with open(args.head, 'r') as file:
            # Make list of each line
            head = file.readlines()
    
    train=[]
    if (args.train):
        with open(args.train, 'r') as file:
            # Make list of each line
            train = file.readlines()
    
    test=[]
    if (args.test):
        with open(args.test, 'r') as file:
            # Make list of each line
            test = file.readlines()

    if (args.len > len(data)):
        print("Error: Wordlist length " + str(args.len) + 
            " is greater than input length " + str(len(data)))
        sys.exit(0)

    buildOutput(data, args.len, args.ratio, head, train, test)
   

if __name__ == "__main__":
    main()