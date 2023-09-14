import socket


def main():
	# 创建套接字
	tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# 绑定端口
	local = ("",2003)
	tcp_server.bind(local)
	
	# 被动链接
	tcp_server.listen()
	
	while True:	
		# 等待链接
		tem_server, slient_infor = tcp_server.accept()
		
		# 等待数据
		# 两个点后面的是对前面的返回值进行处理
		recv_data = tem_server.recv(1024).decode("utf-8")
		print("客户%s想要下载的文件是%s" % (slient_infor, recv_data))
		
		# 读取文件
		send_content = None
		# with 的前提是open可以打开，在保证可以打开的情况下才用open
		try:
			f = open(recv_data, "rb")
			send_content = f.read()
			f.close()
		except:
			print("没有要发送的%s" % recv_data)
		
		# 发送数据
		if send_content:
			tem_server.send(send_content)
		
		# 关闭套接字
		tem_server.close()
		
		
	tcp_server.close()

if __name__ == "__main__":
	main()
