# metawiki

In order to refer to a concept unambiguously, these days, it is easiest to use URL to a dictionary word online. However, these URLs are long. Using a hash function or compressor like md5, zlib, etc. for URLs are not convenient, because results are not human-readable.

THUS:

It makes sense to define a specific MAP function, that implements a namespace to refer to all concepts on the web. Mostly, concepts are defined on wikis, so call it - `metawiki`.

`pip install metawiki`

```python
>>> from metawiki import (
    url_to_name,
    name_to_url
)

# INDB (sub-namespace of GitHub)
>>> url_to_name('https://github.com/infamily/indb/wiki/percent-change#1hourly')
'IN:infamily/percent-change#1hourly'

>>> name_to_url('infamily.level')
https://github.com/infamily/indb/wiki/level

# Wikidata
>>> url_to_name('https://www.wikidata.org/wiki/Q1347367')
'WD:Q/1347367'

>>> name_to_url('Q1347367')
'https://www.wikidata.org/wiki/Q1347367'

>>> url_to_name('https://www.wikidata.org/wiki/Property:P31')
'WD:P/31'
...
```

The reason I use `/` instead of `.` for namespacing in each source, is because this makes it usable as keys in the key-value databases, that rely on `.` for queries.
