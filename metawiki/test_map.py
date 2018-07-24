from . import (
    url_to_name,
    name_to_url
)

def test_to_name():

    # _:
    result = url_to_name(
        'https://github.com/infamily/indb/wiki/percent-change#1hourly')

    assert result == '_:percent-change#1hourly'

    # IN:
    result = url_to_name(
        'https://github.com/infamily/ooio/wiki/percent-change#1hourly')

    assert result == 'IN:infamily/percent-change#1hourly'

    # FN:
    result = url_to_name(
        'https://github.com/mindey/ooio/blob/master/keys.md#a225d1e4')

    assert result == 'FN:mindey/keys.md#a225d1e4'

    # WD:
    result =  url_to_name('https://www.wikidata.org/wiki/Q1347367')

    assert result == 'WD:Q/1347367'

    result =  url_to_name('https://www.wikidata.org/wiki/Property:P31')

    assert result == 'WD:P/31'

def test_to_url():

    # _:
    result = name_to_url('_:level')

    assert result == 'https://github.com/infamily/indb/wiki/level'

    # IN:
    result = name_to_url('IN:infamily/level')

    assert result == 'https://github.com/infamily/ooio/wiki/level'

    # FN:
    result = name_to_url('FN:mindey/keys.md#a225d1e4')

    assert result == 'https://github.com/mindey/ooio/blob/master/keys.md#a225d1e4'

    # WD:
    result = name_to_url('WD:Q/1347367')

    assert result == 'https://www.wikidata.org/wiki/Q1347367'
