#Siakavara Themistokleia, 4786
import csv
import sys

def mergeJoin(reader1, reader2, output):
    writer = csv.writer(output)
    R = next(reader1, None)
    S = next(reader2, None)
    
    while R is not None and S is not None:
        if not R or not S:
            continue
        
        if int(R[0]) == int(S[1]):
            R.append(S[0])
            R.append(S[2])
            writer.writerow(R)

            R.pop()
            R.pop()
            S = next(reader2, None)

        elif int(R[0]) < int(S[1]):
            R = next(reader1, None)
        else:
            S = next(reader2, None)
            
if __name__ == "__main__":
    with open('R.csv', mode='r') as file1:
        with open('S.csv', mode = 'r') as file2:
                  reader1 = csv.reader(file1)
                  reader2 = csv.reader(file2)

                  with open('O2.csv', mode='w', newline='') as output:
                      mergeJoin(reader1, reader2, output)
                            
