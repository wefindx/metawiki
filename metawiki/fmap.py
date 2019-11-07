# Files Map -- Crosswalk map.

# Extenions:        .yaml, .json, .csv., .xlsx, .png
# Sub-extensions:   .Topic.yaml, .Comment.yaml, .Drawing.png

# In order to hard-assign files with sub-extensions, we need a way to link sub-extensions with Wikis for concepts.

# Example:
'''
*GH~mindey.terms.topic_metaculus.* <=> GH:mindey/terms/topic#metaculus
*WD~Q123.*                         <=> WD:Q123
'''

FMAP = {}

def f2n(token):
    'filename to name'

    # PARSE
    if '_' in token:
        _concept, _format = token.rsplit('_', 1)
    else:
        _concept, _format = token, None

    if '~' in _concept:
        _namespace, _alias = _concept.rsplit('~', 1)
    else:
        _namespace, _alias = _concept, None

    # MERGE
    name = ''

    if _namespace == 'GH':            # github wikis
        name += _namespace + ':'
    elif _namespace == 'GHF':         # github repo files
        name += _namespace + ':'
    elif _namespace == 'WD':          # wikidata
        name += _namespace + ':'

    if _alias is not None:
        name += _alias.replace('.', '/')

    if _format is not None:
        name += '#'+_format

    return name


def n2f(token):
    'name to filename'

    # PARSE
    if '#' in token:
        _concept, _format = token.rsplit('#', 1)
    else:
        _concept, _format = token, None

    if ':' in _concept:
        _namespace, _path = _concept.rsplit(':', 1)
    else:
        _namespace, _path = _concept, None

    # MERGE
    name = ''

    name += _namespace + '~'

    if _path is not None:
        name += _path.replace('/', '.')

    if _format is not None:
        name += '_'+_format

    return name
