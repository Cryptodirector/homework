from typing import (
    Optional,
    TypeVar,
    List,
    Self,
    Generic
)

# Определение универсального типа
T = TypeVar('T')


class ObjList(Generic[T]):
    """
    Класс, представляющий элемент связного списка.

    Attributes:
        _next (Optional[Self]): Ссылка на следующий элемент списка.
        _prev (Optional[Self]): Ссылка на предыдущий элемент списка.
        _data (T): Хранимые данные в элементе.
    """

    def __init__(self, data: T) -> None:
        """
        Инициализация элемента списка с данными.

        Args:
            data (T): Данные, которые будут храниться в элементе.
        """
        self._next: Optional[Self] = None
        self._prev: Optional[Self] = None
        self._data: T = data

    def set_next(self, obj: Optional[Self]) -> None:
        """
        Устанавливает ссылку на следующий элемент списка.

        Args:
            obj (Optional[Self]): Следующий элемент списка.
        """
        self._next = obj

    def set_prev(self, obj: Optional[Self]) -> None:
        """
        Устанавливает ссылку на предыдущий элемент списка.

        Args:
            obj (Optional[Self]): Предыдущий элемент списка.
        """
        self._prev = obj

    def get_next(self) -> Optional[Self]:
        """
        Возвращает следующий элемент списка.

        Returns:
            Optional[Self]: Следующий элемент списка или None.
        """
        return self._next

    def get_prev(self) -> Optional[Self]:
        """
        Возвращает предыдущий элемент списка.

        Returns:
            Optional[Self]: Предыдущий элемент списка или None.
        """
        return self._prev

    def set_data(self, data: T) -> None:
        """
        Устанавливает данные для текущего элемента.

        Args:
            data (T): Новые данные для элемента.
        """
        self._data = data

    def get_data(self) -> T:
        """
        Возвращает данные, хранящиеся в элементе.

        Returns:
            T: Данные элемента.
        """
        return self._data


class LinkedList(Generic[T]):
    """
    Класс, представляющий двусвязный список.

    Attributes:
        head (Optional[ObjList[T]]): Первый элемент списка.
        tail (Optional[ObjList[T]]): Последний элемент списка.
    """

    def __init__(self) -> None:
        """
        Инициализация пустого связного списка.
        """
        self.head: Optional[ObjList[T]] = None
        self.tail: Optional[ObjList[T]] = None

    def add_obj(self, obj: ObjList[T]) -> None:
        """
        Добавляет элемент в конец связного списка.

        Args:
            obj (ObjList[T]): Элемент для добавления в список.
        """
        if self.tail is None:
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self) -> None:
        """
        Удаляет последний элемент из связного списка.
        """
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            if self.tail:
                self.tail.set_next(None)

    def get_data(self) -> List[T]:
        """
        Возвращает все данные из связного списка.

        Returns:
            List[T]: Список данных, хранящихся в элементах связного списка.
        """
        data_list: List[T] = []
        current = self.head
        while current:
            data_list.append(current.get_data())
            current = current.get_next()
        return data_list
