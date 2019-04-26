# Files Map

# Extenions:        .yaml, .json, .csv., .xlsx, .png
# Sub-extensions:   .Topic.yaml, .Comment.yaml, .Drawing.png

# In order to hard-assign files with sub-extensions, we need a way to link sub-extensions with Wikis for concepts.

# Example:
'''
*._topic#metaculus.*         <=> _:topic#metaculus
*.__mindey@topic#metaculus.* <=> ::mindey/topic#metaculus
*.WD@Q123.*                  <=> WD:Q123
'''

FMAP = {}

def f2n(token):
    'filename to name'

    # PARSE
    if '#' in token:
        _concept, _format = token.rsplit('#', 1)
    else:
        _concept, _format = token, None

    if '@' in _concept:
        _namespace, _alias = _concept.rsplit('@', 1)
    else:
        _namespace, _alias = _concept, None

    # MERGE
    name = ''

    if _namespace.startswith('__'):     # github wikis
        name += '_:'+_namespace[2:]
    elif _namespace.startswith('_'):
        name += '::'+_namespace[1:]     # infamily wiki
    elif _namespace == 'WD':            # wikidata
        name += _namespace + ':'

    if _alias is not None:
        if _namespace.startswith('_') and _namespace[:2]!='__' : # github wikis
            name += '/'
        name += _alias

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

    if '/' in _concept:
        _namespace, _alias = _concept.rsplit('/', 1)
    elif ':' in _concept:
        _namespace, _alias = _concept.rsplit(':', 1)
#       _namespace += ':'
    else:
        _namespace, _alias = _concept, None

    # MERGE
    name = ''

    if _namespace == '_':               # infamily
        name += '_' + _namespace
    elif _namespace.startswith('::'):
        name += '_' + _namespace[2:] + '@'   # infamily wiki
    elif _namespace == 'WD':            # wikidata
        name += _namespace + '@'

    if _alias is not None:
        if _namespace.startswith('__'): # github wikis
            name += '/'
        name += _alias

    if _format is not None:
        name += '#'+_format

    return name
