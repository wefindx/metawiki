NAMESPACES = {}

# Infinity namespace, to be defined on
# https://github.com/infamily/ooio/wiki
# and refered by keys starting with '_:'
INFINITY = {
    '_:{concept}': [
        'https://github.com/infamily/_/wiki/{concept}',
        'https://raw.githubusercontent.com/wiki/infamily/_/{concept}.md'
    ],
    '_:{concept}#{format}': [
        'https://github.com/infamily/_/wiki/{concept}#{format}',
        'https://raw.githubusercontent.com/wiki/infamily/_/{concept}.md#{format}'
    ]
}
NAMESPACES['_:'] = INFINITY


# Wikidata namespace, to be defined on
# https://www.wikidata.org
# and refered by keys starting with 'WD:'
WIKIDATA = lambda N: {
    '%s:Q{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Q{integer}'
    ],
    '%s:P{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Property:P{integer}'
    ]
}
NAMESPACES['WD:'] = WIKIDATA('WD')


# Github ooio wiki namespace, to be defined on M repo wikis
# https://github.com/{user}/M/wiki/{concept}
# and refered by keys starting with 'N:{user}/{concept}'
GITHUB_WIKI = lambda N, M: {
    '%s:{user}/{concept}' % (N,): [
        'https://github.com/{user}/%s/wiki/{concept}' % (M,),
        'https://raw.githubusercontent.com/wiki/{user}/%s/{concept}.md' % (M,),
    ],
    '%s:{user}/{concept}#{format}' % (N,): [
        'https://github.com/{user}/%s/wiki/{concept}#{format}' % (M,),
        'https://raw.githubusercontent.com/wiki/{user}/%s/{concept}.md#{format}' % (M,),
    ]
}
NAMESPACES['IN:'] = GITHUB_WIKI('IN', 'ooio') # WIKIs of ooio repos
NAMESPACES['@:'] = GITHUB_WIKI('@', 'terms') # WIKIs of terms repos
NAMESPACES['::'] = GITHUB_WIKI(':', '-') # WIKIs of - repos

# Files of ooio repos namespaces, to be defined on M repo files
# https://github.com/{user}/M/wiki/{concept}
# and refered by keys starting with 'N:{user}/{filename}'
GITHUB_FILE = lambda N, M: {
    '%s:{user}/{concept}' % (N,): [
        'https://github.com/{user}/%s/blob/master/{concept}' % (M,),
        'https://raw.githubusercontent.com/{user}/%s/{concept}' % (M,),
    ],
    '%s:{user}/{concept}#{format}' % (N,): [
        'https://github.com/{user}/%s/blob/master/{concept}#{format}' % (M,),
        'https://raw.githubusercontent.com/{user}/%s/{concept}#{format}' % (M,),
    ]
}
NAMESPACES['FN:'] = GITHUB_FILE('FN', 'ooio') # FILEs of ooio repos
NAMESPACES['-:'] = GITHUB_FILE('-', '-') # FILEs of ooio repos


MAP = {}

for key, value in NAMESPACES.items():
    MAP = dict(MAP, **value)
