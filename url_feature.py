from urllib.parse import urlparse, parse_qs


def get_url_feature(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Extract the domain

    try:
        domain = parsed_url.netloc


    except:
        domain = {}

    # Extract the directory (path)
    directory = parsed_url.path

    # Extract the file name
    file = parsed_url.path.split('/')[-1]

    # Extract the parameters
    parameters = parse_qs(parsed_url.query)
    single_string = ' '.join([str(value) for value in parameters.values()])

    return domain, directory, file, single_string
