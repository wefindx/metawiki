from .fmap import (
    n2f,
    f2n,
)
from metawiki import (
    ext2url,
    url2ext,
)

def test_f2n():

    # _:
    assert f2n('__topic#metaculus') == '_:topic#metaculus'

    # ::
    assert f2n('_mindey@topic#metaculus') == '::mindey/topic#metaculus'

    # WD
    assert f2n('WD@Q123') == 'WD:Q123'

def test_n2f():

    # _:
    assert n2f('_:topic#metaculus') == '__topic#metaculus'

    # ::
    assert n2f('::mindey/topic#metaculus') == '_mindey@topic#metaculus'

    # WD
    assert n2f('WD:Q123') == 'WD@Q123'

def test_url2f():
    assert url2ext('https://github.com/mindey/-/wiki/cucumber#xtrandard') == '_mindey@cucumber#xtrandard'

    assert url2ext('https://github.com/infamily/_/wiki/topic#google-plus') == '__topic#google-plus'

def test_f2url():
    assert 'https://github.com/mindey/-/wiki/cucumber#xtrandard' == ext2url('_mindey@cucumber#xtrandard')

    assert 'https://github.com/infamily/_/wiki/topic#google-plus' == ext2url('__topic#google-plus')
