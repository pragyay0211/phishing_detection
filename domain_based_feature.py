import re
import pandas as pd


def extract_domain_features(url):
    features = {}

    # Check if URL is empty
    if not url:
        # Return zero values for each feature
        features['qty_dot_domain'] = 0
        features['qty_hyphen_domain'] = 0
        features['qty_underline_domain'] = 0
        features['qty_slash_domain'] = 0
        features['qty_questionmark_domain'] = 0
        features['qty_equal_domain'] = 0
        features['qty_at_domain'] = 0
        features['qty_and_domain'] = 0
        features['qty_exclamation_domain'] = 0
        features['qty_space_domain'] = 0
        features['qty_tilde_domain'] = 0
        features['qty_comma_domain'] = 0
        features['qty_plus_domain'] = 0
        features['qty_asterisk_domain'] = 0
        features['qty_hashtag_domain'] = 0
        features['qty_dollar_domain'] = 0
        features['qty_percent_domain'] = 0
        features['qty_vowels_domain'] = 0
        features['domain_length'] = 0
        features['domain_in_ip'] = 0
        features['server_client_domain'] = 0

        # Return the features as a DataFrame
        return pd.DataFrame(features, index=[0])

    # Number of "." signs
    features['qty_dot_domain'] = url.count('.')

    # Number of "-" signs
    features['qty_hyphen_domain'] = url.count('-')

    # Number of "_" signs
    features['qty_underline_domain'] = url.count('_')

    # Number of "/" signs
    features['qty_slash_domain'] = url.count('/')

    # Number of "?" signs
    features['qty_questionmark_domain'] = url.count('?')

    # Number of "=" signs
    features['qty_equal_domain'] = url.count('=')

    # Number of "@" signs
    features['qty_at_domain'] = url.count('@')

    # Number of "&" signs
    features['qty_and_domain'] = url.count('&')

    # Number of "!" signs
    features['qty_exclamation_domain'] = url.count('!')

    # Number of space signs
    features['qty_space_domain'] = url.count(' ')

    # Number of "~" signs
    features['qty_tilde_domain'] = url.count('~')

    # Number of "," signs
    features['qty_comma_domain'] = url.count(',')

    # Number of "+" signs
    features['qty_plus_domain'] = url.count('+')

    # Number of "*" signs
    features['qty_asterisk_domain'] = url.count('*')

    # Number of "#" signs
    features['qty_hashtag_domain'] = url.count('#')

    # Number of "$" signs
    features['qty_dollar_domain'] = url.count('$')

    # Number of "%" signs
    features['qty_percent_domain'] = url.count('%')

    # Number of vowels
    features['qty_vowels_domain'] = sum(1 for char in url if char.lower() in 'aeiou')

    # Number of characters
    features['domain_length'] = len(url)

    # Domain in IP address format
    features['domain_in_ip'] = int(bool(re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', url)))

    # "server" or "client" in domain
    features['server_client_domain'] = int(bool(re.search(r'server|client', url, re.IGNORECASE)))

    return pd.DataFrame(features, index=[0])
