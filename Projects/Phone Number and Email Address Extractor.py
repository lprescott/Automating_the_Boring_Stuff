#! python3
import re, pyperclip as clipboard

# Get the text off the clipboard.
# Wait for user input
input("\nPress Enter when String to be searched is on clipboard...\n")

user_input = str(clipboard.paste())

# Find all phone numbers and email addresses in the text.
# Regex for phone number
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Regex for email address
emailRegex = re.compile(r'''(
    ([\S]+)                         # local-part
    (@)                             # @
    ([\S]+)                         # domain
    (\.)                            # .
    ([\S]+)                         # type
    )''', re.VERBOSE)
    
# search
matches = []
for groups in phoneRegex.findall(user_input):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(user_input):
    matches.append(groups[0])
    
# paste them onto the clipboard.
if len(matches) > 0:
    clipboard.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# Wait for user input
input("\nPress Enter to exit...")