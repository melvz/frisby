
import datetime

class Account(object):

	def __init__(self, name=None, balance=0, number=None):
		self.number = number
		self.name = name
		self.balance = balance
		self.date_opened = datetime.datetime.now()
		self.is_open = True



