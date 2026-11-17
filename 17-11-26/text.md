# set methods:-
1. add()
2. pop()
3. remove()
4. discard()
5. clear():- for clear remove all data from set but structure not remove
syntax = setname.clear()

6. difference():- difference function show the unique element of first specified set(base set)

7. intersection():- intersection function shows the common element of both specified set.

8. union():- the combine two set element and store in 3rd set but duplicate element add one time.

9. update():- for update an existing set by another set.

10. del keyword

============================================================

# dictionary:-
it is a collection of similar + different-different data types value.

-> it stores data in key value format
-> key data can be int or str
-> key value must be unique
-> its belongs to wrapper class <class:dict>
-> dict is ordered collection of element
-> its mutable or changeable in nature

syntax:- ref_var_name = {"key1:value","key2:value","key3:value",}

double quotes is only used for string

# dictionay methods:- 
1.update():- for add new element un existing dictionary in key anad value pair. if key is already exists it only modify the value.

* syntax :- dictname.update({key:value})

2. keys():- it returns all keys of dictionary.
* syntax:- dictname.keys()

3. values():- returns a list of all the values available in given dictionary.
dictname.values()

4. items():- returns the list with all dictionary key with values. 
dictname.items()

5. pop():- removes the specified element from the dictionary on the basis of key.
dict.pop("key")

6. popitem():- removes the last inserted key:value pair from the dictionry and returns its a tuple.
dict.popitem()

7. get():- returns the value for the given key.
value = dict.get(key)

8. copy():- returns a shallow copy of original dict. it changes in old dict, new/copy dict will not affected by this 
dict.copy()

9. clear():- removes all the elements from the dictionary structure remains same.
dict.clear()

============================================================

# shallow copy:- 
shallow copy create a new object but retain reference to the object contained within the original. it only copies the top level structure without duplicating nested elements.

add module - import copy
copy module provides a method copy()
* syntax :- ref = copy.copy(reference)

* note:- modifying shallow copies are also reflected in original reference.
1. faster and consuming less memory head

# deep copy:- 
creates a new component object before inserting of the items/data found in the original. it perform copy in  recursive manner. any changes medo of to a copy of the object do not reflect in the original object.

reference = copy.deepcopy(reference)

* note:- 
1. slower as compare to copy()
2. higher memory overhead.