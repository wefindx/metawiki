from metawiki import (
    url_to_name,
    name_to_url
)

def test_to_name():

    # GH:
    result = url_to_name(
        'https://github.com/infamily/-/wiki/percent-change#1hourly')

    assert result == 'GH:infamily/-/percent-change#1hourly'

    # GHF:
    result = url_to_name(
        'https://github.com/mindey/-/blob/master/keys.md#a225d1e4')

    assert result == 'GHF:mindey/-/keys.md#a225d1e4'

    # WD:
    result =  url_to_name('https://www.wikidata.org/wiki/Q1347367')

    assert result == 'WD:Q1347367'

    result =  url_to_name('https://www.wikidata.org/wiki/Property:P31')

    assert result == 'WD:P31'

def test_to_url():

    # GH:
    result = name_to_url('GH:infamily/-/level')

    assert result == 'https://github.com/infamily/-/wiki/level'

    # GHF:
    result = name_to_url('GHF:mindey/-/keys.md#a225d1e4')

    assert result == 'https://github.com/mindey/-/blob/master/keys.md#a225d1e4'

    # WD:
    result = name_to_url('WD:Q1347367')

    assert result == 'https://www.wikidata.org/wiki/Q1347367'
