import socket
import ssl
import requests
import dns.resolver
import pandas as pd
import tldextract
import tld
from urllib.parse import urlparse


def extract_asn_ip_from_url(url):
    parsed_url = urlparse(url)
    netloc_parts = parsed_url.netloc.split(":")
    ip_address = netloc_parts[0]
    asn = parsed_url.path.strip("/")
    return asn


def perform_whois_lookup(url):
    domain = tldextract.extract(url).registered_domain
    whois_url = f"https://www.whois.com/whois/{domain}"
    response = requests.get(whois_url)
    return response.text


def extract_features(url):
    features = {}

    # Check if URL is empty
    if not url:
        # Return zero values for each feature
        features['time_response'] = 0
        features['domain_spf'] = 0
        features['qty_ip_resolved'] = 0
        features['qty_nameservers'] = 0
        features['qty_mx_servers'] = 0
        features['ttl_hostname'] = 0
        features['tls_ssl_certificate'] = 0
        features['qty_redirects'] = 0
        features['url_google_index'] = 0
        features['domain_google_index'] = 0
        features['url_shortened'] = 0

        # Return the features as a DataFrame
        return pd.DataFrame(features, index=[0])

    # Perform domain lookup and measure the response time
    try:
        domain_ip = socket.gethostbyname(url)
        features['time_response'] = float(socket.gethostbyname_ex(url)[-1][-1])
    except socket.gaierror:
        features['time_response'] = 0
    except socket.error:
        features['time_response'] = 0

    # features['asn_ip'] = extract_asn_ip_from_url(url)

    # Check if the domain has SPF (using WHOIS lookup)
    try:
        whois_info = perform_whois_lookup(url)
        spf_present = "SPF" in whois_info.upper()
        features['domain_spf'] = int(spf_present)
    except requests.exceptions.RequestException:
        features['domain_spf'] = 0

    # Get the number of resolved IPs
    try:
        resolved_ips = socket.getaddrinfo(url, None)
        features['qty_ip_resolved'] = len(resolved_ips)
    except (socket.gaierror, socket.herror):
        features['qty_ip_resolved'] = 0

    # # Get the number of resolved nameservers
    # try:
    #     ns_records = dns.resolver.resolve(url, 'NS')
    #     features['qty_nameservers'] = len(ns_records)
    # except dns.resolver.NXDOMAIN:
    #     features['qty_nameservers'] = 0
    #
    # # Get the number of MX servers
    # try:
    #     mx_records = dns.resolver.resolve(url, 'MX')
    #     features['qty_mx_servers'] = len(mx_records)
    # except dns.resolver.NXDOMAIN:
    #     features['qty_mx_servers'] = 0

    # Get the TTL (Time-To-Live) for the hostname
    try:
        ttl = socket.gethostbyname_ex(url)[-1][-1]
        features['ttl_hostname'] = int(ttl)
    except (socket.gaierror, socket.herror):
        features['ttl_hostname'] = 0

    # Check if the TLS/SSL certificate is valid
    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()
                features['tls_ssl_certificate'] = int(bool(cert))
    except (socket.gaierror, ssl.SSLError, ConnectionRefusedError):
        features['tls_ssl_certificate'] = 0

    # Get the number of redirects
    try:
        redirects = len(requests.get(url).history)
        features['qty_redirects'] = redirects
    except (requests.exceptions.RequestException, requests.exceptions.URLRequired):
        features['qty_redirects'] = 0

    # Check if the URL is indexed on Google
    try:
        indexed = bool(requests.get(f'https://www.google.com/search?q={url}').text)
        features['url_google_index'] = int(indexed)
    except (requests.exceptions.RequestException, requests.exceptions.URLRequired):
        features['url_google_index'] = 0

    # Check if the domain is indexed on Google
    try:
        indexed = bool(requests.get(f'https://www.google.com/search?q=site:{url}').text)
        features['domain_google_index'] = int(indexed)
    except (requests.exceptions.RequestException, requests.exceptions.URLRequired):
        features['domain_google_index'] = 0

    # Check if the URL is shortened
    features['url_shortened'] = int(len(url) <= 15)

    return pd.DataFrame(features, index=[0])
