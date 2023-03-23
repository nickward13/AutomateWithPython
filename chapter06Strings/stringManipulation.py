import pyperclip

# strings are arrays
spam = 'Hello, world!'
print(spam[0])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[7:])

# special characters
print('''Here are some special characters:

\\' single quote
\\" double quote
\\t tab
\\n newline
\\ backslash
''')

# in and not in operators
print('Hello' in 'Hello, world!')
print('Hello' not in 'Hello, world!')
print('HELLO' in 'Hello, world!')
print('' in 'spam')

# string concatenation
print('Hello' + ' world!')
name = 'Al'
age = 4000
print('My name is ' + name + '. I am ' + str(age) + ' years old.')
print('My name is %s. I am %s years old.' % (name, age))
print(f'My name is {name}. I am {age} years old.') # note f-string

# upper, lower and other
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.isalnum())
print(name.istitle())
print(name.startswith('A'))
print(name.endswith('Ward'))

# join and split
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('Hello, world!'.partition('w'))

# formatting
print('Hello'.rjust(10))
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10))
print('Hello'.ljust(10, '-'))
print('Hello'.center(10))
print('Hello'.center(10, '='))

# remove whitespace with strip(), rstrip() and lstrip()
spam = '     Hello, World     '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

# ASCII
print(ord('A'))
print(ord('a'))
print(chr(65))

# copy and paste
pyperclip.copy('Hello, world!')
print(pyperclip.paste())
