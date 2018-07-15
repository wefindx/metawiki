WIKIDATA = lambda N: {
    '%s:Q/{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Q{integer}'
    ],
    '%s:P/{integer}' % (N,): [
        'https://www.wikidata.org/wiki/Property:P{integer}'
    ]
}

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

# NAMESPACES

N = {}
N.update(WIKIDATA('WD'))
N.update(GITHUB_WIKI('IN', 'indb'))
N.update(GITHUB_WIKI('OO', 'ooio'))

MAP = N
