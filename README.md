# Formal-Concept-Analysis
A principled way of deriving a concept hierarchy or formal ontology from a collection of objects and their properties. Each __concept__ in the hierarchy represents the objects sharing some set of properties and each __sub-concept__ in the hierarchy represents a subset of the object in the concepts above it.
The package includes the implementation of lattice structures of the above called concepts and the methods of __Formal Concept Analysis__:
It provides a mathematical model for describing set of __objects__ with the set of __properties__. Methods included in the package are :
* supremum
* Infimum
* Intenstion
* Extension

Since the set of concepts of the lattie are in ordered form, the method _infimum_ and _supremum_ aren't something that is being calculated, they are the first and last concept in the set of concept that is the __lattice__.

This model is yet to be used in actual application since the formation of lattice is very time consuming but it's approach is better than what other model provides.

The input is taken from the csv file in the directory named `test.csv`. To have it run on some other data input change the file path in the `lattice.py` and interpret the script `lattice.py` with python3 interepreter.
```
python lattice.py
```
