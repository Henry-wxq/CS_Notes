import socket


# 每次定义和使用函数时都要考虑是否需要参数加入
def send_data(a):
    dest_ip = input("请输入目标ip：")
    dest_port = int(input("请输入目标端口："))
    message = input("请输入想发送的数据：")
    a.sendto(message.encode("utf-8"), (dest_ip, dest_port))


def recv_data(b):
    rec = b.recvfrom(1024)
    print("%s:%s" % (str(rec[1]), rec[0].decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local = ("", 5200)
    udp_socket.bind(local)

    while True:
        # 发送数据
        send_data(udp_socket)

        # 接收数据
        recv_data(udp_socket)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
