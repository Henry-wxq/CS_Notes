import socket

def main():
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 绑定端口
	local = ("",2000)
	tcp_socket.bind(local)

	# 连接服务器
	server_ip = input("请输入服务器的ip:")
	server_port = int(input("请输入服务器的端口:"))
	tcp_socket.connect((server_ip, server_port))
	
	while True:
		while True:
		# 发送数据
			send_data = input("请填写你要发送的数据(输入exit:对方将回复；输入close:服务将终止):")
			tcp_socket.send(send_data.encode("utf-8"))
			

			if send_data == "exit":
				break
            
            # return以后直接整个函数终止
			if send_data == "close":
				return 
			
		# 接收数据
		recv = tcp_socket.recv(1024)
		print(recv.decode("utf-8"))

		 		
		# 关闭套接字
	tcp_socket.close()


if __name__ == "__main__":
	main()






