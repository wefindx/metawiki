MAP = {
    'IN:{user}/{concept}': [
        'https://github.com/{user}/indb/wiki/{concept}',
        'https://raw.githubusercontent.com/wiki/{user}/indb/{concept}.md',
    ],
    'IN:{user}/{concept}#{format}': [
        'https://github.com/{user}/indb/wiki/{concept}#{format}',
        'https://raw.githubusercontent.com/wiki/{user}/indb/{concept}.md#{format}',
    ],
    'WD:Q{integer}': [
        'https://www.wikidata.org/wiki/Q{integer}'
    ],
    'WD:P{integer}': [
        'https://www.wikidata.org/wiki/Property:P{integer}'
    ]
}

