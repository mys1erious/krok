import dns
import dns.resolver
import socket


def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]]+result[1]
    except socket.herror:
        return None


def dns_request(domain):
    ips = []
    try:
        result = dns.resolver.resolve(domain)
        if result:
            print('\n', domain)
            for answer in result:
                print(answer)
                print(f"Domain Names: {reverse_dns(answer.to_text())}")
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return []
    return ips


def subdomain_search(domain, subdomains, nums=False):
    for subdomain in subdomains:
        full_subdomain = subdomain+"."+domain
        dns_request(full_subdomain)
        if nums:
            for i in range(0, 10):
                s = subdomain+str(i)+"."+domain
                dns_request(s)


if __name__ == '__main__':
    domain = "google.com"
    subdomain_paths = "subdomains.txt"

    with open(subdomain_paths, "r") as f:
        subdomains = f.read().splitlines()

    subdomain_search(domain, subdomains, True)
