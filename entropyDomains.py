#!/usr/bin/env python3

from collections import Counter
import math
from sys import argv
from urllib.parse import urlparse

# function to calculate the entropy of the domain
def calculate_entropy(domain):
    p, lns = Counter(domain), float(len(domain))
    return -sum(count/lns * math.log2(count/lns) for count in p.values())

# function to read a file and parse the domains, removing subdomains and returning entropy scores
def process_domains_file(filename):
    with open(filename, 'r') as file:
        domains = [line.strip() for line in file.readlines()]

    newDomains = []

    for i in domains:
        if len(i.split(".")) > 2:
            newDomains.append('.'.join(urlparse(i).path.split('.')[1:]))
        else:
            newDomains.append(i)

    entropies = []
    for domain in newDomains:
        entropy = calculate_entropy(list(domain))
        entropies.append((domain, entropy))

    return entropies

# main function to take file as argument, run file through functions, sort the result and return only higher
# than 3 entropy score
def main():
    if len(argv) > 2:
        filename = argv
    elif len(argv) == 2:
        filename = argv[1]

    try:
        results = process_domains_file(filename)
    except Exception as e:
        print(f"\nYou must provide a file as an argument with this script.\n")
        exit(1)

    sortedDict = sorted(results, key=lambda x:x[1], reverse=True)

    for domain, entropy in sortedDict:
        if entropy > 3:
            print(f"Entropy for '{domain}': {entropy:.2f}")

if __name__ == "__main__":
    main()
