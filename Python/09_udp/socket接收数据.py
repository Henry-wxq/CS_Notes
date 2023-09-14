import socket

def main():

# 创建套接字
	udp_test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 绑定端口
	local = ("",5200)
	udp_test.bind(local)

	# 接收数据
	while True:
		result = udp_test.recvfrom(1024)

		# 打印数据
		data = result[0]
		dest = result[1]
		print("%s;%s" % (str(dest),data.decode("utf-8")))

	# 关闭套接字
	udp_test.close()

if __name__ == "__main__":
	main()






