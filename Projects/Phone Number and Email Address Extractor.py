#! python3
import re, pyperclip as clipboard

# Get the text off the clipboard.
# Wait for user input
input("\nPress Enter when String to be searched is on clipboard...")
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
phone_numbers = phoneRegex.findall(user_input)
print(phone_numbers)

email_addresses = emailRegex.findall(user_input)
print(email_addresses)


# Paste them onto the clipboard.

# Wait for user input
input("\nPress Enter to exit...")