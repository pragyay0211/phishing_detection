import re
import pandas as pd


def extract_params_features(url):
    features = {}

    # Check if URL is empty
    if not url:
        # Return DataFrame with all columns of zero values
        features = {
            'qty_dot_params': 0,
            'qty_hyphen_params': 0,
            'qty_underline_params': 0,
            'qty_slash_params': 0,
            'qty_questionmark_params': 0,
            'qty_equal_params': 0,
            'qty_at_params': 0,
            'qty_and_params': 0,
            'qty_exclamation_params': 0,
            'qty_space_params': 0,
            'qty_tilde_params': 0,
            'qty_comma_params': 0,
            'qty_plus_params': 0,
            'qty_asterisk_params': 0,
            'qty_hashtag_params': 0,
            'qty_dollar_params': 0,
            'qty_percent_params': 0,
            'params_length': 0,
            'tld_present_params': 0,
            'qty_params': 0
        }
        return pd.DataFrame(features, index=[0])

    # Number of "." signs
    features['qty_dot_params'] = url.count('.')

    # Number of "-" signs
    features['qty_hyphen_params'] = url.count('-')

    # Number of "_" signs
    features['qty_underline_params'] = url.count('_')

    # Number of "/" signs
    features['qty_slash_params'] = url.count('/')

    # Number of "?" signs
    features['qty_questionmark_params'] = url.count('?')

    # Number of "=" signs
    features['qty_equal_params'] = url.count('=')

    # Number of "@" signs
    features['qty_at_params'] = url.count('@')

    # Number of "&" signs
    features['qty_and_params'] = url.count('&')

    # Number of "!" signs
    features['qty_exclamation_params'] = url.count('!')

    # Number of space signs
    features['qty_space_params'] = url.count(' ')

    # Number of "~" signs
    features['qty_tilde_params'] = url.count('~')

    # Number of "," signs
    features['qty_comma_params'] = url.count(',')

    # Number of "+" signs
    features['qty_plus_params'] = url.count('+')

    # Number of "*" signs
    features['qty_asterisk_params'] = url.count('*')

    # Number of "#" signs
    features['qty_hashtag_params'] = url.count('#')

    # Number of "$" signs
    features['qty_dollar_params'] = url.count('$')

    # Number of "%" signs
    features['qty_percent_params'] = url.count('%')

    # Number of characters
    features['params_length'] = len(url)

    # TLD present in parameters
    features['tld_present_params'] = bool(re.search(r'\.([a-zA-Z]{2,})', url))

    # Number of parameters
    features['qty_params'] = len(url.split('&'))

    return pd.DataFrame(features, index=[0])



