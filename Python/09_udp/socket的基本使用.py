import socket

def main():
        # 创建一个udp套接字
	socket_test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 可以使用套接字收发数据
	socket_test.sendto(b"I love Michelle", ("192.168.43.1", 5200))


	# 关闭套接字
	socket_test.close()


if __name__ == '__main__':
	main
