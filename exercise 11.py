import re

mystr = """If you have a common name like mine then you can try different combinations of your name. For Example:

DoeJohn@gmail.com
ItsJohnDoe@gmail.com
ThisIsJohn@gmail.com
JDoe@gmail.com
2: Try using DOT in between names
If Step1 is not working in your case, then you can try adding dot or underscore (if allowed) in your email address name.

For Example:

John[dot]Doe@outlook.com
Doe[dot]John@outlook.com
3: Avoid Using Nicknames
I have seen many emails, people include their nickname and having cool email names like dashing, boy, cute, princess, etc. Seriously, avoid such kind of names while creating any email whether for personal or professional use.

When we are making any email address, we have to make sure that the email name must be easy to remember, easy to pronounce, and meaningful."""

patt = re.compile(r'.*@gmail.com\b')
matches = patt.finditer(mystr)
for match in matches:
    print(match)