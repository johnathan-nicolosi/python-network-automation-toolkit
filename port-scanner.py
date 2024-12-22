import socket
import ipaddress

def is_port_open(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

# Function to scan network for open hosts
def scan_network(network, port):
    open_hosts = []
    for ip in ipaddress.IPv4Network(network):
        if is_port_open(str(ip), port):
            open_hosts.append(str(ip))
    return open_hosts

def main():
    network = input("Enter the network range (e.g., 192.168.1.0/24): ")
    port = int(input("Enter a port number (e.g., 22, 80, 443): "))
    output_file = "scan_results.txt"
    
    try:
        ipaddress.IPv4Network(network)  # Validate the network range
    except ValueError:
        print("Invalid network range")
        return
    
    print(f"Scanning network {network} for open port {port}...")
    open_hosts = scan_network(network, port)
    
    with open(output_file, 'w') as f:
        if open_hosts:
            print(f"Devices with port {port} open:")
            #f.write(f"Devices with port {port} open:\n")
            for host in open_hosts:
                print(host)
                f.write(f"{host}\n")
        else:
            print(f"No devices with port {port} open found on the network {network}.")
            f.write(f"No devices with port {port} open found on the network {network}.\n")
    
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
