from . import (
    url_to_name,
    name_to_url
)

def test_to_name():

    # INDB
    result = url_to_name(
        'https://github.com/infamily/indb/wiki/percent-change#1hourly')

    assert result == 'IN:infamily/percent-change#1hourly'

    result =  url_to_name('https://www.wikidata.org/wiki/Q1347367')

    # Wikidata
    assert result == 'WD:Q/1347367'

    result =  url_to_name('https://www.wikidata.org/wiki/Property:P31')

    assert result == 'WD:P/31'

def test_to_url():

    # INDB
    result = name_to_url('IN:infamily/level')

    assert result == 'https://github.com/infamily/indb/wiki/level'

    # Wikidata
    result = name_to_url('WD:Q1347367')

    assert result == 'https://www.wikidata.org/wiki/Q1347367'
