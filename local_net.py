from typing import Optional, Dict, List
from dataclasses import dataclass


@dataclass
class Data:
    """
    Класс, представляющий пакет данных.

    Attributes:
        data (str): Содержимое пакета данных.
        ip (int): IP-адрес сервера назначения.
    """
    data: str
    ip: int


class Server:
    """
    Класс, представляющий сервер.

    Attributes:
        ip_counter (int): Счётчик для генерации уникальных IP-адресов.
        ip (int): Уникальный IP-адрес сервера.
        buffer (List[Data]): Буфер для хранения полученных пакетов данных.
    """
    ip_counter: int = 1

    def __init__(self) -> None:
        """
        Инициализация сервера с уникальным IP-адресом.
        """
        self.ip: int = self.ip_counter
        Server.ip_counter += 1
        self.buffer: List[Data] = []

    def send_data(
        self,
        data: str,
        destination_ip: int,
        router: 'Router'
    ) -> Optional[List[Data]]:
        """
        Отправляет пакет данных через указанный роутер.

        Args:
            data (str): Содержимое пакета данных.
            destination_ip (int): IP-адрес сервера назначения.
            router (Router): Экземпляр роутера для отправки данных.

        Returns:
            Optional[List[Data]]: Текущий буфер данных сервера.
        """
        packet = Data(data, destination_ip)
        router.buffer.append(packet)
        return self.buffer

    def get_data(self) -> List[Data]:
        """
        Возвращает все данные из буфера и очищает его.

        Returns:
            List[Data]: Список пакетов данных из буфера.
        """
        received_data = self.buffer.copy()
        self.buffer.clear()
        return received_data

    def get_ip(self) -> int:
        """
        Возвращает IP-адрес сервера.

        Returns:
            int: IP-адрес сервера.
        """
        return self.ip


class Router:
    """
    Класс, представляющий роутер для передачи данных между серверами.

    Attributes:
        connected_servers (Dict[int, Server]): Словарь подключённых серверов с их IP-адресами.
        buffer (List[Data]): Буфер для хранения пакетов данных, ожидающих отправки.
    """

    def __init__(self) -> None:
        """
        Инициализация роутера с пустым списком подключённых серверов и буфером данных.
        """
        self.connected_servers: Dict[int, Server] = {}
        self.buffer: List[Data] = []

    def link(self, server: Server) -> None:
        """
        Подключает сервер к роутеру.

        Args:
            server (Server): Экземпляр сервера для подключения.
        """
        self.connected_servers[server.get_ip()] = server

    def unlink(self, server: Server) -> None:
        """
        Отключает сервер от роутера.

        Args:
            server (Server): Экземпляр сервера для отключения.
        """
        self.connected_servers.pop(server.get_ip(), None)

    def send_data(self) -> None:
        """
        Отправляет все пакеты данных из буфера на соответствующие сервера.
        """
        for packet in self.buffer:
            destination_server = self.connected_servers.get(packet.ip)
            if destination_server:
                destination_server.buffer.append(packet)
        self.buffer.clear()

