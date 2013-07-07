class Volume:
	def __init__(self):
		self.vol=50

	def get_vol(self):
		return self.vol

	def set_vol(self,vol):
		print 'VOL CHANGE', vol
		self.vol=vol

	commands={
		'set_vol':set_vol
	}

	parameters={
		'vol':get_vol
	}

	constants={
		'class':'volume'
	}