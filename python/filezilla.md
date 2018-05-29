# FileZilla
1. Make a `public_html` in your user account folder.

2. Use the FileZilla to go to sftp://149.89.160.101 and you'll need to enter your student ID and password.  When a directory is displayed, navigate to your public_html directory.

3. More resources for web related python:
http://bert.stuy.edu/pbrooks/ml2/html_forms_guide.htm

4. Here is a sample website with forms:
http://bert.stuy.edu/pbrooks/ml2/SampleQuestions.htm



Simple way to get and use form data:

See the following two files working together here:
http://marge.stuy.edu/~konstans/formdemo/

1. Create a form on your website. This can be an html file, or even a py file.
```html
<form method="GET" action="formhandler.py">
Name:
<input type="text" name="name" size="20" value="Bob"><br>
Repeat:
<input type="text" name="count" size="20" value="0"><br>
<input type="submit" name="varname" value="I'm done.">
</form>
```

2. Create a form handling python program:
```
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


print head

main()

print ''' </body>
</html>'''


# I include this function to convert a python cgi field storage to a standard dictionary.
# This is good enough for 95% of all forms you would want to create!
def cgiFieldStorageToDict( fieldStorage ):
   """Get a plain dictionary, rather than the cgi module field storage."""
   ans = {}
   for key in fieldStorage.keys():
     ans[ key ] = fieldStorage[ key ].value
   return ans

def main():
    # ask the library function to retrieve all answers and put them
    #   into a dictionary
    form = cgiFieldStorageToDict(cgi.FieldStorage())


    #ONLY FOR DEBUGGING
    #print the form data!
    print form
    print "<br>"

    #lets say you want 2 pieces of information, the name, and the count (number of times to print the name)

    #pick some values that you want as default
    count = -1
    #try to replace it using the form (if it exists!)
    if "count" in form:
        #the data must be integer formatted!
        count = int(form['count'])

    #pick default value
    name = -1
    #try to replace it
    if "name" in form:
        name = form["name"]

    #after getting all the info you need, you can now
    #print the body of your html using the variables that
    #you initialized with the form elements.
    if count == -1 or name == -1:
        #ERROR BODY HERE
        print "<h2>error! Did not receive all required form data!</h2>"
    else:
        #GOOD BODY HERE
        for i in range(count):
            print "Hi "+form["name"]+"!<br>"
```
