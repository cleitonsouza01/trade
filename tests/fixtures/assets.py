"""A set of assets for the tests."""

from __future__ import absolute_import

from trade import Asset
from trade.plugins import Option


ASSET = Asset(symbol='some asset')
ASSET2 = Asset(symbol='some other asset')
ASSET3 = Asset(symbol='even other asset')

OPTION1 = Option(
    symbol='some option',
    underlying_assets={ASSET: 1},
    expiration_date='2015-10-02'
)
