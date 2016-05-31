"""A set of assets for the tests."""

from __future__ import absolute_import

from trade.occurrences import Asset


ASSET = Asset(symbol='some asset')
ASSET2 = Asset(symbol='some other asset')
ASSET3 = Asset(symbol='even other asset')
ASSET4 = Asset(
    name='asset that expires',
    symbol='EXPR',
    expiration_date='2015-12-31'
)
