#Siakavara Themistokleia, 4786
import csv
import sys

def compositeQuery(reader1, reader2, output):
    writer = csv.writer(output)
    R = next(reader1, None)
    S = next(reader2, None)

    currentR = []
    temp = []
    sumE = 0
    
    while R is not None and S is not None:
        if not R or not S:
            continue
        if int(R[0]) == int(S[1]):
            if R[2] == '7':
                sumE = sumE + int(S[2])
                currentR = R[0]
            else:
                if sumE!=0:
                    temp.append(currentR)
                    temp.append(str(sumE))
                    writer.writerow(temp)
                    currentR = temp = []
                    sumE = 0
            S = next(reader2, None)
            
        elif int(R[0]) < int(S[1]):
            if sumE!=0:
                temp.append(currentR)
                temp.append(str(sumE))
                writer.writerow(temp)
                currentR = temp = []
                sumE = 0
            R = next(reader1, None)
        else:
            if sumE!=0:
                temp.append(currentR)
                temp.append(str(sumE))
                writer.writerow(temp)
                currentR = temp = []
                sumE = 0
            S = next(reader2, None)
        
            
if __name__ == "__main__":
    with open('R.csv', mode='r') as file1:
        with open('S.csv', mode = 'r') as file2:
                  reader1 = csv.reader(file1)
                  reader2 = csv.reader(file2)

                  with open('O3.csv', mode='w', newline='') as output:
                      compositeQuery(reader1, reader2, output)
