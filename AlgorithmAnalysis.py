from timeit import default_timer as timer
from random import randint
from ggplot import *
import pandas as pd

class AlgorithmAnalysis:

    def sequenceGenerator(self, n):
        sequence = [None] * n
        for x in range(n):
            sequence[x] = randint(0, n)
        return sequence

    def analyzeAlgorithm(self, algorithmNum, n):

        from Algorithms import Algorithm

        n += 1

        performTimeList = [None] * n

        sequencesList = [None] * n
        
        for x in range(n):
            randomSequence = self.sequenceGenerator(x)
            sequencesList[x] = randomSequence
        
        for x in range(n):
            start = timer()
            Algorithm(algorithmNum, sequencesList[x])
            end = timer()
            timeDifference = end - start
            performTimeList[x] = timeDifference

        self.graphComplexity(performTimeList, Algorithm(algorithmNum, sequencesList[0]).algorithmName)

        return performTimeList

    def graphComplexity(self, performTimeList, algorithmName):
        n = len(performTimeList)
        sizesOfN = [None] * n
        for x in range(n):
            sizesOfN[x] = x

        df = pd.DataFrame(performTimeList, columns=['Performance Time in Milliseconds'])
        df['Sizes of N'] = sizesOfN
        p = ggplot(aes(x = "Sizes of N", y="Performance Time in Milliseconds"), data=df) + geom_point() + ggtitle("Analysis of Time Complexity for " + algorithmName)
        print(p)