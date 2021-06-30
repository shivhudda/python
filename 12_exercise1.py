'''The details and functionalities that are essential and must be present are:
User will give a word as an input. Suppose that the word is present in your dictionary along with its definition or meaning.
The program will print the meaning or definition of that word.'''

# Solution
print("welcome\n find about programming languages:\n1.Python\n2.C++\n3.HTML")
user_input=str(input('Enter your choice:'))
dict1= {}
dict1.update({'Python':'Python is an interpreted high-level general-purpose programming language. Python''s design philosophy emphasizes code readability with its notable use of significant indentation. '})
dict1.update({'C++':'C++ is a general-purpose programming language created by Bjarne Stroustrup as an extension of the C programming language, or "C with Classes".'})
dict1.update({'HTML':'The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets and scripting languages such as JavaScript.'})

print(dict1[user_input])
