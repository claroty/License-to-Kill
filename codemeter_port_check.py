import socket
import sys


if len(sys.argv) != 2:
	print("Usage: {} IP_ADDR".format(sys.argv[0]))
	sys.exit(1)

ip_address = sys.argv[1]
port = 22350
timeout = 5


sock = socket.socket(2,1)
sock.settimeout(timeout)
try:
	sock.connect((ip_address, port))
	sock.send("73616d63000000004100010000000000".decode("hex"))
	recv_data = sock.recv(1024)

	if recv_data.startswith(b"samc"):
		print("[V] CodeMeter instace detected!")
	else:
		print("[X] No CodeMeter instace detected")
except Exception as e:
	print("[X] Timeout")