from timeit import default_timer as timer
from random import randint
import rpy2
from numpy import *
import scipy as sp
import rpy2.robjects as ro


class AlgorithmAnalysis:

    def sequenceGenerator(self, n):
        sequence = [None] * n
        for x in range(n):
            sequence[x] = randint(0, n)
        return sequence

    def timeAlgorithm(self, algorithmNum, n):

        from Algorithms import Algorithm

        performTimeList = [None] * n

        sequencesList = [None] * n
        for x in range(n):
            randomSequence = self.sequenceGenerator(x)
            sequencesList[x] = randomSequence

        for x in range(n):
            start = timer()
            Algorithm(algorithmNum, sequencesList[x])
            end = timer()
            timeDifference = start - end
            performTimeList[x] = timeDifference


        self.graphComplexity(performTimeList)
        return performTimeList

    def graphComplexity(self, timeList):
        n = len(timeList)
        xCoordinates = [None] * n
        for x in range(n):
            xCoordinates[x] = x
        xString = str(xCoordinates)
        xString = xString[1:n-1]
        yString = str(timeList)
        yString = yString[1:n-1]
        ro.r('x = c(' + xString + ' )')
        ro.r('y = c(' + yString + ' )')
        ro.r('plot(x, y)')


