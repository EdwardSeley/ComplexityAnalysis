from AlgorithmAnalysis import AlgorithmAnalysis

class Algorithm:

    def __init__(self, AlgorithmNum, sequence):

        options = {0 : lambda: self.insertionSort(sequence),
                   1 : lambda: self.merge_sort(sequence, 0, len(sequence)),
                   #4: sqr,
                   #9: sqr,
                   #2: even,
                   #3: prime,
                   #5: prime,
                   #7: prime,
                   }

        options[AlgorithmNum]()

    def insertionSort(self, sequence):
        for x in range(1, len(sequence)):
            key = sequence[x]
            j = x - 1
            while key < sequence[j] and j > -1:
                sequence[j + 1] = sequence[j]
                j = j - 1
            sequence[j + 1] = key
        return sequence

    def merge_sort(self, sequence, first, last):
        if first < last:
            middle = int(0.5 * (first + last))
            self.merge_sort(sequence, first, middle)
            self.merge_sort(sequence, middle + 1, last)
            self.merge(sequence, first, middle, last)
            print(sequence)

    def merge(self, sequence, first, middle, last):
        subOneLength = middle - first
        subTwoLength = last - middle
        leftSequence = [None] * (subOneLength + 1)
        rightSequence = [None] * (subTwoLength + 1)
        for x in range(subOneLength):
            leftSequence[x] = sequence[first + x]
        for y in range(subTwoLength):
            rightSequence[y] = sequence[middle + y]

        leftSequence[subOneLength] = 1000
        rightSequence[subTwoLength] = 1000

        print("subOneLength: " + str(subOneLength))
        print("subTwoLength: " + str(subTwoLength))
        print("left sequence: " + str(leftSequence))
        print("right sequence: " + str(rightSequence))

        x = 0
        y = 0

        for i in range(first, last):
            if leftSequence[x] < rightSequence[y]:
                sequence[i] = leftSequence[x]
                x = x + 1
            else:
                sequence[i] = rightSequence[y]
                y = y + 1

if __name__ == "__main__":
    #analysis = AlgorithmAnalysis()
    #performTimeList = analysis.timeAlgorithm(0, 1000)
    random_list = [3, 7, 1, 9, 3, 6, 4, 12]
    Algorithm(1, random_list)






