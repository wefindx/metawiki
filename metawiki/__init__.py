from metawiki.map import MAP, NAMESPACES, LOV
from metawiki.fmap import f2n, n2f

import parse

class MetaWikiError(Exception):
    pass


urlspaces = {
    'http://': 'HTTP location',
    'https://': 'HTTPS location'
}

def isname(string):
    return any([string.startswith(name) for name in NAMESPACES])

def isurl(string):
    return any([string.startswith(url) for url in urlspaces])


def convert(name, template, inverse=False):

    if inverse:
        REVERSED_MAP = {item[-1][0]: [item[0]] for item in MAP.items()}
        endplate = REVERSED_MAP[template][0]
    else:
        endplate = MAP[template][0]

    p = parse.parse(template, name)

    return endplate.format(**p.named)


def name_to_url(name, skip_valid=True):

    if skip_valid:
        if isurl(name):
            return name

    template = None

    # GH:
    if name.startswith('GH:'):
        if not '#' in name:
            template = 'GH:{user}/{repo}/{concept}'
        else:
            template = 'GH:{user}/{repo}/{concept}#{format}'


    # GHF:
    if name.startswith('GHF:'):
        if not '#' in name:
            template = 'GHF:{user}/{repo}/{concept}'
        else:
            template = 'GHF:{user}/{repo}/{concept}#{format}'

    # WD:
    elif name.startswith('WD:'):
        if name.startswith('WD:Q'):
            template = 'WD:Q{integer}'

        elif name.startswith('WD:P'):
            template = 'WD:P{integer}'

        else:
            raise MetaWikiError(
                "Wikidata concept cannot start with anything other than WD:Q or WD:P, you provided: {}.".format(name)
            )
    # LOV
    else:
        for vocab in LOV:
            if name.split(':', 1)[0] == vocab['prefix']:
                template = '%s:{concept}' % name.split(':', 1)[0]

    if template:
        return convert(name, template)
    else:
        raise MetaWikiError(
            "Could not find the template for concept: {}.".format(name)
        )

name2url = name_to_url


def url_to_name(url, skip_valid=True):

    if skip_valid:
        if isname(url):
            return url

    template = None

    # GH:
    if url.startswith('https://github.com/'):

        # GH:
        if '/wiki/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/{repo}/wiki/{concept}'
            else:
                template = 'https://github.com/{user}/{repo}/wiki/{concept}#{format}'

        # GHF:
        elif '/blob/master/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/{repo}/blob/master/{concept}'
            else:
                template = 'https://github.com/{user}/{repo}/blob/master/{concept}#{format}'

        else:
            raise MetaWikiError("Undefined GitHub namespace for: {}. (currently, only repo=_ in url are valid)".format(url))

    # WD:
    elif url.startswith('https://www.wikidata.org/'):
        if '/wiki/Q' in url:
            template = 'https://www.wikidata.org/wiki/Q{integer}'
        elif '/wiki/Property:P' in url:
            template = 'https://www.wikidata.org/wiki/Property:P{integer}'
        else:
            raise MetaWikiError("Undefined Wikidata namespace for: {}.".format(url))

    # LOV
    else:
        for vocab in LOV:
            if vocab['nsp'].split('://', 1)[-1][:-1] in url:
                url = vocab['nsp'] + url.split('#', 1)[-1]
                template = vocab['nsp']+'{concept}'


    if template:
        return convert(url, template, inverse=True)
    else:
        raise MetaWikiError(
            "Could not find the template for url: {}.".format(url)
        )

url2name = url_to_name

def ext2url(token, skip_valid=True):
    return name_to_url(f2n(token), skip_valid=skip_valid)

def url2ext(url, skip_valid=True):
    return n2f(url_to_name(url, skip_valid=skip_valid))
