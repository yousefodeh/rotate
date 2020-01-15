import sys, random, argparse 
import numpy as np

def imgyou(fileName): 
    v=[]
    myfile = open(fileName, "r")
    while True:
        line = myfile.readline()
        if not line:
                break
        v.append(len(line))  

    with open(fileName, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh.readlines()]
    y = []
    #print(max(v))
    for word in lines:
        y.append([n for n in word])
    #print (y)
    for i in range(len(y)):
        #print(len(y[i]))
        while len(y[i])!=max(v)-1:
           y[i].append(' ')
    #print(y)
    arr2D = np.array(y)
    arr1_transpose = arr2D.transpose()
    #print(arr1_transpose)
    d=[''.join(x) for x in arr1_transpose]
    #print(d)
    return d
def main(): 
	parser = argparse.ArgumentParser(description="") 
	parser.add_argument('--file', dest='inFile', required=True) 
	parser.add_argument('--out', dest='outFile', required=False) 	
	args = parser.parse_args() 
	imgFile = args.inFile 

	outFile = 'output.txt'
	if args.outFile: 
		outFile = args.outFile 

	A = imgyou(imgFile) 
	f = open(outFile, 'w') 

	for item in A:
            f.write("%s\n" % item)

	f.close() 
	
if __name__ == '__main__': 
	main() 

