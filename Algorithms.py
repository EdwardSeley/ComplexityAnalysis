
from AlgorithmAnalysis import AlgorithmAnalysis

class Algorithm:

    def __init__(self, AlgorithmNum, sequence):

        options = {0 : lambda: self.insertionSort(sequence),
                   1 : lambda: self.merge_sort(sequence, 0, len(sequence) - 1),
                   #4: sqr,
                   #9: sqr,
                   #2: even,
                   #3: prime,
                   #5: prime,
                   #7: prime,
                   }

        options[AlgorithmNum]()

        names = {0 : "Insertion Sort",
                 1 : "Merge Sort"
        }

        self.algorithmName = names[AlgorithmNum]

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
            subOneLength = middle - first + 1
            subTwoLength = last - middle
            leftSequence = [None] * (subOneLength + 1)
            rightSequence = [None] * (subTwoLength + 1)
            for x in range(subOneLength):
                leftSequence[x] = sequence[first + x]
            for y in range(subTwoLength):
                rightSequence[y] = sequence[middle + 1 + y]

            leftSequence[subOneLength] = 1000
            rightSequence[subTwoLength] = 1000

            x = 0
            y = 0
            i = 0

            for i in range(first, last):
                if leftSequence[x] < rightSequence[y]:
                    sequence[i] = leftSequence[x]
                    x = x + 1
                else:
                    sequence[i] = rightSequence[y]
                    y = y + 1
            
            i = i + 1
            # Copy the remaining elements of L[], if there
            # are any
            while x < subOneLength and i < len(sequence) and x < len(leftSequence):
                sequence[i] = leftSequence[x]
                x += 1
                i += 1

            # Copy the remaining elements of R[], if there
            # are any
            while y < subTwoLength:
                sequence[i] = rightSequence[y]
                y += 1
                i += 1

        return sequence

if __name__ == "__main__":
  analysis = AlgorithmAnalysis()
  analysis.analyzeAlgorithm(0, 1000)
  analysis.analyzeAlgorithm(1, 1000)