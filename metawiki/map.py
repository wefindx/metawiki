# Infinity namespace, to be defined on
# https://github.com/infamily/ooio/wiki
# and refered by keys starting with '_:'
INFINITY = {
    '_:{concept}': [
        'https://github.com/infamily/indb/wiki/{concept}',
        'https://raw.githubusercontent.com/wiki/infamily/indb/{concept}.md'
    ],
    '_:{concept}#{format}': [
        'https://github.com/infamily/indb/wiki/{concept}#{format}',
        'https://raw.githubusercontent.com/wiki/infamily/indb/{concept}.md#{format}'
    ]
}

# Wikidata namespace, to be defined on
# https://www.wikidata.org
# and refered by keys starting with 'WD:'
WIKIDATA = lambda N: {
    '%s:Q/{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Q{integer}'
    ],
    '%s:P/{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Property:P{integer}'
    ]
}

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


N = {}
N.update(INFINITY)
N.update(WIKIDATA('WD'))
N.update(GITHUB_WIKI('IN', 'ooio'))
MAP = N
