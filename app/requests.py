import urllib.request,json
from .models.articles import Articles
from .models.sources import Sources
from .models.highlights import Highlights


# Getting api key
api_key = None

# Getting the movie base url
base_url = None
base_article_url = None
base_highlights_url = None

def configure_request(app):
    global api_key,base_url,base_article_url,base_highlights_url,categories_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    base_article_url = app.config['ARTICLES_API_BASE_URL']
    base_highlights_url = app.config['HIGHLIGHTS_API_BASE_URL']
    categories_url = app.config['CATEGORY_API_BASE_URL']



def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)

    return sources_results

def process_sources_results(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of source objects
    """
    
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        # if poster:
        source_object = Sources(id, name, description, url, category, language, country)
        sources_results.append(source_object)

    return sources_results

def get_categories(category):
    '''
    Function that gets the json response to our url request
    '''
    get_categories_url = categories_url.format(category,api_key)

    with urllib.request.urlopen(get_categories_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_results_list)

    return sources_results

def process_sources_results(sources_list):
    """
    Function  that processes the sources result and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        sources_results: A list of source objects
    """
    
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        # if poster:
        source_object = Sources(id, name, description, url, category, language, country)
        sources_results.append(source_object)

    return sources_results


def get_articles(id):
    '''
    Function that gets the json Articles response to our url request
    '''
    get_articles_url = base_article_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_results_list)

        

    return articles_results

def process_articles_results(articles_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain sources details

    Returns :
        articles_results: A list of source objects
    """
    
    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Articles(id, author, title, description, url, urlToImage, publishedAt, content)
            articles_results.append(article_object)

    return articles_results



def get_highlights(id):
    '''
    Function that gets the json Highlights response to our url request
    '''
    get_highlights_url = base_highlights_url.format(id, api_key)

    with urllib.request.urlopen(get_highlights_url) as url:
        get_highlights_data = url.read()
        get_highlights_response = json.loads(get_highlights_data)

        highlights_results = None

        if get_highlights_response['articles']:
            highlights_results_list = get_highlights_response['articles']
            highlights_results = process_highlights_results(highlights_results_list)

        

    return highlights_results

def process_highlights_results(highlights_list):
    """
    Function  that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain sources details

    Returns :
        articles_results: A list of source objects
    """
    
    highlights_results = []
    for highlights_item in highlights_list:
        id = highlights_item.get('id')
        author = highlights_item.get('author')
        title = highlights_item.get('title')
        description = highlights_item.get('description')
        url = highlights_item.get('url')
        urlToImage = highlights_item.get('urlToImage')
        publishedAt = highlights_item.get('publishedAt')
        content = highlights_item.get('content')

        if urlToImage:
            highlights_object = Highlights(id, author, title, description, url, urlToImage, publishedAt, content)
            highlights_results.append(highlights_object)

    return highlights_results