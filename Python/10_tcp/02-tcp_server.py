import socket


def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 绑定ip和port
	local = ("", 2001)
	socket_server.bind(local)
	
	# 被动链接
	socket_server.listen()
	while True:
			
	# 等待链接
		tem_socket, client_address = socket_server.accept()
		print(client_address)
	
		while True:
		# 接收数据
			rev = tem_socket.recv(1024)
			print(rev.decode("utf-8"))
		
			if rev == b"exit":
			# 发送数据
				send_data = input("请输入要发送的数据:")
				tem_socket.send(send_data.encode("utf-8"))
			
			elif rev == b"close":
				break
			
		tem_socket.close()
	
	# 关闭套接字
	socket_server.close()

	
	
	
if __name__ == "__main__":
	main()



