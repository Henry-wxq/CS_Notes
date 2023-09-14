import socket

def main():

	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	local = ("",5202)
	udp_socket.bind(local)
	
	while True:
		print("functions:")
		print("1:send message")
		print("2.receive message")
		print("0.exit")
		op = input("please choose:")
		
		if op == "1":
			dest_ip = input("please enter the ip address:")
			dest_port = int(input("please enter the port:"))
			send_data = input("please enter what you would like to send:")
		
			udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))
		elif op == "2":
			recv_message = udp_socket.recvfrom(1024)
			print("%s:%s" % (recv_message[1], recv_message[0].decode("utf-8")))
		elif op == "0":
			break
		else:
			print("please choose again")

	udp_socket.close()

if __name__ == "__main__":
	main()
