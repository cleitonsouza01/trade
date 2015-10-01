"""trade: Tools For Stock Trading Applications.

Copyright (c) 2015 Rafael da Silva Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from __future__ import absolute_import

from .operation import Operation


class Asset:
    """An asset represents anything that can be traded.

    Attributes:
        name: A string representing the name of the asset.
        symbol: A string representing the symbol of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the asset, if any.
    """

    def __init__(self, name=None, symbol=None, expiration_date=None):
        self.name = name
        self.symbol = symbol
        self.expiration_date = expiration_date

    def __deepcopy__(self, memo):
        return self


class Derivative(Asset):
    """A derivative is a asset which derives from one or more assets.

    Derivatives have all the asset attributes and can be traded like
    normal assets.

    This is a base class for derivatives.

    Attributes:
        name: A string representing the name of the asset.
        symbol: A string representing the symbol of the asset.
        expiration_date: A string 'YYYY-mm-dd' representing the
            expiration date of the derivative, if any.
        underlying_assets: A list of Asset objects representing the
            underlying assets of this derivative.
        ratio: By default the ratio is 1, so
            1 derivative = 1 underlying asset.
    """

    def __init__(
                self,
                name=None,
                symbol=None,
                expiration_date=None,
                underlying_assets=None,
                ratio=1
            ):
        self.name = name
        self.symbol = symbol
        self.expiration_date = expiration_date
        if underlying_assets is None: underlying_assets = []
        self.underlying_assets = underlying_assets
        self.ratio = ratio
