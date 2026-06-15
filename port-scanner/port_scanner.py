import socket
import time


def scan_port(host, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()

        return result==0


    except Exception as e:
        print("Error",e)
        return False
def main():

    try:
        host_name=input("enter host name: ")
        start_port=int(input("Enter the starting port: "))
        end_port=int(input("Enter the ending port"))
    except ValueError:
        print("Enter a Number")
        return False

    if start_port < 1 or end_port > 65535:
        print("Ports must be between 1 and 65535")
        return
    if start_port > end_port:
        print("Starting port must be less than ending port")
        return
    try:
        socket.gethostbyname(host_name)
    except socket.gaierror:
        print("invalid host name")
        return


    opend_ports=0
    start_time=time.perf_counter()
    for port in range(start_port,end_port+1):
        if scan_port(host_name,port):
            print(port,"Open")
            opend_ports+=1
    end_time=time.perf_counter()
    scanned_time=end_time-start_time
    print(f"the opend ports is:{opend_ports}")
    print(f"scanned ime is : {scanned_time:.2f} seconds")
if __name__ == "__main__":
    main()
