# Files Map

# Allows to attach schemas to paths and filenames inside them.
# i.e., metawiki.get_path_schema(<filename or url>)

# Extenions:        .yaml, .json, .csv., .xlsx, .png
# Sub-extensions:   .Topic.yaml, .Comment.yaml, .Drawing.png

# In order to hard-assign files with sub-extensions, we need a way to link sub-extensions with Wikis for concepts.

# Example:
'''
*.GH~wefindx+schema+Sale.*      <=> GH:wefindx/schema/Sale
*.GH~mindey+-+topic$metaculus.* <=> GH:mindey/-/topic#metaculus
*.WD~Q123.*                     <=> WD:Q123

Then, also:
*.GH~wefindx+schema+Sale.csv       <=> {'ext': 'csv', 'schema': 'https://github.com/wefindx/schema/wiki/Sale'}
*.GH~mindey+-+topic$metaculus.json <=> {'ext': 'json', 'schema': 'https://github.com/mindey/-/wiki/topic#metaculus'}
*.WD~Q123$XYZ.png                  <=> {'ext': 'png', 'schema': 'https://www.wikidata.org/wiki/Q123#XYZ'}
'''
# To allow to parse file content automatically by using schema reference in the filenames of data. (metawiki.get_path_schema)


FMAP = {}

def f2n(token):
    'filename to name'

    # PARSE
    if '$' in token:
        _concept, _format = token.rsplit('$', 1)
    else:
        _concept, _format = token, None

    if '~' in _concept:
        _namespace, _alias = _concept.rsplit('~', 1)
    else:
        _namespace, _alias = _concept, None

    # MERGE
    name = ''

    if _namespace is not None:
        name += _namespace + ':'

    if _alias is not None:
        name += _alias.replace('+', '/')

    if _format is not None:
        name += '#' + _format

    return name



def n2f(token):
    'name to filename'

    # PARSE
    if '#' in token:
        _concept, _format = token.rsplit('#', 1)
    else:
        _concept, _format = token, None

    if ':' in _concept:
        _namespace, _alias = _concept.rsplit(':', 1)
    else:
        _namespace, _alias = _concept, None

    # MERGE
    name = ''

    name += _namespace  + '~'

    if _alias is not None:
        name += _alias.replace('/', '+')

    if _format is not None:
        name += '$' + _format

    return name



