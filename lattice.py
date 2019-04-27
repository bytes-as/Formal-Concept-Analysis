import sys;
import pandas;
from concept import Concept;
""" class Lattice contains a list of all the concepts are
	derived from the indput dataset as pandas dataframe"""
if not 'pandas' in sys.modules:
	print("Fail to load pandas...\ncheck the pandas intallation\nterminating...");
	sys.exit();


class Lattice:
	def __init__(self, dataframe=None):
		""" verifying the input dataset """
		if isinstance(dataframe, pandas.DataFrame) or dataframe == None:
			self.dataframe = dataframe;
		else :
			print("Argument should be a pandas dataframe");
			return None;
		""" initializing the class variables """
		if self.dataframe is not None:
			""" print cross table"""
			self.__print_cross_table__();
			""" creating lattice """
			self.lattice = self.__create_lattice__();
			"""printitng lattice / all the concepts"""
			self.__print_lattice__();

	""" if not included at the time of initializing 
		also can change the dataset given as input"""
	def __add_dataframe__(self, dataframe):
		if isinstance(dataframe, pandas.DataFrame):
			self.dataframe = dataframe;

	""" create a lattice by finding all the concepts it shoudl
		contain according to the given input as dataframe """
	def __create_lattice__(self):
		if self.dataframe is None:
			print("Load the dataframe first\n__add_dataframe__(<type pandas.DataFrame>)");
			return None;
		# will contain a list of concepts (extent, intent)
		concepts = list();
		extents = self.__get_extent_list__();
		for ex in extents:
			# print(ex, end=" --> ");
			# print(self.__get_intent__(ex));
			concepts.append(Concept(set(ex), self.__get_intent__(ex)));
		return concepts;

	""" printing the concepts contained by the lattice """
	def __print_lattice__(self):
		print("------------------ Lattice ------------------")		
		if self.lattice is not None:
			for concept in self.lattice:
				print(concept.extent, "<-->", concept.intent);
			print("");
		else :
			pass;

	""" print the cross table/ or the context TB more precise"""
	def __print_cross_table__(self):
		print("------------ Dataframe imported ------------")
		print(self.dataframe, end="\n\n");

	""" generate all the set of object list in the complete
		lattice and append them into the list, return this list"""
	def __get_extent_list__(self):
		extents = set();
		for j in range(len(self.dataframe.columns)):
			extent = set();
			for i in range(len(self.dataframe.index)):
				if(self.dataframe.iloc[i][j] == 1):
					extent.add(self.dataframe.index[i]);
			extents.add(frozenset(extent));
		extent_list = list(extents);
		for i in range(len(extent_list)):
			for j in range(i, len(extent_list)):
				extents.add(frozenset(extent_list[i] & extent_list[j]));
		# add the extent containing all the objects just in case it left out
		extent = set();
		for index in self.dataframe.index:
			extent.add(index);
		extents.add(frozenset(extent));
		# convert set to a list for sorting and return the list
		extents = list(extents);
		extents.sort(key=lambda x:len(x), reverse=False);
		_extents = [set(e) for e in extents];
		return _extents;

	""" Create a list of attributes for a given set of objects
		passed ass argument according to the cross table/ context"""
	def __get_intent__(self, extent):
		intent = set();
		if len(extent) == 0:
			for attribute in self.dataframe.columns:
				intent.add(attribute);
			return list(intent);
		extent_list = list(extent);
		for attribute in self.dataframe.columns:
			if self.dataframe.loc[extent_list[0]][attribute] == 1:
				intent.add(attribute);
		for i in range(1, len(extent_list)):
			temp_intent = set();
			for j in range(len(self.dataframe.columns)):
				if self.dataframe.loc[extent_list[i]][j] == 1:
					temp_intent.add(self.dataframe.columns[j]);
			intent = intent & temp_intent;
		return list(intent);

	""" return infimum for the lattice formed"""
	def __get_infimum__(self):
		infimum = self.lattice[0];
		print("< Infimum", end=" ");
		infimum.__print__(" ");
		print(">");
		return infimum;

	""" return supremum for the lattice"""
	def __get_superemum__(self):
		supremum = self.lattice[-1];
		print("< Supremum", end=" ");
		supremum.__print__(" ");
		print(">");
		return self.lattice[-1];

	""" intension function for finding common properties"""
	def __intension__(self, objects):
		if isinstance(objects, set):
			objects = list(objects);
		max_len = len(self.lattice);
		intent_concept = self.lattice[-1];
		for concept in self.lattice:
			if set(objects).issubset(concept.extent) and len(concept.extent) <= max_len:
				intent_concept = concept;
				# intent_concept.__print__();
				max_len = len(concept.extent);
		print("< Intension(", end="");
		print(set(objects), end="");
		print(") --> ", end="");
		print(intent_concept.intent, end="");
		print(" >");
		# intent_concept.__print__();
		return intent_concept;

	""" extension for searching objects having given properties"""
	def __extension__(self, attributes):
		if isinstance(attributes, set):
			attributes = list(attributes);
		min_len = len(self.lattice[0].extent);
		extent_concept = self.lattice[0];
		for concept in self.lattice:
			if set(attributes).issubset(concept.intent) and len(concept.extent) >= min_len:
				extent_concept = concept;
				# intent_concept.__print__();
				min_len = len(concept.extent);
		print("< Extension(", end="");
		print(attributes,end="");
		print(") --> ", end="");
		print(extent_concept.extent, end="");
		print(" >");
		# extent_concept.__print__();
		return extent_concept;

	""" search concept for the given set of objects """
	def get_concept_from_objects(objects):
		for concept in self.lattice:
			if concept.extent == set(objects):
				return concept;
		return set();

	""" serach concept for given set of attributes """
	def get_concept_from_attributes(attributes):
		for concept in self.lattice:
			if set(concept.intent) == set(attributes):
				return concept;
		return set();

dataframe = pandas.read_csv("test.csv", index_col=0);
l = Lattice(dataframe);
l.__get_infimum__();
l.__get_superemum__();
l.__intension__({'1sg','2pl'});
l.__extension__({'1', '-3'});

# l = lattice();
# l.__add_dataframe__(dataframe);
# l.__print_cross_table__();

# attributes = list(dataframe.columns);
# super_set = power_set(attributes);

# for i in super_set:
	# print(i);

if __name__ == "lattice":
	main();