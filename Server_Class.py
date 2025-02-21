class Server:
    count = 0

    def __init__(self, hostname, ip_address, os_type, status):
        self.hostname = hostname
        self.ip = ip_address
        self.os = os_type
        self.status = status
        Server.count += 1
        print(f'Server "', self.hostname, '" has been intialized successfully!')

    def info_server(self):
        return f"Server Info:\nHostname: {self.hostname}\nIP Address: {self.ip}\nOS: {self.os}\nStatus: {self.status}"

    def start_server(self):
        if self.status == "Running":
            return f"{self.hostname} is already running."
        self.status = "Running"
        return f"{self.hostname} has been started."

    def stop_server(self):
        if self.status == "Stopped":
            return f"{self.hostname} is already stopped."
        self.status = "Stopped"
        return f"{self.hostname} has been stopped."

    def restart_server(self):
        self.stop_server()
        self.start_server()
        return f"{self.hostname} has been restarted."


# Creating objects to test

# server1 = Server("Server1", "192.168.1.10", "Linux", "Stopped")

# print(server1.info_server(), '\n')
# print(server1.stop_server(), '\n')
# print(server1.start_server(), '\n')
# print(server1.restart_server(), '\n')
# print(f'Your network has', Server.count, 'servers', '\n')
# print('-' * 30, '\n')

# server2 = Server("Server2", "192.168.1.20", "Windows", "Running")

# print(server2.info_server(), '\n')
# print(server2.start_server(), '\n')
# print(server2.stop_server(), '\n')
# print(server2.restart_server(), '\n')
# print(f'Your network has', Server.count, 'servers')
