from typing import Optional, Any, List


class ObjList:
    def __init__(self, data: Any) -> None:
        self._next: Optional[ObjList] = None
        self._prev: Optional[ObjList] = None
        self._data: Any = data

    def set_next(self, obj: Optional['ObjList']) -> None:
        self._next = obj

    def set_prev(self, obj: Optional['ObjList']) -> None:
        self._prev = obj

    def get_next(self) -> Optional['ObjList']:
        return self._next

    def get_prev(self) -> Optional['ObjList']:
        return self._prev

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[ObjList] = None
        self.tail: Optional[ObjList] = None

    def add_obj(self, obj: ObjList) -> None:
        if self.tail is None:
            self.head = self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self) -> None:
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.get_prev()
            if self.tail:
                self.tail.set_next(None)

    def get_data(self) -> List[Any]:
        data_list: List[Any] = []
        current = self.head
        while current:
            data_list.append(current.get_data())
            current = current.get_next()
        return data_list
