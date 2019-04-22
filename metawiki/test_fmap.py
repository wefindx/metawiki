from .fmap import (
    n2f,
    f2n
)

def test_f2n():

    # _:
    assert f2n('_topic#metaculus') == '_:topic#metaculus'

    # ::
    assert f2n('__mindey@topic#metaculus') == '::mindey/topic#metaculus'

    # WD
    assert f2n('WD@Q123') == 'WD:Q123'

def test_n2f():

    # _:
    assert n2f('_:topic#metaculus') == '_topic#metaculus'

    # ::
    assert n2f('::mindey/topic#metaculus') == '__mindey@topic#metaculus'

    # WD
    assert n2f('WD:Q123') == 'WD@Q123'
