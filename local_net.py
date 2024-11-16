from typing import Optional, Dict, List


class Data:
    def __init__(
            self,
            data: str,
            ip: int
    ) -> None:
        self.data: str = data
        self.ip: int = ip


class Server:
    ip_counter: int = 1

    def __init__(self) -> None:
        self.ip: int = Server.ip_counter
        Server.ip_counter += 1
        self.buffer: List[Data] = []

    def send_data(
            self,
            data: str,
            destination_ip: int,
            router: 'Router'
    ) -> Optional[List[Data]]:
        packet = Data(data, destination_ip)
        router.buffer.append(packet)
        return self.buffer

    def get_data(self) -> List[Data]:
        received_data = self.buffer.copy()
        self.buffer.clear()
        return received_data

    def get_ip(self) -> int:
        return self.ip


class Router:
    def __init__(self) -> None:
        self.connected_servers: Dict[int, Server] = {}
        self.buffer: List[Data] = []

    def link(self, server: Server) -> None:
        self.connected_servers[server.get_ip()] = server

    def unlink(self, server: Server) -> None:
        self.connected_servers.pop(server.get_ip(), None)

    def send_data(self) -> None:
        for packet in self.buffer:
            destination_server = self.connected_servers.get(packet.ip)
            if destination_server:
                destination_server.buffer.append(packet)
        self.buffer.clear()



