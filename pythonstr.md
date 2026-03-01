## Quotes Inside Quotes
You can use quotes inside a string, as long as they 
don't match the  quotes surrounding the string:

## Assign String to a Variable

Assigning a string to a variable is done with the 
variable name followed by an equal sign and the  string:

## Strings are Arrays 
Like many other popular programming languages, strings in Python are 
arrays of unicode characters.
However, Python does not have a character data type , a single character is 
simply a string with a length of 1.

Square brackets can be used to access elements of the string.

## Looping Through a String 

## Since strings are arrays, we can loop through the characters in a string ,
with a `for ` loop

[Python-string Method](https://www.w3schools.com/python/python_strings_methods.asp)

## Python has a set of built-in methods that you can use on strings.

The `capitalize()` method returns a string where
the first character is upper case, and the rest in lower case.
## Syntax
string.capitalize()
## Parameter Values
No parameters

[Python string casefold()](https://www.w3schools.com/python/ref_string_casefold.asp)

## Definition and Usage
The `casefold()` method returns a string where all the  characters are lower case.
This method is similar to the `lower()` method, but the `casefold()` method is stronger,
more aggressive ,meaning that it will convert more characters into lower case,
and will find more matches when comparing two strings and 
both are converted using the `casefold()` method.

## Syntax
string.casefold()

## Python String center() Method
 The `center()` method will center align the string,
 using a  specified character(space is default) ast he
 fill character.

 ## Syntax
 string.center(length,character)
 ## Python String count() Method
 Return the number of times the value "apple" appears in the string:
 ## The `count()` method returns the number of times a specified valued appears in the string.
 ## Syntax
 string.count(value,start,end)
 