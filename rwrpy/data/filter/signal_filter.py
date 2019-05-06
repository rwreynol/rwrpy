from scipy.signal import medfilt

class data_filter(object):
	''' an abstract class for signals '''

	def __init__(self):
		''' constructor '''
		self._name = type(self).__name__

	def filter(self,data):
		''' abstract method for returning filtered data '''
		return Nones

class no_filter(data_filter):
	''' a class for not filtering signals '''

	def __init__(self):
		''' constructor '''
		super().__init__()

	def filter(self,data):
		''' returns unfiltered signals '''
		return data

class median_filter(data_filter):
	''' a class for median filtering signals'''

	def __init__(self,n=15):
		''' constructor '''
		super().__init__()
		self.setWindow(n)

	def setWindow(self,n=15):
		''' sets the window size '''
		self._n = n

	def filter(self,data):
		''' returns the median filtered data '''
		return medfilt(data)