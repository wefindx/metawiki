from .map import MAP

import parse

class MetaWikiError(Exception):
    pass

def name_to_url(name):

    template = None

    # INDB
    if name.startswith('IN:'):
        if not '#' in name:
            template = 'IN:{user}/{concept}'
            endplate = MAP[template][0]
            p = parse.parse(template, name)

            return endplate.format(
                concept=p['concept'],
                user=p['user'])
        else:
            template = 'IN:{user}/{concept}#{format}'
            endplate = MAP[template][0]
            p = parse.parse(template, name)

            return endplate.format(
                concept=p['concept'],
                user=p['user'],
                format=p['format'])

    # Wikidata
    elif name.startswith('WD:'):
        if name.startswith('WD:Q'):
            template = 'WD:Q{integer}'
            endplate = MAP[template][0]
            p = parse.parse(template, name)

            return endplate.format(
                integer=p['integer'])


        elif name.startswith('WD:P'):
            template = 'WD:P{integer}'
            endplate = MAP[template][0]
            p = parse.parse(template, name)

            return endplate.format(
                integer=p['integer'])

        else:
            raise MetaWikiError(
                "Wikidata concept cannot start with anything other than WD:Q or WD:P, you provided: {}.".format(name)
            )

    if template is None:
        raise MetaWikiError(
            "Could not find the template for concept: {}.".format(name)
        )

    return


def url_to_name(url):
    if url.startswith('https://github.com/'):
        if '/wiki/' in url:
            pass
