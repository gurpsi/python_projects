print('Hello world')

message = 'back to BASICS + Hello world'

# Lower function
print('message in lower case:',message.lower())

# Upper function
print('{}'.format(message.upper()))

# Count function
print('Count of back in message:',message.count('back'))

# Find function
print("Find where 'hello' word comes in the message:",message.find('Hello'))

# Replace function
new_message = message.replace('world','git')
print('After replacement:', new_message)

# Concatenation
print('Concatenating 2 strings:', message  + ' & ' + new_message)

# For python 3.6 and above fstring:
string = "{},' & ',{}".format(message,new_message)
fstring = f"{message},' & ',{new_message}"
print(string)
print(fstring)

print(string,'\n',fstring)

