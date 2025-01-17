import socket, time

host = "127.0.0.1"
port = 5000

buffer_size = 126
rep = 62000//buffer_size

file_name = "recordings\VortEx_test02.udp"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

f = open(file_name, "rb")
data = f.read(buffer_size)

start_time = time.perf_counter()
print("Sending...")
i=0
while len(data)==126:
    # Should run 10 times each second ~ 0.9 seconds sleep and 0.1 second of sending the code.
    if (sock.sendto(data, (host, port))):
        data = f.read(buffer_size)
    if (i%rep==0):
        time.sleep(0.09) 
    i+=1
print(i)
print(time.perf_counter()-start_time)
sock.close()
f.close()