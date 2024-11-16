import random
from typing import List


class Cell:
    def __init__(self, around_mines: int = 0, mine: bool = False) -> None:
        self.around_mines: int = around_mines
        self.mine: bool = mine
        self.fl_open: bool = False

    def __repr__(self) -> str:
        return f"Cell(mine={self.mine}, around_mines={self.around_mines}, fl_open={self.fl_open})"


class GamePole:
    def __init__(self, N: int, M: int) -> None:
        self.N: int = N
        self.M: int = M
        self.pole: List[List[Cell]] = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self) -> None:
        mines_set: int = 0
        while mines_set < self.M:
            i: int = random.randint(0, self.N - 1)
            j: int = random.randint(0, self.N - 1)
            if not self.pole[i][j].mine:
                self.pole[i][j].mine = True
                mines_set += 1
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    self.pole[i][j].around_mines = self.count_mines_around(i, j)

    def count_mines_around(self, i: int, j: int) -> int:
        directions: List[tuple[int, int]] = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        ]
        count: int = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.N and 0 <= nj < self.N and self.pole[ni][nj].mine:
                count += 1
        return count

    def show(self) -> None:
        for row in self.pole:
            row_str: str = ""
            for cell in row:
                row_str += "* " if cell.fl_open and cell.mine else f"{cell.around_mines} " if cell.fl_open else "# "
            print(row_str)
        print()



