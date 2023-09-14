import socket

def main():
        # 创建一个udp套接字
	socket_test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	# 提示用户输入数据
	send_data = input("请输入你想发送的数据：")


	# 可以使用套接字发数据
	socket_test.sendto(send_data.encode("utf-8"), ("192.168.43.1", 5200))


	# 关闭套接字
	socket_test.close()


if __name__ == '__main__':
	main
