from .fmap import (
    n2f,
    f2n,
)
from metawiki import (
    ext2url,
    url2ext,
    fn2url,
)

def test_f2n():

    # GH:
    assert f2n('GH~mindey+-+topic$metaculus') == 'GH:mindey/-/topic#metaculus'

    # WD:
    assert f2n('WD~Q123') == 'WD:Q123'

def test_n2f():

    # GH:
    assert n2f('GH:mindey/-/topic#metaculus') == 'GH~mindey+-+topic$metaculus'

    # WD:
    assert n2f('WD:Q123') == 'WD~Q123'

def test_url2f():
    assert url2ext('https://github.com/mindey/-/wiki/cucumber#xtrandard') == 'GH~mindey+-+cucumber$xtrandard'

    assert url2ext('https://github.com/infamily/_/wiki/topic#google-plus') == 'GH~infamily+_+topic$google-plus'

def test_f2url():
    assert 'https://github.com/mindey/-/wiki/cucumber#xtrandard' == ext2url('GH~mindey+-+cucumber$xtrandard')

    assert 'https://github.com/infamily/_/wiki/topic#google-plus' == ext2url('GH~infamily+_+topic$google-plus')

def test_fn2url():

    assert 'https://github.com/mindey/-/wiki/cucumber#xtrandard' == fn2url('GH~mindey+-+cucumber$xtrandard.csv')

    assert 'https://github.com/infamily/_/wiki/topic#google-plus' == fn2url('GH~infamily+_+topic$google-plus.csv')
