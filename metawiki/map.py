NAMESPACES = {}

# Wikidata (https://www.wikidata.org/wiki/{reference})
# WD: namespace refered by keys starting with 'WD:'
WIKIDATA = lambda N: {
    '%s:Q{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Q{integer}'
    ],
    '%s:P{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Property:P{integer}'
    ]
}
NAMESPACES['WD:'] = WIKIDATA('WD')

# Github (https://github.com/{user}/{repo}/wiki/{concept})
# GH: wiki namespace, refered by keys starting with 'GH:'
GITHUB_WIKI = lambda N: {
    '%s:{user}/{repo}/{concept}' % (N,): [
        'https://github.com/{user}/{repo}/wiki/{concept}',
        'https://raw.githubusercontent.com/wiki/{user}/{repo}/{concept}.md',
    ],
    '%s:{user}/{repo}/{concept}#{format}' % (N,): [
        'https://github.com/{user}/{repo}/wiki/{concept}#{format}',
        'https://raw.githubusercontent.com/wiki/{user}/{repo}/{concept}.md#{format}',
    ]
}
NAMESPACES['GH:'] = GITHUB_WIKI('GH')

# Github files (https://github.com/{user}/{repo}/blob/master/{concept})
# GHF: refered by keys starting with 'GHF:'
GITHUB_FILE = lambda N: {
    '%s:{user}/{repo}/{concept}' % (N,): [
        'https://github.com/{user}/{repo}/blob/master/{concept}',
        'https://raw.githubusercontent.com/{user}/{repo}/{concept}',
    ],
    '%s:{user}/{repo}/{concept}#{format}' % (N,): [
        'https://github.com/{user}/{repo}/blob/master/{concept}#{format}',
        'https://raw.githubusercontent.com/{user}/{repo}/{concept}#{format}',
    ]
}
NAMESPACES['GHF:'] = GITHUB_FILE('GHF') # FILEs of ooio repos


MAP = {}

for key, value in NAMESPACES.items():
    MAP = dict(MAP, **value)
