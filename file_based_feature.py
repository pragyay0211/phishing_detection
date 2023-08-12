import re
import pandas as pd


def extract_file_features(url):
    features = {}

    # Check if URL is empty
    if not url:
        # Return zero values for each feature
        features['qty_dot_file'] = 0
        features['qty_hyphen_file'] = 0
        features['qty_underline_file'] = 0
        features['qty_slash_file'] = 0
        features['qty_questionmark_file'] = 0
        features['qty_equal_file'] = 0
        features['qty_at_file'] = 0
        features['qty_and_file'] = 0
        features['qty_exclamation_file'] = 0
        features['qty_space_file'] = 0
        features['qty_tilde_file'] = 0
        features['qty_comma_file'] = 0
        features['qty_plus_file'] = 0
        features['qty_asterisk_file'] = 0
        features['qty_hashtag_file'] = 0
        features['qty_dollar_file'] = 0
        features['qty_percent_file'] = 0
        features['file_length'] = 0

        # Return the features as a DataFrame
        return pd.DataFrame(features, index=[0])

    # Number of "." signs
    features['qty_dot_file'] = url.count('.')

    # Number of "-" signs
    features['qty_hyphen_file'] = url.count('-')

    # Number of "_" signs
    features['qty_underline_file'] = url.count('_')

    # Number of "/" signs
    features['qty_slash_file'] = url.count('/')

    # Number of "?" signs
    features['qty_questionmark_file'] = url.count('?')

    # Number of "=" signs
    features['qty_equal_file'] = url.count('=')

    # Number of "@" signs
    features['qty_at_file'] = url.count('@')

    # Number of "&" signs
    features['qty_and_file'] = url.count('&')

    # Number of "!" signs
    features['qty_exclamation_file'] = url.count('!')

    # Number of space signs
    features['qty_space_file'] = url.count(' ')

    # Number of "~" signs
    features['qty_tilde_file'] = url.count('~')

    # Number of "," signs
    features['qty_comma_file'] = url.count(',')

    # Number of "+" signs
    features['qty_plus_file'] = url.count('+')

    # Number of "*" signs
    features['qty_asterisk_file'] = url.count('*')

    # Number of "#" signs
    features['qty_hashtag_file'] = url.count('#')

    # Number of "$" signs
    features['qty_dollar_file'] = url.count('$')

    # Number of "%" signs
    features['qty_percent_file'] = url.count('%')

    # Number of characters
    features['file_length'] = len(url)

    return pd.DataFrame(features, index=[0])
