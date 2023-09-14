import socket

def main():
	# 创建套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 绑定端口
	local = ("",2002)
	tcp_socket.bind(local)
	
	# 链接服务器
	dest_ip = input("请输入下载服务器的ip：")
	dest_port = int(input("请输入下载服务器的port："))
	tcp_socket.connect((dest_ip, dest_port))
	
	# 发送文件名称
	send_file_name = input("请输入下载的文件名称：")
	tcp_socket.send(send_file_name.encode("utf-8"))
	
	# 接收数据
	recv_data = tcp_socket.recv(1024)
	
	# 写入数据
	# 因为是用"utf-8"收到的，是（二进制）编码，所以用b
	if recv_data:
		with open("[新]"+send_file_name,"wb") as f:
			f.write(recv_data)
	
	# 关闭套接字
	tcp_socket.close()


if __name__ == "__main__":
	main()
