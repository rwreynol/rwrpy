'''
author: randall
4/7/2019
'''

class data_state(object):
	'''
	A class detecting when a data state changes
	'''

	def __init__(self,default=None):
		'''
		constructor

		default: defualt state
		'''
		self._state = default

	def isDifferent(self,state=None):
		'''
		Returns whether the state has changed

		state: the new state

		returns: state changed boolean
		'''
		changed = state == self._state
		if changed: self._state = state
		return changed

	def getState(self):
		'''
		returns the current state

		state: the current state
		'''
		return self._state