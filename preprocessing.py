from url_based_feature import extract_url_features
from domain_based_feature import extract_domain_features
from directory_based_feature import extract_directory_features
from file_based_feature import extract_file_features
from parameter_based_feature import extract_params_features
from external_service_feature import extract_features
from url_feature import get_url_feature
import pandas as pd


def get_df(url):
    domain, directory, file, parameter = get_url_feature(url)

    df1 = extract_url_features(url)
    df2 = extract_domain_features(domain)
    df3 = extract_file_features(file)
    df4 = extract_directory_features(directory)
    df5 = extract_params_features(parameter)
    df6 = extract_features(url)

    df_final = pd.concat([df1, df2, df3, df4, df5, df6], axis=1)

    return df_final

