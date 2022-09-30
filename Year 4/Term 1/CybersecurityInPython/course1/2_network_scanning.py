from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, TCP, UDP
from scapy.sendrecv import sr


def syn_scan(host, ports):
    # ans - open ports
    # unans - closed ports
    ans, unans = sr(
        IP(dst=host) / TCP(dport=list(ports), flags="S"),
        timeout=2, verbose=0
    )

    ports_msg = f'Open ports at {host}: '
    for (sent, received) in ans:
        if sent.haslayer(TCP) and received.haslayer(TCP):
            if sent[TCP].dport == received[TCP].sport:
                ports_msg += f'{sent[TCP].dport} '
    print(ports_msg)


def dns_scan(host):
    ans, unans = sr(
        IP(dst=host) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="google.com")),
        timeout=2, verbose=0
    )
    if ans:
        print(f"DNS Server at {host}")


if __name__ == '__main__':
    ports = [25, 80, 53, 443, 445, 8080, 8443]
    host = "8.8.8.8"
    syn_scan(host, ports)
    dns_scan(host)
