#Siakavara Themistokleia, 4786
import csv
import sys

def groupby_with_aggregation(data, groupAttribute, aggregationAttribute, aggregationFunction):
    if aggregationFunction == 'sum':
        aggFunction = sum
        initialValue = 0
    elif aggregationFunction == 'min':
        aggFunction = min
        initialValue = float('inf')
    elif aggregationFunction == 'max':
        aggFunction = max
        initialValue = float('-inf')
    else:
        raise ValueError("Inappropriate aggregation argument value")

    def extractAttribute(row, groupAttritube, aggAttribute):
        groupValue = row[groupAttribute]
        aggValue = row[aggAttribute]
        return groupValue, aggValue

    def merge(left, right):
        result = []
        i=j=0
        while i<len(left) and j<len(right):
            if left[i][0] < right[j][0]:
                result.append(left[i])
                i = i+1
            elif left[i][0] > right[j][0]:
                result.append(right[j])
                j = j+1
            else:
                aggValues = [left[i][1], right[j][1]]
                aggResult = aggFunction(aggValues)
                result.append((left[i][0], aggResult))
                i = i+1
                j = j+1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def mergeSort(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = mergeSort(array[:mid])
        right = mergeSort(array[mid:])
        return merge(left, right)

    elimination = [extractAttribute(row, groupAttribute, aggregationAttribute) for row in data]
    elim = [(int(x), int(y)) for x, y in elimination]
    sortData = mergeSort(elim)
    return sortData
            
if __name__ == "__main__":
    if len(sys.argv)!= 5:
        print("Not enough arguments")
        sys.exit(1)

    data = []
    with open(sys.argv[1], mode = 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
            
    groupAttribute = int(sys.argv[2])
    aggregationAttribute = int(sys.argv[3])
    aggregationFunction = sys.argv[4]
    

    finalData = groupby_with_aggregation(data, groupAttribute, aggregationAttribute, aggregationFunction)

    with open('O1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in finalData:
            writer.writerow(row)
