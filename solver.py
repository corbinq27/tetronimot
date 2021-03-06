import random
import sys

class Solver:

    def __init__(self):
        self.l = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.m = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        self.currentBlock = 1
        self.coordlist = []

        #just used for backtrakcing
        self.currentZeroIndex = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.currentPieceIndex = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        self.solution = []
        self.thisIsSolved = False


    def reset(self):
        self.l = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        self.m = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

    def place(self, tOne, tTwo, tThree, tFour):
        self._placeUnit(tOne)
        self._placeUnit(tTwo)
        self._placeUnit(tThree)
        self._placeUnit(tFour)
        self.currentBlock += 1
        self.coordlist.append([tOne, tTwo, tThree, tFour])

    def _placeUnit(self, coord):
        if coord[2] == 0:
            self.l[coord[1]][coord[0]] = self.currentBlock
        else:
            self.m[coord[1]][coord[0]] = self.currentBlock

    def isTetrinoSpaceEmpty(self, tOne, tTwo, tThree, tFour):
        return self._isUnitEmpty(tOne) and self._isUnitEmpty(tTwo) and self._isUnitEmpty(tThree) and self._isUnitEmpty(
            tFour)

    def _isUnitEmpty(self, coord):
        if coord[2] == 0:
            if self.l[coord[1]][coord[0]] != 0:
                return False
        else:
            if self.m[coord[1]][coord[0]] != 0:
                return False
        return True

    def _getValidMoves(self, unitCoord):
        """
                                  3
        Tetrino's four pieces: x0 1 2
        all possible placements on a single plane:
           a                                             [0,0,0],[-1,1,0],[0,1,0],[1,1,0]
           3
        x0 1 2z        [0,0,0],[1,0,0],[2,0,0],[1,-1,0]                                    [0,0,0],[-2,0,0],[-1,0,0],[-1,-1,0]
           y                                            [0,0,0],[-1,0,0],[1,0,0],[0,-1,0]


          z     z      [0,0,0],[0,2,0],[0,1,0],[-1,1,0]                                    [0,0,0],[0,2,0],[0,1,0],[1,1,0]
          2     2
        a31y   y13a    [0,0,0],[1,1,0],[1,0,0],[1,-1,0] [0,0,0],[0,1,0],[0,-1,0],[-1,0,0]  [0,0,0],[0,1,0],[0,-1,0],[1,0,0] [0,0,0],[-1,1,0],[-1,-1,0],[-1,0,0]
          0     0
          x     x      [0,0,0],[0,-1,0],[0,-2,0],[-1,-1,0]                                 [0,0,0],[0,-1,0],[0,-2,0],[1,-1,0]

            y          [0,0,0],[1,0,0],[-1,0,0],[0,1,0]
         z2 1 0x       [0,0,0],[2,0,0],[1,0,0],[1,1,0]  [0,0,0],[-1,0,0],[-2,0,0],[-1,-1,0]
            3
            a          [0,0,0],[1,-1,0],[0,-1,0],[-1,-1,0]

          x      x
          0      0
        a31y    a13y
          2      2
          z      z

        All possible placements when on exactly two planes:
        m is "in" the monitor; when 1 is shown, 3 is "in" the monitor on m (and vice versa)
          l     l l l
          z                    [0,0,0],[0,2,0],[0,1,0],[0,1,1]
          2       y                                                                                  [0,0,0],[-1,0,0],[1,0,0],[0,0,1]
          1y   x0 1 2z         [0,0,0],[0,1,0],[0,-1,0],[0,0,1] [0,0,0],[0,0,-1],[0,-1,-1],[0,1,-1]  [0,0,0],[1,0,0],[2,0,0],[1,0,1] [0,0,0],[-2,0,0],[-1,0,0],[-1,0,1]
          0                                                                                          [0,0,0],[-1,0,-1],[0,0,-1],[1,0,-1]
          x                    [0,0,0],[0,-1,0],[0,-2,0],[0,-1,1]

          l
          z
          2
         y1
          0
          x

        l l l       m l m    m l m    m
                      y               0z  [0,0,0],[1,0,0],[-1,0,0],[0,0,-1]                                       [0,0,0],[0,1,0],[0,2,0],[0,1,-1]
        2 1 0      x2 3 0z    0 3 2   3y  [0,0,0],[2,0,0],[1,0,0],[1,0,-1] [0,0,0],[-1,0,0],[-2,0,0],[-1,0,-1]    [0,0,0],[0,-1,0],[0,1,0],[0,0,-1] [0,0,0],[0,-1,1],[0,0,1],[0,1,1]
                                      2x  [0,0,0],[1,0,1],[0,0,1],[-1,0,1]                                        [0,0,0],[0,-2,0],[0,-1,0],[0,-1,-1]

         m           m
         2           0
         1 (on l)    1 (on l)
         0           2
        """
        # validVectors = [
        #     [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, -1, 0]],     # x_|_
        #     [[0, 0, 0], [0, -1, 0], [0, -2, 0], [-1, -1, 0]],  # -|
        #                                                        # x
        #     [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, 1, 0]],   # Tx
        #     [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 1, 0]],      # x
        #                                                        # |-
        #     [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 1, 0]],      # XT
        #     [[0, 0, 0], [0, -1, 0], [0, -2, 0], [1, -1, 0]],   # |-
        #                                                        # x
        #     [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, -1, 0]],  # _|_x
        #                                                        # x
        #     [[0, 0, 0], [0, 1, 0], [0, 2, 0], [-1, 1, 0]],     # -|
        #     [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1]],      # x---
        #     [[0, 0, 0], [0, -1, 0], [0, -2, 0], [0, -1, 1]],   # |
        #                                                        # x
        #     [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, 0, 1]],   # ---x
        #     [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1]],      # x
        #                                                        # |
        #     [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, -1]],     # x---
        #     [[0, 0, 0], [0, -1, 0], [0, -2, 0], [0, -1, -1]],  # |
        #                                                        # x
        #     [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, 0, -1]],  # ---x
        #     [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, -1]],     # x
        #                                                        # |
        #     [[0, 0, 0], [0, -1, -1], [0, 0, -1], [0, 1, -1]],  # |
        #                                                        # x
        #                                                        # |
        #     [[0, 0, 0], [0, -1, 1], [0, 0, 1], [0, 1, 1]],     # |
        #                                                        # |X (Tetrino is |- but is rotated 90 degrees left)
        #                                                        # |
        #     [[0, 0, 0], [-1, 0, -1], [1, 0, -1], [0, 0, -1]],  # -x-
        #     [[0, 0, 0], [-1, 0, 1], [1, 0, 1], [0, 0, 1]],  # --- (Tetrino is _|_ but rotated 90 degrees away (into the page))
        #                                                        #  x
        #     [[0, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1]],
        #     [[0, 0, 0], [0, -1, 0], [1, 0, 0], [0, 1, 0]],    # x|-
        #     [[0, 0, 0], [-1, -1, 0], [-1, 0, 0], [-1, 1, 0]], # |-x
        #     [[0, 0, 0], [-1, 1, 0], [0, 1, 0], [1, 1, 0]],    # x
        #                                                       #_|_
        #     [[0, 0, 0], [-1, -1, 0], [0, -1, 0], [1, -1, 0]]  #T
        #                                                       #x

        validVectors = [
            [[0,0,0],[-1,1,0],[0,1,0],[1,1,0]],
            [[0,0,0],[1,0,0],[2,0,0],[1,-1,0]],
            [[0,0,0],[-2,0,0],[-1,0,0],[-1,-1,0]],
            [[0,0,0],[-1,0,0],[1,0,0],[0,-1,0]],
            [[0,0,0],[0,2,0],[0,1,0],[-1,1,0]],
            [[0,0,0],[0,2,0],[0,1,0],[1,1,0]],
            [[0,0,0],[1,1,0],[1,0,0],[1,-1,0]],
            [[0,0,0],[0,1,0],[0,-1,0],[-1,0,0]],
            [[0,0,0],[0,1,0],[0,-1,0],[1,0,0]],
            [[0,0,0],[-1,1,0],[-1,-1,0],[-1,0,0]],
            [[0,0,0],[0,-1,0],[0,-2,0],[-1,-1,0]],
            [[0,0,0],[0,-1,0],[0,-2,0],[1,-1,0]],
            [[0,0,0],[1,0,0],[-1,0,0],[0,1,0]],
            [[0,0,0],[2,0,0],[1,0,0],[1,1,0]],
            [[0,0,0],[-1,0,0],[-2,0,0],[-1,-1,0]],
            [[0,0,0],[1,-1,0],[0,-1,0],[-1,-1,0]],
            [[0,0,0],[0,2,0],[0,1,0],[0,1,1]],
            [[0,0,0],[-1,0,0],[1,0,0],[0,0,1]],
            [[0,0,0],[0,1,0],[0,-1,0],[0,0,1]],
            [[0,0,0],[0,0,-1],[0,-1,-1],[0,1,-1]],
            [[0,0,0],[1,0,0],[2,0,0],[1,0,1]],
            [[0,0,0],[-2,0,0],[-1,0,0],[-1,0,1]],
            [[0,0,0],[0,-1,0],[0,-2,0],[0,-1,1]],
            [[0,0,0],[-1,0,-1],[0,0,-1],[1,0,-1]],
            [[0,0,0],[1,0,0],[-1,0,0],[0,0,-1]],
            [[0,0,0],[0,1,0],[0,2,0],[0,1,-1]],
            [[0,0,0],[2,0,0],[1,0,0],[1,0,-1]],
            [[0,0,0],[-1,0,0],[-2,0,0],[-1,0,-1]],
            [[0,0,0],[0,-1,0],[0,1,0],[0,0,-1]],
            [[0,0,0],[0,-1,1],[0,0,1],[0,1,1]],
            [[0,0,0],[1,0,1],[0,0,1],[-1,0,1]],
            [[0,0,0],[0,-2,0],[0,-1,0],[0,-1,-1]]

        ]
        toReturn = []
        for eachVector in range(0, len(validVectors)):
            tOne = [validVectors[eachVector][0][0] + unitCoord[0], \
                    validVectors[eachVector][0][1] + unitCoord[1], \
                    validVectors[eachVector][0][2] + unitCoord[2]]
            tTwo = [validVectors[eachVector][1][0] + unitCoord[0], \
                    validVectors[eachVector][1][1] + unitCoord[1], \
                    validVectors[eachVector][1][2] + unitCoord[2]]
            tThree = [validVectors[eachVector][2][0] + unitCoord[0], \
                      validVectors[eachVector][2][1] + unitCoord[1], \
                      validVectors[eachVector][2][2] + unitCoord[2]]
            tFour = [validVectors[eachVector][3][0] + unitCoord[0], \
                     validVectors[eachVector][3][1] + unitCoord[1], \
                     validVectors[eachVector][3][2] + unitCoord[2]]
            toReturn.append([tOne, tTwo, tThree, tFour])
        return toReturn

    def getValidMoves(self, unitCoord):
        toReturn = []
        possibleMoves = self._getValidMoves(unitCoord)
        for eachTetrino in possibleMoves:
            if eachTetrino[0][0] >= 0 and eachTetrino[0][0] <= 5 and \
                    eachTetrino[0][1] >= 0 and eachTetrino[0][1] <= 5 and \
                    eachTetrino[0][2] >= 0 and eachTetrino[0][2] <= 1 and \
                    eachTetrino[1][0] >= 0 and eachTetrino[1][0] <= 5 and \
                    eachTetrino[1][1] >= 0 and eachTetrino[1][1] <= 5 and \
                    eachTetrino[1][2] >= 0 and eachTetrino[1][2] <= 1 and \
                    eachTetrino[2][0] >= 0 and eachTetrino[2][0] <= 5 and \
                    eachTetrino[2][1] >= 0 and eachTetrino[2][1] <= 5 and \
                    eachTetrino[2][2] >= 0 and eachTetrino[2][2] <= 1 and \
                    eachTetrino[3][0] >= 0 and eachTetrino[3][0] <= 5 and \
                    eachTetrino[3][1] >= 0 and eachTetrino[3][1] <= 5 and \
                    eachTetrino[3][2] >= 0 and eachTetrino[3][2] <= 1:
                toReturn.append(eachTetrino)
        return toReturn

    def placeRandomPiece(self, coord, randomSeed=-1):
        validPieces = self.getValidMoves(coord)
        validMoves = []
        for eachPiece in validPieces:
            if self.isTetrinoSpaceEmpty(eachPiece[0], eachPiece[1], eachPiece[2], eachPiece[3]):
                validMoves.append(eachPiece)
        if randomSeed >= 0:
            random.seed(randomSeed)
        try:
            randomlyChosenPiece = random.choice(validMoves)
            self.place(randomlyChosenPiece[0], randomlyChosenPiece[1], randomlyChosenPiece[2], randomlyChosenPiece[3])
        except IndexError:
            pass

    def getCoordinatesAroundUnit(self, givenCoordinates):
        toReturn = []
        bufferList = []
        bufferList.append([givenCoordinates[0], givenCoordinates[1] - 1, givenCoordinates[2]])
        bufferList.append([givenCoordinates[0] + 1, givenCoordinates[1], givenCoordinates[2]])
        bufferList.append([givenCoordinates[0], givenCoordinates[1] + 1, givenCoordinates[2]])
        bufferList.append([givenCoordinates[0] - 1, givenCoordinates[1], givenCoordinates[2]])
        bufferList.append([givenCoordinates[0], givenCoordinates[1], givenCoordinates[2] - 1])
        bufferList.append([givenCoordinates[0], givenCoordinates[1], givenCoordinates[2] + 1])
        for eachUnit in bufferList:
            if eachUnit[0] >= 0 and eachUnit[0] <= 5 and eachUnit[1] >= 0 \
                    and eachUnit[1] <= 5 and eachUnit[2] >= 0 and eachUnit[2] <= 1:
                toReturn.append(eachUnit)
        return toReturn

    def getValueOfUnit(self, unit):
        try:
            if unit[2] == 0:
                return self.l[unit[1]][unit[0]]
            else:
                return self.m[unit[1]][unit[0]]
        except IndexError:
            print("This piece has no honor: %s" % unit)

    def getCoordinatesForPiece(self, piece):
        return self.coordlist[piece - 1]

    def getAllZerosForPiece(self, piece):
        coordinateListForPiece = self.getCoordinatesForPiece(piece)
        setOfCoordinatesAroundPiece = set()
        listOfZeroCoordinate = []
        for eachUnit in coordinateListForPiece:
            l = self.getCoordinatesAroundUnit(eachUnit)
            for eachUnitAroundUnit in l:
                setOfCoordinatesAroundPiece.add(tuple(i for i in eachUnitAroundUnit))
        for eachUnitFound in setOfCoordinatesAroundPiece:
            if 0 == self.getValueOfUnit(list(eachUnitFound)):
                listOfZeroCoordinate.append(list(eachUnitFound))
        return listOfZeroCoordinate

    def placeRandomPieces(self, numberOfPieces):
        for _ in range(0, numberOfPieces):
            zerosForLastPiece = self.getAllZerosForPiece(len(self.coordlist))
            try:
                randomZero = random.choice(zerosForLastPiece)
            except IndexError:
                pass #cuz you don't have anywhere to move.
            self.placeRandomPiece(randomZero)

    def prettyprint(self):
        s = [[str(e) for e in row] for row in self.l]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))
        sys.stdout.write("\r\n--------------------\r\n")
        
        #print('-----------------')

        s = [[str(e) for e in row] for row in self.m]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        sys.stdout.write('\n'.join(table))
        sys.stdout.write("  \r\n")
        sys.stdout.write("  \r\n")
        sys.stdout.write("CPI: %s\r\n" % self.currentPieceIndex)
        sys.stdout.write("CZI: %s\r\n" % self.currentZeroIndex)
        sys.stdout.flush()
    def getAllZeroUnitsInPuzzle(self):
        listOfCoordinate = []
        for y, eachRow in enumerate(self.l):
            for x, eachItem in enumerate(eachRow):
                if eachItem == 0:
                    listOfCoordinate.append([x, y, 0])
        for y, eachRow in enumerate(self.m):
            for x, eachItem in enumerate(eachRow):
                if eachItem == 0:
                    listOfCoordinate.append([x, y, 1])
        return listOfCoordinate

    def isUnsolvable(self):
        allZeros = self.getAllZeroUnitsInPuzzle()
        for eachZeroUnit in allZeros:
            if len(self.getValidPieces(eachZeroUnit)) == 0:
                return True
        return False

    def getValidPieces(self, unit):
        validPieces = self.getValidMoves(unit)
        validMoves = []
        for eachPiece in validPieces:
            if self.isTetrinoSpaceEmpty(eachPiece[0], eachPiece[1], eachPiece[2], eachPiece[3]):
                validMoves.append(eachPiece)
        return validMoves

    def unplaceLatestPiece(self):
        for eachUnit in self.coordlist[-1]:
            if eachUnit[2] == 1:
                self.m[eachUnit[1]][eachUnit[0]] = 0
            else:
                self.l[eachUnit[1]][eachUnit[0]] = 0
        getLastPiece = self.coordlist[-1]
        self.coordlist.remove(getLastPiece)
        self.currentBlock -= 1

    def isCurrentPieceInvalid(self):
        currentPiece = len(self.coordlist)
        allZerosForNewestPiece = self.getAllZerosForPiece(currentPiece)
        whichZeroToTryForCurrentPiece = self.currentZeroIndex[currentPiece]
        if whichZeroToTryForCurrentPiece == len(allZerosForNewestPiece):
            return True
        return False
        
    def isValidNextState(self):
        currentPiece = len(self.coordlist)
        allZerosForNewestPiece = self.getAllZerosForPiece(currentPiece)
        whichZeroToTryForCurrentPiece = self.currentZeroIndex[currentPiece]
        zeroUnitCoordinates = allZerosForNewestPiece[whichZeroToTryForCurrentPiece]
        allValidMovesForChosenZeroUnit = self.getValidPieces(zeroUnitCoordinates)
        if not allValidMovesForChosenZeroUnit:
            return False
        return True

    def setNextState(self):
        currentPiece = len(self.coordlist)
        allZerosForNewestPiece = self.getAllZerosForPiece(currentPiece)
        whichZeroToTryForCurrentPiece = self.currentZeroIndex[currentPiece]
        zeroUnitCoordinates = allZerosForNewestPiece[whichZeroToTryForCurrentPiece]
        allValidMovesForChosenZeroUnit = self.getValidPieces(zeroUnitCoordinates)
        try:
            uOne = allValidMovesForChosenZeroUnit[self.currentPieceIndex[currentPiece]][0]
        except IndexError:
            pass
        uTwo = allValidMovesForChosenZeroUnit[self.currentPieceIndex[currentPiece]][1]
        uThree = allValidMovesForChosenZeroUnit[self.currentPieceIndex[currentPiece]][2]
        uFour = allValidMovesForChosenZeroUnit[self.currentPieceIndex[currentPiece]][3]
        self.place(uOne, uTwo, uThree, uFour)
        self.currentPieceIndex[currentPiece] += 1
        if self.currentPieceIndex[currentPiece] >= len(allValidMovesForChosenZeroUnit):
            self.currentZeroIndex[currentPiece] += 1
            self.currentPieceIndex[currentPiece] = 0

    def makeAllHigherPieceAndZeroIndexesZero(self, currentPiece):
        for i in range(len(self.currentPieceIndex)):
            if i >= (currentPiece - 1):
                self.currentPieceIndex[i] = 0
        for i in range(len(self.currentZeroIndex)):
            if i >= (currentPiece - 1):
                self.currentZeroIndex[i] = 0


    def backtrackNonRecursive(self):
        currentPiece = len(self.coordlist)
        while currentPiece < 18:
            self.prettyprint()
            if self.isCurrentPieceInvalid():
                self.currentPieceIndex[len(self.coordlist)] = 0
                self.currentZeroIndex[len(self.coordlist)] = 0
                self.makeAllHigherPieceAndZeroIndexesZero(currentPiece)
                self.unplaceLatestPiece()
                self.unplaceLatestPiece()
            elif self.isValidNextState():
                self.setNextState()
                if self.isUnsolvable():
                    self.unplaceLatestPiece()
            else:
                self.currentPieceIndex[currentPiece] += 1
                allZerosForNewestPiece = self.getAllZerosForPiece(currentPiece)
                whichZeroToTryForCurrentPiece = self.currentZeroIndex[currentPiece]
                zeroUnitCoordinates = allZerosForNewestPiece[whichZeroToTryForCurrentPiece]
                allValidMovesForChosenZeroUnit = self.getValidPieces(zeroUnitCoordinates)
                if self.currentPieceIndex[currentPiece] >= len(allValidMovesForChosenZeroUnit):
                    self.currentZeroIndex[currentPiece] += 1
                    self.currentPieceIndex[currentPiece] = 0
                self.unplaceLatestPiece()
            currentPiece = len(self.coordlist)

    def getPossibleMovesFor(self, piece):
        """
        piece 0
          3
        0 1 2

         piece 1
          2
         31
          0

         piece 2
          2
          13
          0

         piece 3
           2 1 0
             3

         piece 4
            2
            1
            0

         piece 5
          0 1 2

         piece 6
          2 3 0

         piece 7
          2
          3
          0
        """
        toReturn = []
        for i in range(0, 72):
            if piece == 0:
                if (8+i) < 72:
                    if not ((8+i) % 6 == 0):
                        if not ((1 + i) % 6 == 0):
                           toReturn.append([1+i, 6+i, 7+i, 8+i])
            if piece == 1:
                if (13 + i) < 72:
                    if not ((1 + i) % 6 == 0):
                        if ((1 + i) > 0):
                            toReturn.append([1 + i, 6 + i, 7 + i, 13 + i])
            if piece == 2:
                if (13 + i) < 72:
                    if not ((7 + i) % 6 == 0):
                        toReturn.append([0 + i, 6 + i, 7 + i, 12 + i])
            if piece == 3:
                if (7 + i) < 72:
                    if not ((2 + i) % 6 == 0):
                        if not((1 + i) % 6 == 0):
                            toReturn.append([0 + i, 1 + i, 2 + i, 7 + i])
            if piece == 4:
                if (12 + i) < 36:
                    toReturn.append([0 + i, 6 + i, 12 + i, 42 + i])
            if piece == 5:
                if (2 + i) < 36:
                    if not ((2 + i) % 6 == 0):
                        if not ((1 + i) % 6 == 0):
                            toReturn.append([0 + i, 1 + i, 2 + i, 37 + i])
            if piece == 6:
                if (38 + i) < 72:
                    if not ((38 + i) % 6 == 0):
                        if not ((37 + i) % 6 == 0):
                            toReturn.append([36 + i, 37 + i, 38 + i, 1 + i])
            if piece == 7:
                if (48 + i) < 72:
                    toReturn.append([36 + i, 42 + i, 48 + i, 6 + i])
        return toReturn

    def appendConstraints(self, numberOfPieceConstraints, numberOfPiece):
        toReturn = []
        for i in range(0, numberOfPieceConstraints):
            toReturn.append(0)
        toReturn[numberOfPiece] = 1
        return toReturn

    def createValidPieceAlgorithmRow(self, piecePosition):
        toReturn = []
        for i in range(0, 72):
            toReturn.append(0)
        for eachPosition in piecePosition:
            toReturn[eachPosition] = 1
        return toReturn

    def rowCreate(self, piecePosition, numberOfConstraintPieces, numberOfPiece):
        return self.createValidPieceAlgorithmRow(piecePosition) + self.appendConstraints(numberOfConstraintPieces, numberOfPiece)

    def getAlgorithmXMatrix(self, pieces):
        matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]]
        for i, eachPiece in enumerate(pieces):
            for eachValidPlacement in self.getPossibleMovesFor(eachPiece):
                matrix.append(self.rowCreate(eachValidPlacement, len(pieces), i))
        return matrix

    def removeAppropriateRowsAndColumns(self, matrix, chosenRow):
        newMatrix = [matrix[0]]
        columnsToRemove = set()
        for columnIndex, eachValue in enumerate(chosenRow):
            if eachValue == 1:
                columnsToRemove.add(matrix[0][columnIndex])
        for matrixRowNumber, eachRow in enumerate(matrix):
            if matrixRowNumber > 0:
                addRow = True
                for i, eachValue in enumerate(chosenRow):
                    if eachValue == 1:
                        if eachRow[i] == 1:
                            addRow = False
                            break
                if addRow:
                    newMatrix.append(eachRow)
        #remove columns
        matrixToReturn = []
        listOfColumnsToRemove = list(columnsToRemove)
        listOfColumnsToRemove = sorted(listOfColumnsToRemove)
        listOfColumnsToRemove = listOfColumnsToRemove[::-1]
        for rowsInNewMatrix in newMatrix:
            newRow = rowsInNewMatrix.copy()
            for eachColumnIndexToRemove in listOfColumnsToRemove:
                newRow.pop(matrix[0].index(eachColumnIndexToRemove))
            matrixToReturn.append(newRow)

        return matrixToReturn

    def getColumn(self, matrix, columnIndex):
        toReturn = []
        for eachRow in matrix:
            toReturn.append(eachRow[columnIndex])
        return toReturn

    def listOfRowIndexesContainingAOneInTheLeftmostColumnWithTheFewestOnes(self, matrix):
        """
        return a list of row indexes of a given matrix that happen to contain a one in the column
        which contains the fewest ones and is leftmost.
        """
        toReturn = []
        sumOfEachColumnList = []
        minSum = 9999999999 #ugh shitty max sum...
        indexOfColumnWithLeftmostMinSum = -1
        for i in range(0, len(matrix[0])):
            eachColumn = self.getColumn(matrix, i)
            sumOfEachColumn = sum(eachColumn[1:])
            if sumOfEachColumn < minSum:
                minSum = sumOfEachColumn
            sumOfEachColumnList.append(sumOfEachColumn)
        for index, eachSum in enumerate(sumOfEachColumnList):
            if eachSum == minSum:
                indexOfColumnWithLeftmostMinSum = index
                break
        for rowIndex, eachRow in enumerate(matrix):
            if rowIndex > 0:
                if eachRow[indexOfColumnWithLeftmostMinSum] == 1:
                    toReturn.append(rowIndex)
        return toReturn

    def shouldBacktrack(self, matrix):
        for i in range(0, len(matrix[0])):
            eachColumn = self.getColumn(matrix, i)
            if sum(eachColumn[1:]) == 0:
                return True
                break
        return False

    def getBetterWayOfReturningRow(self, chosenRow, header):
        toReturn = []
        for indexInRow, eachItem in enumerate(chosenRow):
            if eachItem == 1:
                toReturn.append(header[indexInRow])
        return toReturn

    def recurse(self, matrix):
        if matrix == [[]]:
            self.thisIsSolved = True
            return self.solution
        else:
            listOfRowsToTry = self.listOfRowIndexesContainingAOneInTheLeftmostColumnWithTheFewestOnes(matrix)
            for eachRow in listOfRowsToTry:
                chosenRow = self.getBetterWayOfReturningRow(matrix[eachRow], matrix[0])
                self.solution.append(chosenRow)
                newMatrix = self.removeAppropriateRowsAndColumns(matrix, matrix[eachRow])
                if newMatrix and not self.shouldBacktrack(newMatrix):
                    self.recurse(newMatrix)
                if self.thisIsSolved:
                    break
                if not self.thisIsSolved:
                    self.solution.remove(chosenRow)
        


