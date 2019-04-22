from metawiki.map import MAP, NAMESPACES
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

    # _:
    if name.startswith('_:'):
        if not '#' in name:
            template = '_:{concept}'
        else:
            template = '_:{concept}#{format}'

    # IN:
    if name.startswith('IN:'):
        if not '#' in name:
            template = 'IN:{user}/{concept}'
        else:
            template = 'IN:{user}/{concept}#{format}'

    # @:
    if name.startswith('@:'):
        if not '#' in name:
            template = '@:{user}/{concept}'
        else:
            template = '@:{user}/{concept}#{format}'

    # ::
    if name.startswith('::'):
        if not '#' in name:
            template = '::{user}/{concept}'
        else:
            template = '::{user}/{concept}#{format}'


    # FN:
    if name.startswith('FN:'):
        if not '#' in name:
            template = 'FN:{user}/{concept}'
        else:
            template = 'FN:{user}/{concept}#{format}'

    # -:
    if name.startswith('-:'):
        if not '#' in name:
            template = '-:{user}/{concept}'
        else:
            template = '-:{user}/{concept}#{format}'

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

    # _:, IN:
    if url.startswith('https://github.com/'):
        # _:
        if '/infamily/_/wiki/' in url:
            if not '#' in url:
                template = 'https://github.com/infamily/_/wiki/{concept}'
            else:
                template = 'https://github.com/infamily/_/wiki/{concept}#{format}'
        # IN:
        elif '/ooio/wiki/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/ooio/wiki/{concept}'
            else:
                template = 'https://github.com/{user}/ooio/wiki/{concept}#{format}'

        # @:
        elif '/terms/wiki/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/terms/wiki/{concept}'
            else:
                template = 'https://github.com/{user}/terms/wiki/{concept}#{format}'

        # ::
        elif '/-/wiki/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/-/wiki/{concept}'
            else:
                template = 'https://github.com/{user}/-/wiki/{concept}#{format}'

        # -:
        elif '/-/blob/master/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/-/blob/master/{concept}'
            else:
                template = 'https://github.com/{user}/-/blob/master/{concept}#{format}'

        # FN:
        elif '/ooio/blob/master/' in url:
            if not '#' in url:
                template = 'https://github.com/{user}/ooio/blob/master/{concept}'
            else:
                template = 'https://github.com/{user}/ooio/blob/master/{concept}#{format}'

        else:
            raise MetaWikiError("Undefined GitHub namespace for: {}. (currently, only repo=_ in url are valid)".format(url))

    # WD:
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

def ext2url(token, skip_valid=True):
    return name_to_url(f2n(token), skip_valid=skip_valid)

def url2ext(url, skip_valid=True):
    return n2f(url_to_name(url, skip_valid=skip_valid))
