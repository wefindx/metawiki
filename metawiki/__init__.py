from .map import MAP

import parse

class MetaWikiError(Exception):
    pass

namespaces = {
    'IN:': 'INDB',
    'WD:': 'Wikidata'
}
urlspaces = {
    'http://': 'HTTP location',
    'https://': 'HTTPS location'
}

def isname(string):
    return any([string.startswith(name) for name in namespaces])

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

    # INDB
    if name.startswith('IN:'):
        if not '#' in name:
            template = 'IN:{user}/{concept}'
        else:
            template = 'IN:{user}/{concept}#{format}'

    # Wikidata
    elif name.startswith('WD:'):
        if name.startswith('WD:Q'):
            template = 'WD:Q{integer}'

        elif name.startswith('WD:P'):
            template = 'WD:P{integer}'

        else:
            raise MetaWikiError(
                "Wikidata concept cannot start with anything other than WD:Q or WD:P, you provided: {}.".format(name)
            )

    if template:
        return convert(name, template)
    else:
        raise MetaWikiError(
            "Could not find the template for concept: {}.".format(name)
        )


def url_to_name(url, skip_valid=True):

    if skip_valid:
        if isname(url):
            return url

    template = None

    # INDB
    if url.startswith('https://github.com/'):
        if '/indb/wiki/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/indb/wiki/{concept}'
            else:
                template = 'https://github.com/{user}/indb/wiki/{concept}#{format}'
        else:
            raise MetaWikiError("Undefined GitHub namespace for: {}. (currently, only repo=indb in url are valid)".format(url))

    # Wikidata
    if url.startswith('https://www.wikidata.org/'):
        if '/wiki/Q' in url:
            template = 'https://www.wikidata.org/wiki/Q{integer}'
        elif '/wiki/Property:P' in url:
            template = 'https://www.wikidata.org/wiki/Property:P{integer}'
        else:
            raise MetaWikiError("Undefined Wikidata namespace for: {}.".format(url))

    if template:
        return convert(url, template, inverse=True)
    else:
        raise MetaWikiError(
            "Could not find the template for url: {}.".format(url)
        )
