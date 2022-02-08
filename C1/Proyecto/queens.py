import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class NQueensProblem:
    def __init__(self, numOfQueens):
        self.numOfQueens = numOfQueens

    def __len__(self):
        return self.numOfQueens

    def getViolationsCount(self, positions):
        if len(positions) != self.numOfQueens:
            raise ValueError("El tamaño de la lista de posiciones debería ser igual a: ", self.numOfQueens)

        violations = 0

        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                column1 = i
                row1 = positions[i]
                column2 = j
                row2 = positions[j]

                if abs(column1 - column2) == abs(row1 - row2):
                    violations += 1

        return violations

    def plotBoard(self, positions):
        if len(positions) != self.numOfQueens:
             raise ValueError("El tamaño de la lista de posiciones debería ser igual a: ", self.numOfQueens)

        fig, ax = plt.subplots()
        board = np.zeros((self.numOfQueens, self.numOfQueens))
        board[::2, 1::2] = 1
        board[1::2, ::2] = 1
        ax.imshow(board, interpolation='none', cmap=mpl.colors.ListedColormap(['#000', '#fff']))
        queenThumbnail = plt.imread('queen.png')
        thumbnailSpread = 0.70 * np.array([-1, 1, -1, 1]) / 2

        for i, j in enumerate(positions):
            ax.imshow(queenThumbnail, extent=[j, j, i, i] + thumbnailSpread)

        ax.set(xticks=list(range(self.numOfQueens)), yticks=list(range(self.numOfQueens)))
        ax.axis('image')

        return plt