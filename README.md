# metawiki

_Namespaces are one honking great idea -- let's do more of those!_

In order to refer to a concept unambiguously, these days, it is easiest to use URL to a dictionary word online. However, these URLs are long. Using a hash function or compressor like md5, zlib, etc. for URLs are not convenient, because results are not human-readable.

THUS:

It makes sense to define a specific **[MAP](/metawiki/map.py)** function, that implements a namespace to refer to all concepts on the web. Mostly, concepts are defined on wikis, so call it - `metawiki`.

`pip install metawiki`

```python
>>> from metawiki import (
    url2name,
    name2url
)
```

## [GitHub  wikis](https://help.github.com/en/github/building-a-strong-community/about-wikis) (GH namespace)
All wikis of GitHub repositories under users and organizations.

```
>>> url2name('https://github.com/infamily/indb/wiki/percent-change#1hourly')
'GH:infamily/indb/percent-change#1hourly'

>>> name2url('GH:infamily/terms/level')
https://github.com/infamily/terms/wiki/level
```

In addition, namespace **GHF** also exists, to refer to files on GitHub repositories:
```
>>> url2name('https://github.com/wefindx/metawiki/metawiki/map.py')
'GHF:wefindx/metawiki/metawiki/map.py'

>>> name2url('GHF:wefindx/metawiki/metawiki/map.py')
'https://github.com/wefindx/metawiki/blob/master/metawiki/map.py'
```

The reason we use `/` instead of `.` for namespacing in each source, is because this makes it usable as keys in the key-value databases, that rely on `.` for queries.

The general resulting pattern, is, e.g.:

```
Namespace:Path/In/Organization/Concept#Format

# E.g.
GH:nasa/terms/precession#<some metric or measure>
```

## [Wikidata](https://www.wikidata.org/) (WD namespace)

The Wikidata namespace. All concepts and relations from WikiData.
```
>>> url2name('https://www.wikidata.org/wiki/Q1347367')
'WD:Q1347367'

>>> name2url('WD:Q1347367')
'https://www.wikidata.org/wiki/Q1347367'

>>> url2name('https://www.wikidata.org/wiki/Property:P31')
'WD:P31'
...
```

## [LOV](https://lov.linkeddata.es/dataset/lov/vocabs/) (a-loc..zbwext namespaces)

The LOV namespaces. (Most of the semantic web, as defined through RDF initiative.)

Get the newest after importing metawiki with `metawiki.data.update_lov()`.


_Feel free to PR, to extend the [map](/metawiki/map.py)._
