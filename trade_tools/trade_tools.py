"""trade_tools: Tools To Work With Financial Data
"""

class Asset:
	"""An asset.

    An asset is anything that can be traded.

	Attributes:
        name: A string representing the name of the asset.
	"""

	def __init__(self, name=''):
		self.name = name
