import re
import pandas as pd


def extract_url_features(url):
    features = {}

    # Check if URL is empty
    if not url:
        # Return an empty DataFrame
        return pd.DataFrame()

    # Number of "." signs
    features['qty_dot_url'] = url.count('.')

    # Number of "-" signs
    features['qty_hyphen_url'] = url.count('-')

    # Number of "_" signs
    features['qty_underline_url'] = url.count('_')

    # Number of "/" signs
    features['qty_slash_url'] = url.count('/')

    # Number of "?" signs
    features['qty_questionmark_url'] = url.count('?')

    # Number of "=" signs
    features['qty_equal_url'] = url.count('=')

    # Number of "@" signs
    features['qty_at_url'] = url.count('@')

    # Number of "&" signs
    features['qty_and_url'] = url.count('&')

    # Number of "!" signs
    features['qty_exclamation_url'] = url.count('!')

    # Number of space signs
    features['qty_space_url'] = url.count(' ')

    # Number of "~" signs
    features['qty_tilde_url'] = url.count('~')

    # Number of "," signs
    features['qty_comma_url'] = url.count(',')

    # Number of "+" signs
    features['qty_plus_url'] = url.count('+')

    # Number of "*" signs
    features['qty_asterisk_url'] = url.count('*')

    # Number of "#" signs
    features['qty_hashtag_url'] = url.count('#')

    # Number of "$" signs
    features['qty_dollar_url'] = url.count('$')

    # Number of "%" signs
    features['qty_percent_url'] = url.count('%')

    # Top level domain character length
    tld = re.findall(r'\.([a-zA-Z]+)$', url)
    features['qty_tld_url'] = len(tld[0]) if tld else 0

    # Number of characters
    features['length_url'] = len(url)

    # Is email present
    features['email_in_url'] = bool(re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', url))

    return pd.DataFrame(features, index=[0])



