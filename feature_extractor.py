import re
import tldextract


def extract_features(url):

    features = []

    features.append(len(url))

    features.append(url.count('.'))

    features.append(url.count('-'))

    features.append(url.count('@'))

    features.append(sum(c.isdigit() for c in url))

    features.append(1 if "https" in url else 0)

    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'

    features.append(
        1 if re.search(ip_pattern, url)
        else 0
    )

    suspicious_words = [
        'login',
        'secure',
        'verify',
        'update',
        'account',
        'banking'
    ]

    count = 0

    for word in suspicious_words:
        if word in url.lower():
            count += 1

    features.append(count)

    extracted = tldextract.extract(url)

    subdomains = extracted.subdomain

    if subdomains:
        features.append(len(subdomains.split('.')))
    else:
        features.append(0)

    return features
