import random
from typing import List, Tuple


class Cell:
    """
    Класс, представляющий ячейку на игровом поле.

    Attributes:
        surrounding_mines (int): Количество мин вокруг данной ячейки.
        has_mine (bool): Присутствие мины в ячейке.
        is_open (bool): Открыта ли ячейка (для отображения).
    """

    def __init__(
            self,
            surrounding_mines: int = 0,
            has_mine: bool = False
    ) -> None:
        """
        Инициализация ячейки.

        Args:
            surrounding_mines (int): Количество мин вокруг ячейки.
            has_mine (bool): Признак наличия мины в ячейке.
        """
        self.surrounding_mines: int = surrounding_mines
        self.has_mine: bool = has_mine
        self.is_open: bool = False

    def __repr__(self) -> str:
        """Возвращает строковое представление ячейки для отладки."""
        return (
            f"Cell(has_mine={self.has_mine},"
            f" surrounding_mines={self.surrounding_mines},"
            f" is_open={self.is_open})"
        )


class Minefield:
    """
    Класс, представляющий игровое поле 'Сапёр'.

    Attributes:
        grid_size (int): Размер поля (NxN).
        num_mines (int): Количество мин на поле.
        grid (List[List[Cell]]): Матрица ячеек, представляющая игровое поле.
    """

    def __init__(
            self,
            grid_size: int,
            num_mines: int
    ) -> None:
        """
        Инициализация игрового поля.

        Args:
            grid_size (int): Размер игрового поля (NxN).
            num_mines (int): Количество мин, которые будут размещены на поле.
        """
        self.grid_size: int = grid_size
        self.num_mines: int = num_mines
        self.grid: List[List[Cell]] = [
            [Cell() for _ in range(grid_size)] for _ in range(grid_size)
        ]
        self.place_mines_and_count_surroundings()

    def place_mines_and_count_surroundings(self) -> None:
        """
        Размещает мины на поле и вычисляет количество мин вокруг каждой ячейки.
        """
        mines_placed: int = 0
        while mines_placed < self.num_mines:
            row: int = random.randint(0, self.grid_size - 1)
            col: int = random.randint(0, self.grid_size - 1)
            if not self.grid[row][col].has_mine:
                self.grid[row][col].has_mine = True
                mines_placed += 1

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if not self.grid[row][col].has_mine:
                    self.grid[row][col].surrounding_mines = self.count_surrounding_mines(row, col)

    def count_surrounding_mines(
            self,
            row: int,
            col: int
    ) -> int:
        """
        Считает количество мин вокруг заданной ячейки.

        Args:
            row (int): Номер строки ячейки.
            col (int): Номер столбца ячейки.

        Returns:
            int: Количество мин вокруг ячейки.
        """
        directions: List[Tuple[int, int]] = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        mine_count: int = 0
        for d_row, d_col in directions:
            neighbor_row, neighbor_col = row + d_row, col + d_col
            if 0 <= neighbor_row < self.grid_size and 0 <= neighbor_col < self.grid_size:
                if self.grid[neighbor_row][neighbor_col].has_mine:
                    mine_count += 1
        return mine_count

    def display(self) -> None:
        """
        Отображает игровое поле в консоли.
        Закрытые ячейки обозначаются '#', мины '*', открытые ячейки числом мин вокруг них.
        """
        for row in self.grid:
            row_str: str = ""
            for cell in row:
                if cell.is_open:
                    row_str += "* " if cell.has_mine else f"{cell.surrounding_mines} "
                else:
                    row_str += "# "
            print(row_str)
        print()

