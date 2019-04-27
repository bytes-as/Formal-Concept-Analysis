class Concept:
	def __init__(self, extent=None, intent=None):
		if isinstance(extent, set) or extent == None:
			self.extent = extent;
		else :
			print("First arguments is to be given as set of objects");
			return None;
		if isinstance(intent, list) or intent == None:
			self.intent = intent;
		else :
			print("Second argument is to be given as list of attributes");
			return none
		# self.__print__();
	
	def __add_intent__(self, intent):
		if isinstance(intent, list):
			self.intent = intent;
		else : print("Type error: expected type of list");

	def __add_extent__(self, extent):
		if isinstance(extent, set):
			self.extent = extent;
		else : print("Type error: expected type of set");

	def __intent__(self):
		return self.intent;

	def __extent__(self):
		return extent;

	def __print__(self, e="\n"):
		print(self.extent,"<-->",self.intent, end=e);