import socket


udp_socket_practise = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)




instr = (input("请输入你想发送的内容：")
inip = input("请输入目标ip：")
inport =int(input("请输入目标端口："))

udp_socket_practise.sendto(instr.encode("utf-8"),(inip,inport))



udp_socket_practise.close()



