from AlgorithmAnalysis import AlgorithmAnalysis

class Algorithm:

    def __init__(self, AlgorithmNum, sequence):

        options = {0 : lambda: self.insertionSort(sequence, True),
                   #1 : lambda: self.insertionSort(sequence, True),
                   #4: sqr,
                   #9: sqr,
                   #2: even,
                   #3: prime,
                   #5: prime,
                   #7: prime,
                   }

        options[AlgorithmNum]()

    def insertionSort(self, sequence, increasing):
        if type(increasing) != bool:
            raise ValueError("parameter must be a boolean value, not: " + type(increasing))
        for x in range(1, len(sequence)):
            key = sequence[x]
            j = x - 1
            while key < sequence[j] and j > -1:
                sequence[j + 1] = sequence[j]
                j = j - 1
            sequence[j + 1] = key
        return sequence

if __name__ == "__main__":
    analysis = AlgorithmAnalysis()
    performTimeList = analysis.timeAlgorithm(0, 5000)





