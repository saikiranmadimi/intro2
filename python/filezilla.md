## How to get HTML to run a Python file

1. Make sure you have a folder named `public_html` in the home directory of your Stuyvesant computer account.

2. Open Filezilla and fill in the following fields -  
- Host: `sftp://149.89.160.101`
- Username: <YOUR_STUYVESANT_COMPUTER_LOGIN>
- Password: <YOUR_STUYVESANT_COMPUTER_PASSWORD>

3. Create an `.html` in your `public_html` folder
```html
<form method="GET" action="formhandler.py">
  Name: <input type="text" name="name" size="20" value="Bob"><br>
  Repeat: <input type="text" name="count" size="20" value="0"><br>
  <input type="submit" name="varname" value="I'm done.">
</form>
```

4. Make a file specifically named `formhandler.py` in your `public_html` folder.
```python
#!/usr/bin/python
print "Content-type: text/html\n"


# We need these library modules to retrieve the user's answers
import cgi

#help you see errors
import cgitb
cgitb.enable()



head = '''<!DOCTYPE html>
<html>
  <head>
   <title>Demo!</title>
  </head>
  <body>'''

# I include this function to convert a python cgi field storage to a standard dictionary.
# This is good enough for 95% of all forms you would want to create!
def cgiFieldStorageToDict( fieldStorage ):
   """Get a plain dictionary, rather than the cgi module field storage."""
   ans = {}
   for key in fieldStorage.keys():
     ans[key] = fieldStorage[key].value
   return ans

def main():
    # ask the library function to retrieve all answers and put them
    #   into a dictionary
    form = cgiFieldStorageToDict(cgi.FieldStorage())


    #ONLY FOR DEBUGGING
    #print the form data!
    print form
    print "<br>"

print head

main()

print ''' </body>
</html>'''
```

5. Once you're logged into FileZilla, find the `formhandler.py` file in the right column. Right-click and select `File Permissions`. Check off all of the `Execute` checkboxes.

6. Navigate to `marge.stuy.edu/~USERNAME` and click through to the `html` page you created. Fill out the form and submit. **YOU HAVE TO GO TO THE HTML PAGE FIRST**
