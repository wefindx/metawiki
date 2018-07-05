
import parse


MAP = {
    'user.concept': [
        'https://github.com/{user}/indb/wiki/{concept}',
    ],
    'user.concept#format': [
        'https://github.com/{user}/indb/wiki/{concept}#{format}',
    ],
    'Q{integer}': [
        'https://www.wikidata.org/wiki/Q{integer}'
    ]
}


def url_to_name(url):
    if url.startswith('https://github.com/'):
        if '/wiki/' in url:

    pass

def name_to_url(name):
    pass



def test_to_name():
    assert True

def test_to_url():
    assert True
