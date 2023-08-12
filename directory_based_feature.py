import pandas as pd


def extract_directory_features(url):
    features = {}

    # Check if URL is empty
    if not url:
        # Return zero values for each feature
        features['qty_dot_directory'] = 0
        features['qty_hyphen_directory'] = 0
        features['qty_underline_directory'] = 0
        features['qty_slash_directory'] = 0
        features['qty_questionmark_directory'] = 0
        features['qty_equal_directory'] = 0
        features['qty_at_directory'] = 0
        features['qty_and_directory'] = 0
        features['qty_exclamation_directory'] = 0
        features['qty_space_directory'] = 0
        features['qty_tilde_directory'] = 0
        features['qty_comma_directory'] = 0
        features['qty_plus_directory'] = 0
        features['qty_asterisk_directory'] = 0
        features['qty_hashtag_directory'] = 0
        features['qty_dollar_directory'] = 0
        features['qty_percent_directory'] = 0
        features['directory_length'] = 0

        # Return the features as a DataFrame
        return pd.DataFrame(features, index=[0])

    # Number of "." signs
    features['qty_dot_directory'] = url.count('.')

    # Number of "-" signs
    features['qty_hyphen_directory'] = url.count('-')

    # Number of "_" signs
    features['qty_underline_directory'] = url.count('_')

    # Number of "/" signs
    features['qty_slash_directory'] = url.count('/')

    # Number of "?" signs
    features['qty_questionmark_directory'] = url.count('?')

    # Number of "=" signs
    features['qty_equal_directory'] = url.count('=')

    # Number of "@" signs
    features['qty_at_directory'] = url.count('@')

    # Number of "&" signs
    features['qty_and_directory'] = url.count('&')

    # Number of "!" signs
    features['qty_exclamation_directory'] = url.count('!')

    # Number of space signs
    features['qty_space_directory'] = url.count(' ')

    # Number of "~" signs
    features['qty_tilde_directory'] = url.count('~')

    # Number of "," signs
    features['qty_comma_directory'] = url.count(',')

    # Number of "+" signs
    features['qty_plus_directory'] = url.count('+')

    # Number of "*" signs
    features['qty_asterisk_directory'] = url.count('*')

    # Number of "#" signs
    features['qty_hashtag_directory'] = url.count('#')

    # Number of "$" signs
    features['qty_dollar_directory'] = url.count('$')

    # Number of "%" signs
    features['qty_percent_directory'] = url.count('%')

    # Number of characters
    features['directory_length'] = len(url)

    return pd.DataFrame(features, index=[0])
