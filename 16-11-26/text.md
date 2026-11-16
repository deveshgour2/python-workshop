# string:- 
string is a collection of alphabets, numbers and symbols. Python does not support char datatype. single char/multiple char specified in double quotes, called string.

=> string is ordered in nature. default indexing start with "0"
=> string is immutable/unchangable in nature.
=> string belongs to wrapper class <class:str>

# Methods:- 

1. upper():- to convert any string to uppercase
2. lower():- to convert any string to lowercase
3. capitalize():- capitalizes only the first character of string.
4. title():- capitalizes the first letter of every word.
5. swapcase():- inverts lowercase to uppercase and vice-versa.
6. strip():- removes left + right whitespaces.
syntax = var ref_name = str.strip()

7. replace():- replaces old string with new string.
syntax= refname = strname.replace(oldstring, newstring, count)
here count parameter is optional

8. split():- for split the string at specified position.
syntax = return list = strname.split(delimiter)

9. join():- joins elements of iterable into a single string.
syntax= seperator.join(iterable)

exp.words = ["Python", "is", "easy"]
print("-".join(words))

10. find():- return the index of the first occurence of a substring. returns -1 if the substring is not found.
syntax = string_name.find(substring)

exp. 
text = "learn python"
print(text.find("python"))

11. count():- returns the number of times a substring appears in the str

============================================================

# string function for checkig valid format:- 
1. isalpha():- to check the string contain alphabet or not.

2. isupper():- to check the string is uppercase or not.

3. isnumeric():- to check string contain number or nit

4. isalnum():- 

5. islower():- 