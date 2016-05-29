"""A set of assets for the tests."""

from __future__ import absolute_import

from trade import trade

from trade_app.options import Option


ASSET = trade.Asset(symbol='some asset')

OPTION1 = Option(
    symbol='some option',
    underlying_assets={ASSET: 1},
    expiration_date='2015-10-02'
)
