import socket
import sys
try:
	from netaddr import IPNetwork
except Exception as e:
	print("[-] Please install netaddr package.")
	print("\tpython -m pip install netaddr --user")
	sys.exit(1)


TIMEOUT_SEC = 1
PORT = 22350
try:
	PAYLOAD = bytes.fromhex("73616d63000000004100010000000000")
except Exception as e:
	PAYLOAD = "73616d63000000004100010000000000".decode("hex")
RESP_DETECT = b"samc"

def scan_ip(ip_addr, timeout=TIMEOUT_SEC):
	is_detected = False
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(timeout)
	try:
		sock.connect((ip_addr, PORT))
		sock.send(PAYLOAD)
		recv_data = sock.recv(1024)
		if recv_data.startswith(RESP_DETECT):
			is_detected = True
			print("[V] {}: CodeMeter instace detected!".format(ip_addr))
		sock.close()
	except Exception as e:
		pass
	if not is_detected:
		print("[X] {}: Did not detect CodeMeter Runtime.".format(ip_addr))

def main():
	if len(sys.argv) < 2:
		print("Usage: {} IP_ADDR_OR_SUBNET [TIMEOUT (optional)]".format(sys.argv[0]))
		print("Example: {} 192.168.1.0/24 0.5".format(sys.argv[0]))
		sys.exit(1)

	try:
		ip_addresses = IPNetwork(sys.argv[1])
		timeout = float(sys.argv[2]) if len(sys.argv) == 3 else TIMEOUT_SEC
	except Exception as e:
		print("Usage: {} IP_ADDR_OR_SUBNET [TIMEOUT (optional)]".format(sys.argv[0]))
		print("Example: {} 192.168.1.0/24 0.5".format(sys.argv[0]))
		sys.exit(1)

	print("[-] CodeMeter Runtime Port Scanner Started")
	print("[-] Starting to scan {} ({} IPs) with timeout of {} seconds".format(str(ip_addresses), len(ip_addresses), timeout))
	for ip_addr in ip_addresses:
		scan_ip(str(ip_addr), timeout=timeout)
	print("[-] Done")

main()