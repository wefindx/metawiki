# metawiki

_Namespaces are one honking great idea -- let's do more of those!_

In order to refer to a concept unambiguously, these days, it is easiest to use URL to a dictionary word online. However, these URLs are long. Using a hash function or compressor like md5, zlib, etc. for URLs are not convenient, because results are not human-readable.

THUS:

It makes sense to define a specific MAP function, that implements a namespace to refer to all concepts on the web. Mostly, concepts are defined on wikis, so call it - `metawiki`.

`pip install metawiki`

```python
>>> from metawiki import (
    url2name,
    name2url
)
```

## GitHub wikis (GH namespace)
All wikis of GitHub repositories under users and organizations.

```
>>> url2name('https://github.com/infamily/indb/wiki/percent-change#1hourly')
'GH:infamily/indb/percent-change#1hourly'

>>> name2url('GH:infamily/terms/level')
https://github.com/infamily/terms/wiki/level
```

## Wikidata (WD namespace)

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

The reason we use `/` instead of `.` for namespacing in each source, is because this makes it usable as keys in the key-value databases, that rely on `.` for queries.

The general resulting pattern, is, e.g.:

```
Namespace:Path/In/Organization/Concept#Format

# E.g.
GH:nasa/terms/precession#<some metric or measure>
```


Feel free to PR, to extend the map.
