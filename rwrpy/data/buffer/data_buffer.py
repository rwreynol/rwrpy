'''
author: randall
4/7/2019
'''

class signal_buffer(object):
	'''
	a class for holding data in lists
	'''

	def __init__(self,length=100,n=1,default=0):
		'''
		constructor. initializes the data buffer.

		length: length of the data buffer
		n: the number of time series
		default: the default value of the array
		'''
		self.data = []
		self.reset(length,n,default)

	def reset(self,length=100,n=1,default=0):
		'''
		resets the data buffer to the default value

		length: length of the data buffer
		n: the number of time series
		default: the default value of the array
		'''
		for _ in range(n): self.data = [default] * length

		