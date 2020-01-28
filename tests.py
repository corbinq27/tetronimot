import unittest
from solver import Solver


class TestSolver(unittest.TestCase):

    def testPlaceTetrinoUpperLeft(self):
        solver = Solver()
        solver.reset()
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        expectedL = [
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        expectedM = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(expectedL, solver.l)
        self.assertEqual(expectedM, solver.m)

    def testReset(self):
        solver = Solver()
        solver.reset()
        expectedL = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        expectedM = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(expectedL, solver.l)
        self.assertEqual(expectedM, solver.m)

    def testUnitIsValid(self):
        solver = Solver()
        solver.reset()
        actual = solver._isUnitEmpty([0, 0, 0])
        self.assertTrue(actual)

    def testCheckPlaceIsValid(self):
        solver = Solver()
        solver.reset()
        isValid = solver.isTetrinoSpaceEmpty([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        self.assertTrue(isValid)

    def testCheckPlaceIsInvalid(self):
        solver = Solver()
        solver.reset()
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        isValid = solver.isTetrinoSpaceEmpty([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        self.assertFalse(isValid)

    def testAddSecondBlockAndItIsMarkedWithNumberTwos(self):
        solver = Solver()
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        solver.place([0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1])
        expectedL = [
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        expectedM = [
            [2, 1, 0, 0, 0, 0],
            [2, 2, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(expectedL, solver.l)
        self.assertEqual(expectedM, solver.m)

    def testSecondBlockIsDetectedByisTetrinoSpaceEmpty(self):
        solver = Solver()
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        solver.place([0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1])
        actual = solver.isTetrinoSpaceEmpty([0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1])
        self.assertFalse(actual)

    def testNumberOfValidMovesForUnsurroundedUnit(self):
        solver = Solver()
        validMoveCount = len(solver._getValidMoves([2, 2, 0]))
        self.assertEqual(32, validMoveCount)

    # def testExpectedValidMovesAreReturnedForZeroUnit(self):
    #     solver = Solver()
    #     expectedValidMoves = [
    #         [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, -1, 0]],  # x_|_
    #         [[0, 0, 0], [0, -1, 0], [0, -2, 0], [-1, -1, 0]],  # -|
    #         # x
    #         [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, 1, 0]],  # Tx
    #         [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 1, 0]],  # x
    #         # |-
    #         [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 1, 0]],  # XT
    #         [[0, 0, 0], [0, -1, 0], [0, -2, 0], [1, -1, 0]],  # |-
    #         # x
    #         [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, -1, 0]],  # _|_x
    #         # x
    #         [[0, 0, 0], [0, 1, 0], [0, 2, 0], [-1, 1, 0]],  # -|
    #         [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1]],  # x---
    #         [[0, 0, 0], [0, -1, 0], [0, -2, 0], [0, -1, 1]],  # |
    #         # x
    #         [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, 0, 1]],  # ---x
    #         [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1]],  # x
    #         # |
    #         [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, -1]],  # x---
    #         [[0, 0, 0], [0, -1, 0], [0, -2, 0], [0, -1, -1]],  # |
    #         # x
    #         [[0, 0, 0], [-1, 0, 0], [-2, 0, 0], [-1, 0, -1]],  # ---x
    #         [[0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, -1]],  # x
    #         # |
    #         [[0, 0, 0], [0, -1, -1], [0, 0, -1], [0, 1, -1]],  # |
    #         # x
    #         # |
    #         [[0, 0, 0], [0, -1, 1], [0, 0, 1], [0, 1, 1]],  # |
    #         # |X (Tetrino is |- but is rotated 90 degrees left)
    #         # |
    #         [[0, 0, 0], [-1, 0, -1], [1, 0, -1], [0, 0, -1]],  # -x-
    #         [[0, 0, 0], [-1, 0, 1], [1, 0, 1], [0, 0, 1]],
    #         # --- (Tetrino is _|_ but rotated 90 degrees away (into the page))
    #         #  x
    #         [[0, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, 1]]
    #
    #
    #     ]
    #     actualValidMoves = solver._getValidMoves([0, 0, 0])
    #     self.assertEqual(expectedValidMoves, actualValidMoves)

    def testExpectedValidMovesAreReturnedForZeroUnitValid(self):
        solver = Solver()
        expectedValidMoves = [
            [[0, 0, 0], [0, 2, 0], [0, 1, 0], [1, 1, 0]],
            [[0, 0, 0], [2, 0, 0], [1, 0, 0], [1, 1, 0]],
            [[0, 0, 0], [0, 2, 0], [0, 1, 0], [0, 1, 1]],
            [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1]]]
        actualValidMoves = solver.getValidMoves([0, 0, 0])
        self.assertEqual(expectedValidMoves, actualValidMoves)

    # def testMoreExpectedValidMoves(self):
    #     solver = Solver()
    #     expectedValidMoves = [
    #                           [[5, 1, 1], [4, 1, 1], [3, 1, 1], [4, 2, 1]],
    #                           [[5, 1, 1], [4, 1, 1], [3, 1, 1], [4, 0, 1]],
    #                           [[5, 1, 1], [5, 2, 1], [5, 3, 1], [4, 2, 1]],
    #                           [[5, 1, 1], [4, 1, 1], [3, 1, 1], [4, 1, 0]],
    #                           [[5, 1, 1], [5, 2, 1], [5, 3, 1], [5, 2, 0]],
    #                           [[5, 1, 1], [5, 0, 0], [5, 1, 0], [5, 2, 0]]]
    #     actualValidMoves = solver.getValidMoves([5,1,1])
    #     print(actualValidMoves)
    #     self.assertEqual(expectedValidMoves, actualValidMoves)

    # def testExpectedValidMovesWorkWithNewX(self):
    #     solver = Solver()
    #     expectedValidMoves = [
    #         [[1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0]],  # x
    #                                                        # |-
    #         [[1, 0, 0], [2, 0, 0], [3, 0, 0], [2, 1, 0]],  # XT
    #         [[1, 0, 0], [1, 1, 0], [1, 2, 0], [0, 1, 0]],  # #
    #                                                        # -|
    #         [[1, 0, 0], [2, 0, 0], [3, 0, 0], [2, 0, 1]],  # x---
    #         [[1, 0, 0], [1, 1, 0], [1, 2, 0], [1, 1, 1]],  # x
    #                                                        # |
    #         [[1, 0, 0], [0, 0, 1], [2, 0, 1], [1, 0, 1]]  # -X-
    #
    #     ]
    #     actualValidMoves = solver.getValidMoves([1, 0, 0])
    #     self.assertEqual(expectedValidMoves, actualValidMoves)

    # def testExpectedValidMovesWorkWithNewXNewY(self):
    #     solver = Solver()
    #     expectedValidMoves = [
    #         [[1, 1, 0], [2, 1, 0], [3, 1, 0], [2, 0, 0]],  # x_|_
    #         [[1, 1, 0], [1, 2, 0], [1, 3, 0], [2, 2, 0]],  # x
    #         # |-
    #         [[1, 1, 0], [2, 1, 0], [3, 1, 0], [2, 2, 0]],  # XT
    #         [[1, 1, 0], [1, 2, 0], [1, 3, 0], [0, 2, 0]],  # #
    #         # -|
    #         [[1, 1, 0], [2, 1, 0], [3, 1, 0], [2, 1, 1]],  # x---
    #         [[1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 2, 1]],  # x
    #         # |
    #         [[1, 1, 0], [1, 0, 1], [1, 1, 1], [1, 2, 1]],
    #         [[1, 1, 0], [0, 1, 1], [2, 1, 1], [1, 1, 1]],
    #         [[1, 1, 0], [1, 0, 0], [1, 2, 0], [1, 1, 1]]
    #
    #     ]
    #     actualValidMoves = solver.getValidMoves([1, 1, 0])
    #     self.assertEqual(expectedValidMoves, actualValidMoves)

    # def testExpectedValidMovesWorkWithNewXNewYNewZ(self):
    #     solver = Solver()
    #     expectedValidMoves = [
    #         [[1, 1, 1], [2, 1, 1], [3, 1, 1], [2, 0, 1]],  # x_|_
    #         [[1, 1, 1], [1, 2, 1], [1, 3, 1], [2, 2, 1]],  # x
    #         # |-
    #         [[1, 1, 1], [2, 1, 1], [3, 1, 1], [2, 2, 1]],  # XT
    #         [[1, 1, 1], [1, 2, 1], [1, 3, 1], [0, 2, 1]],  # #
    #         # -|
    #         [[1, 1, 1], [2, 1, 1], [3, 1, 1], [2, 1, 0]],  # x---
    #         [[1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 2, 0]],  # x
    #         # |
    #         [[1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 2, 0]],
    #         [[1, 1, 1], [0, 1, 0], [2, 1, 0], [1, 1, 0]]
    #     ]
    #     actualValidMoves = solver.getValidMoves([1, 1, 1])
    #     self.assertEqual(expectedValidMoves, actualValidMoves)

    def testPlaceRandomlySituatedPieceAtZero(self):
        solver = Solver()
        expectedL = [  # negatives signify that we care that they are simply not zero
            [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        expectedM = [
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        solver.placeRandomPiece([0, 0, 0], 0)
        self.assertEqual(expectedL, solver.l)
        self.assertEqual(expectedM, solver.m)

    def testGetCoordinatesAroundUnit(self):
        givenCoordinates = [1, 1, 1]
        expectedCoordinates = [[1, 0, 1], [2, 1, 1], [1, 2, 1], [0, 1, 1], [1, 1, 0]]

        solver = Solver()
        actualCoordinates = solver.getCoordinatesAroundUnit(givenCoordinates)
        self.assertEqual(expectedCoordinates, actualCoordinates)

    def testGetValueOfUnit(self):
        givenUnit = [1, 1, 1]

        solver = Solver()
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        self.assertEqual(0, solver.getValueOfUnit(givenUnit))

    def testGetValueOfUnitOne(self):
        givenUnit = [2, 0, 0]

        solver = Solver()
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        self.assertEqual(1, solver.getValueOfUnit(givenUnit))

    def testGetCoordinatesForPiece(self):
        solver = Solver();
        pieceOne = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1]]
        pieceTwo = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1]]
        solver.place(pieceOne[0], pieceOne[1], pieceOne[2], pieceOne[3])
        solver.place(pieceTwo[0], pieceTwo[1], pieceTwo[2], pieceTwo[3])
        self.assertEqual(solver.getCoordinatesForPiece(1), pieceOne)
        self.assertEqual(solver.getCoordinatesForPiece(2), pieceTwo)

    def testGetAllZerosAroundAPiece(self):
        solver = Solver()
        # solver.l = 	[[1,1,1,0,0,0],
        # 	[3,3,3,0,0,0],
        # 	[0,3,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0]
        # ]
        # solver.m = 	[[2,1,0,0,0,0],
        # 	[2,2,0,0,0,0],
        # 	[2,0,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0]
        # ]
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        solver.place([0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1])
        solver.place([0, 1, 0], [1, 1, 0], [2, 1, 0], [2, 1, 0])
        # TODO I have to actually call place for these pieces or this won't work.
        actualZeros = solver.getAllZerosForPiece(1)
        self.assertEqual([[3, 0, 0], [2, 0, 1]], actualZeros)

    def testGetAllZerosAroundADifferentPiece(self):
        solver = Solver()
        # solver.l = 	[[1,1,1,0,0,0],
        # 	[3,3,3,0,0,0],
        # 	[0,3,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0]
        # ]
        # solver.m = 	[[2,1,0,0,0,0],
        # 	[2,2,0,0,0,0],
        # 	[2,0,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0],
        # 	[0,0,0,0,0,0]
        # ]
        solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 0, 1])
        solver.place([0, 0, 1], [0, 1, 1], [0, 2, 1], [1, 1, 1])
        solver.place([0, 1, 0], [1, 1, 0], [2, 1, 0], [2, 1, 0])
        # TODO I have to actually call place for these pieces or this won't work.
        actualZeros = solver.getAllZerosForPiece(2)
        self.assertEqual([[1, 2, 1], [0, 2, 0], [2, 1, 1], [0, 3, 1]], actualZeros)

    def testGetSquareOnLevelOneWithFourPieces(self):

        solution = [
            [1, 1, 1, 4, 0, 0],
            [2, 1, 4, 4, 0, 0],
            [2, 2, 3, 4, 0, 0],
            [2, 3, 3, 3, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        hasSolutionBeenFound = False
        count = 0
        while (not hasSolutionBeenFound):
            solver = Solver()
            solver.place([0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 1, 0])
            solver.place([0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 2, 0])
            solver.placeRandomPieces(2)
            count += 1
            if solver.l == solution:
                hasSolutionBeenFound = True
        print("%s tried" % count)
        self.assertEqual(solver.l, solution)

    def testNaiveSolver(self):
        # x 0   1   2   3   4   5   y z = 0
        expectedl = [[10, 1, 2, 2, 2, 17],  # 0
                     [10, 1, 1, 2, 3, 17],  # 1
                     [10, 1, 4, 3, 3, 17],  # 2
                     [11, 4, 4, 4, 3, 16],  # 3
                     [11, 11, 12, 13, 16, 16],  # 4
                     [11, 12, 12, 12, 15, 16]]  # 5

        # x 0  1   2   3   4   5   y z = 1
        expectedm = [[7, 7, 7, 6, 6, 6],  # 0
                     [10, 7, 8, 5, 6, 17],  # 1
                     [9, 8, 8, 5, 5, 18],  # 2
                     [9, 9, 8, 5, 18, 18],  # 3
                     [9, 14, 13, 13, 13, 18],  # 4
                     [14, 14, 14, 15, 15, 15]]  # 5

        hasSolutionBeenFound = False
        count = 0
        maxPlacedPieces = 0
        while (not hasSolutionBeenFound):
            solver = Solver()
            solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
            solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
            solver.place([4, 1, 0], [4, 2, 0], [4, 3, 0], [3, 2, 0])  # 3
            solver.place([2, 2, 0], [3, 3, 0], [2, 3, 0], [1, 3, 0])  # 4
            solver.place([3, 1, 1], [3, 2, 1], [4, 2, 1], [3, 3, 1])  # 5
            solver.place([3, 0, 1], [4, 0, 1], [4, 1, 1], [5, 0, 1])  # 6
            solver.place([0, 0, 1], [1, 0, 1], [2, 0, 1], [1, 1, 1])  # 7
            solver.place([2, 1, 1], [2, 2, 1], [2, 3, 1], [1, 2, 1])  # 8
            solver.place([0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 3, 1])  # 9
            solver.place([0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1])  # 10
            solver.place([0, 3, 0], [0, 4, 0], [0, 5, 0], [1, 4, 0])  # 11
            solver.place([1, 5, 0], [2, 5, 0], [2, 4, 0], [3, 5, 0])  # 12
            solver.place([3, 4, 0], [2, 4, 1], [3, 4, 1], [4, 4, 1])  # 13
            solver.place([0, 5, 1], [1, 4, 1], [1, 5, 1], [2, 5, 1])  # 14
            solver.place([4, 5, 0], [3, 5, 1], [4, 5, 1], [5, 5, 1])  # 15
            solver.place([5, 3, 0], [5, 4, 0], [5, 5, 0], [4, 4, 0])  # 16

            solver.placeRandomPieces(2)
            count += 1
            if count % 100000 == 0:
                print("%s tried." % count)
            if len(solver.coordlist) > maxPlacedPieces:
                maxPlacedPieces = len(solver.coordlist)
                print("%s have been placed." % maxPlacedPieces)
            if len(solver.coordlist) == 17:
                print("%s have been placed." % maxPlacedPieces)
                print(solver.l)
                print(solver.m)
            if 18 == len(solver.coordlist):
                hasSolutionBeenFound = True
        print(solver.l)
        print(solver.m)

    def testGetAllZeroUnitsReturnsExpectedNumberOfUnitsEmpty(self):
        solver = Solver()
        self.assertEquals(72, len(solver.getAllZeroUnitsInPuzzle()))

    def testGetAllZeroUnitsReturnsExpectedNumberOfUnitsTwoPiecesPlaced(self):
        solver = Solver()
        solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
        solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
        self.assertEquals(64, len(solver.getAllZeroUnitsInPuzzle()))

    def testGetAllZeroUnitsReturnsExpectedNumberOfUnitsTwoPlacedPiecesAreNotInZeroList(self):
        solver = Solver()
        units = [[1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0]]
        solver.place(units[0], units[1], units[2], units[3])  # 1
        solver.place(units[4], units[5], units[6], units[7])  # 2
        listOfZeros = solver.getAllZeroUnitsInPuzzle()
        self.assertTrue(not units[0] in listOfZeros)
        self.assertTrue(not units[1] in listOfZeros)
        self.assertTrue(not units[2] in listOfZeros)
        self.assertTrue(not units[3] in listOfZeros)
        self.assertTrue(not units[4] in listOfZeros)
        self.assertTrue(not units[5] in listOfZeros)
        self.assertTrue(not units[6] in listOfZeros)
        self.assertTrue(not units[7] in listOfZeros)
        self.assertTrue([5, 5, 1] in listOfZeros)

    def testIsUnsolvableCleanGame(self):
        solver = Solver()
        self.assertFalse(solver.isUnsolvable())

    def testIsUnsolvableIsFalse(self):
        solver = Solver()
        units = [[1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0], [2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0]]
        solver.place(units[0], units[1], units[2], units[3])  # 1
        solver.place(units[4], units[5], units[6], units[7])  # 2
        self.assertFalse(solver.isUnsolvable())

    def testIsUnsolvableIsTrue(self):
        solver = Solver()
        units = [[1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0],
                 [2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0],
                 [1, 0, 1], [1, 1, 1], [1, 2, 1], [2, 1, 1],
                 [3, 0, 1], [4, 0, 1], [5, 0, 1], [4, 1, 1]
                 ]
        solver.place(units[0], units[1], units[2], units[3])  # 1
        solver.place(units[4], units[5], units[6], units[7])  # 2
        solver.place(units[8], units[9], units[10], units[11])  # 3
        solver.place(units[12], units[13], units[14], units[15])  # 4
        solver.prettyprint()
        self.assertTrue(solver.isUnsolvable())

    def testUnplace(self):
        expectedl = [
            [1, 1, 1, 0, 0, 0],
            [2, 1, 0, 0, 0, 0],
            [2, 2, 3, 0, 0, 0],
            [2, 3, 3, 3, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        solver = Solver()

        units = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [1, 1, 0],
                 [0, 1, 0], [0, 2, 0], [0, 3, 0], [1, 2, 0],
                 [1, 3, 0], [2, 3, 0], [3, 3, 0], [2, 2, 0],
                 [3, 0, 0], [3, 1, 0], [3, 2, 0], [2, 1, 0]
                 ]
        solver.place(units[0], units[1], units[2], units[3])  # 1
        solver.place(units[4], units[5], units[6], units[7])  # 2
        solver.place(units[8], units[9], units[10], units[11])  # 3
        solver.place(units[12], units[13], units[14], units[15])  # 4
        # solver.prettyprint()
        solver.unplaceLatestPiece()
        # solver.prettyprint()
        self.assertEqual(3, len(solver.coordlist))
        self.assertEqual(expectedl, solver.l)

    def testUnplaceRemovesValuesFromArrays(self):
        solver = Solver()
        units = [[1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0],
                 [2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0],
                 [1, 0, 1], [1, 1, 1], [1, 2, 1], [2, 1, 1],
                 [3, 0, 1], [4, 0, 1], [5, 0, 1], [4, 1, 1]
                 ]
        solver.place(units[0], units[1], units[2], units[3])  # 1
        solver.place(units[4], units[5], units[6], units[7])  # 2
        solver.place(units[8], units[9], units[10], units[11])  # 3
        solver.place(units[12], units[13], units[14], units[15])  # 4
        solver.unplaceLatestPiece()
        self.assertEqual(solver.currentZeroIndex, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.assertEqual(solver.currentPieceIndex, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def testSetNextState(self):
        expectedm = [
            [0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0],
            [2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]

        solver = Solver()

        solver.place([0,0,0], [1,0,0], [2,0,0], [1,1,0])
        solver.setNextState()
        self.assertEqual(expectedm, solver.m)

    def testBacktrackingFinalPiece(self):
                   # x 0   1   2   3   4   5   y z = 0
        expectedl = [[10,  1,  2,  2,  2,  17],  # 0
                     [10,  1,  1,  2,  3,  17],  # 1
                     [10,  1,  4,  3,  3,  17],  # 2
                     [11,  4,  4,  4,  3,  16],  # 3
                     [11,  11, 12, 13, 16, 16],  # 4
                     [11,  12, 12, 12, 15, 16]]  # 5

                  # x 0  1   2   3   4   5   y z = 1
        expectedm = [[7,  7, 7,  6,  6,  6],  # 0
                     [10, 7, 8,  5,  6,  17],  # 1
                     [9,  8, 8,  5,  5,  18],  # 2
                     [9,  9, 8,  5,  18, 18],  # 3
                     [9, 14, 13, 13, 13, 18],  # 4
                     [14,14, 14, 15, 15, 15]]  # 5

        solver = Solver()
        solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
        solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
        solver.place([4, 1, 0], [4, 2, 0], [4, 3, 0], [3, 2, 0])  # 3
        solver.place([2, 2, 0], [3, 3, 0], [2, 3, 0], [1, 3, 0])  # 4
        solver.place([3, 1, 1], [3, 2, 1], [4, 2, 1], [3, 3, 1])  # 5
        solver.place([3, 0, 1], [4, 0, 1], [4, 1, 1], [5, 0, 1])  # 6
        solver.place([0, 0, 1], [1, 0, 1], [2, 0, 1], [1, 1, 1])  # 7
        solver.place([2, 1, 1], [2, 2, 1], [2, 3, 1], [1, 2, 1])  # 8
        solver.place([0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 3, 1])  # 9
        solver.place([0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1])  # 10
        solver.place([0, 3, 0], [0, 4, 0], [0, 5, 0], [1, 4, 0])  # 11
        solver.place([1, 5, 0], [2, 5, 0], [2, 4, 0], [3, 5, 0])  # 12
        solver.place([3, 4, 0], [2, 4, 1], [3, 4, 1], [4, 4, 1])  # 13
        solver.place([0, 5, 1], [1, 4, 1], [1, 5, 1], [2, 5, 1])  # 14
        solver.place([4, 5, 0], [3, 5, 1], [4, 5, 1], [5, 5, 1])  # 15
        solver.place([5, 3, 0], [5, 4, 0], [5, 5, 0], [4, 4, 0])  # 16
        solver.place([5, 0, 0], [5, 1, 0], [5, 2, 0], [5, 1, 1])  # 17
        solver.backtrackNonRecursive()
        self.assertEqual(expectedl, solver.l)
        self.assertEqual(expectedm, solver.m)

    def testBacktrackingFinalTwoPieces(self):
                   # x 0   1   2   3   4   5   y z = 0
        expectedl = [[10,  1,  2,  2,  2,  18],  # 0
                     [10,  1,  1,  2,  3,  18],  # 1
                     [10,  1,  4,  3,  3,  18],  # 2
                     [11,  4,  4,  4,  3,  16],  # 3
                     [11,  11, 12, 13, 16, 16],  # 4
                     [11,  12, 12, 12, 15, 16]]  # 5

                  # x 0  1   2   3   4   5   y z = 1
        expectedm = [[7,  7, 7,  6,  6,  6],  # 0
                     [10, 7, 8,  5,  6,  18],  # 1
                     [9,  8, 8,  5,  5,  17],  # 2
                     [9,  9, 8,  5,  17, 17],  # 3
                     [9, 14, 13, 13, 13, 17],  # 4
                     [14,14, 14, 15, 15, 15]]  # 5

        solver = Solver()
        solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
        solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
        solver.place([4, 1, 0], [4, 2, 0], [4, 3, 0], [3, 2, 0])  # 3
        solver.place([2, 2, 0], [3, 3, 0], [2, 3, 0], [1, 3, 0])  # 4
        solver.place([3, 1, 1], [3, 2, 1], [4, 2, 1], [3, 3, 1])  # 5
        solver.place([3, 0, 1], [4, 0, 1], [4, 1, 1], [5, 0, 1])  # 6
        solver.place([0, 0, 1], [1, 0, 1], [2, 0, 1], [1, 1, 1])  # 7
        solver.place([2, 1, 1], [2, 2, 1], [2, 3, 1], [1, 2, 1])  # 8
        solver.place([0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 3, 1])  # 9
        solver.place([0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1])  # 10
        solver.place([0, 3, 0], [0, 4, 0], [0, 5, 0], [1, 4, 0])  # 11
        solver.place([1, 5, 0], [2, 5, 0], [2, 4, 0], [3, 5, 0])  # 12
        solver.place([3, 4, 0], [2, 4, 1], [3, 4, 1], [4, 4, 1])  # 13
        solver.place([0, 5, 1], [1, 4, 1], [1, 5, 1], [2, 5, 1])  # 14
        solver.place([4, 5, 0], [3, 5, 1], [4, 5, 1], [5, 5, 1])  # 15
        solver.place([5, 3, 0], [5, 4, 0], [5, 5, 0], [4, 4, 0])  # 16
        solver.backtrackNonRecursive()
        self.assertEqual(expectedl, solver.l)
        self.assertEqual(expectedm, solver.m)
        
    def testBacktrackingFinalTwoPiecesForceBacktracking(self):
                   # x 0   1   2   3   4   5   y z = 0
        expectedl = [[10,  1,  2,  2,  2,  18],  # 0
                     [10,  1,  1,  2,  3,  18],  # 1
                     [10,  1,  4,  3,  3,  18],  # 2
                     [11,  4,  4,  4,  3,  16],  # 3
                     [11,  11, 12, 13, 16, 16],  # 4
                     [11,  12, 12, 12, 15, 16]]  # 5

                  # x 0  1   2   3   4   5   y z = 1
        expectedm = [[7,  7, 7,  6,  6,  6],  # 0
                     [10, 7, 8,  5,  6,  18],  # 1
                     [9,  8, 8,  5,  5,  17],  # 2
                     [9,  9, 8,  5,  17, 17],  # 3
                     [9, 14, 13, 13, 13, 17],  # 4
                     [14,14, 14, 15, 15, 15]]  # 5

        solver = Solver()
        solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
        solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
        solver.place([4, 1, 0], [4, 2, 0], [4, 3, 0], [3, 2, 0])  # 3
        solver.place([2, 2, 0], [3, 3, 0], [2, 3, 0], [1, 3, 0])  # 4
        solver.place([3, 1, 1], [3, 2, 1], [4, 2, 1], [3, 3, 1])  # 5
        solver.place([3, 0, 1], [4, 0, 1], [4, 1, 1], [5, 0, 1])  # 6
        solver.place([0, 0, 1], [1, 0, 1], [2, 0, 1], [1, 1, 1])  # 7
        solver.place([2, 1, 1], [2, 2, 1], [2, 3, 1], [1, 2, 1])  # 8
        solver.place([0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 3, 1])  # 9
        solver.place([0, 0, 0], [0, 1, 0], [0, 2, 0], [0, 1, 1])  # 10
        solver.place([0, 3, 0], [0, 4, 0], [0, 5, 0], [1, 4, 0])  # 11
        solver.place([1, 5, 0], [2, 5, 0], [2, 4, 0], [3, 5, 0])  # 12
        solver.place([3, 4, 0], [2, 4, 1], [3, 4, 1], [4, 4, 1])  # 13
        solver.place([0, 5, 1], [1, 4, 1], [1, 5, 1], [2, 5, 1])  # 14
        solver.place([4, 5, 0], [3, 5, 1], [4, 5, 1], [5, 5, 1])  # 15
        solver.place([5, 3, 0], [5, 4, 0], [5, 5, 0], [4, 4, 0])  # 16
        solver.place([5,1,1], [5,2,1], [5,3,1], [5,2,0]) #17 in an unsolvable move
        
        solver.backtrackNonRecursive()
        self.assertEqual(expectedl, solver.l)
        self.assertEqual(expectedm, solver.m)

    def testThisZeroIsNotUnolvable(self):
        solver = Solver()
        solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
        solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
        solver.place([4, 1, 0], [4, 2, 0], [4, 3, 0], [3, 2, 0])  # 3
        solver.place([2, 2, 0], [3, 3, 0], [2, 3, 0], [1, 3, 0])  # 4
        solver.place([2, 4, 0], [3, 4, 0], [4, 4, 0], [3, 5, 0])  # 5
        solver.place([5, 4, 0], [5, 3, 0], [5, 5, 0], [5, 4, 1])  # 6
        solver.place([5, 3, 1], [4, 3, 1], [3, 3, 1], [4, 4, 1])  # 7
        solver.place([3, 2, 1], [2, 2, 1], [1, 2, 1], [2, 3, 1])  # 8
        solver.place([0, 2, 1], [0, 3, 1], [1, 3, 1], [0, 4, 1])  # 9
        self.assertFalse(solver.isUnsolvable())

    def convertExpectedArraysToPlaceCalls(self, expectedl, expectedm):
        sortedPieces = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        maxPiece = 1
        for i, eachRow in enumerate(expectedl):
            for j, eachUnit in enumerate(eachRow):
                if eachUnit > 0:
                    sortedPieces[eachUnit-1].append([i,j,0])
                    if eachUnit > maxPiece:
                        maxPiece = eachUnit
        for k, eachRows in enumerate(expectedm):
            for l, eachUnits in enumerate(eachRows):
                if eachUnits > 0:
                    sortedPieces[eachUnits-1].append([k,l,1])
                    if eachUnits > maxPiece:
                        maxPiece = eachUnits
        while len(sortedPieces) > maxPiece:
            sortedPieces.pop(-1)
        return sortedPieces
    
    #This is the big one.  Running this will do the nonrecursive backtracking solution. takes 30 minutes.
    def testBacktrackingFromAVeryLongWaysAway(self):
        solver = Solver()
        solver.place([1, 0, 0], [1, 1, 0], [1, 2, 0], [2, 1, 0])  # 1
        solver.place([2, 0, 0], [3, 0, 0], [4, 0, 0], [3, 1, 0])  # 2
        solver.place([4, 1, 0], [4, 2, 0], [4, 3, 0], [3, 2, 0])  # 3
        solver.place([2, 2, 0], [3, 3, 0], [2, 3, 0], [1, 3, 0])  # 4
        solver.place([2, 4, 0], [3, 4, 0], [4, 4, 0], [3, 5, 0])  # 5
        solver.place([5, 4, 0], [5, 3, 0], [5, 5, 0], [5, 4, 1])  # 6
        solver.place([5, 3, 1], [4, 3, 1], [3, 3, 1], [4, 4, 1])  # 7
        solver.place([3, 2, 1], [2, 2, 1], [1, 2, 1], [2, 3, 1])  # 8
        solver.backtrackNonRecursive()
        print("COMPLETED!")
        solver.prettyprint()
        print("COMPLETED!!")

if __name__ == '__main__':
    unittest.main()
