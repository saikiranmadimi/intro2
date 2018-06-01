## Final Project Tools

### Submitting Form Information
1. You need to include a method and action attribute in the opening form tag. The value for the method should be the string `GET` and the value for the action should be the name of a python file.
2. The submit button triggers the execution of the python file specified in the opening tag of the form.
```html
<form method="GET" action="PYTHON_FILE">
  <input type="submit" name="submit" value="submit">
</form>
```
### Getting HTML Form Data as a Dictionary
3. The `#!/usr/bin/python` tells the computer to execute python on the file.
4. `import cgi` gives you access to `cgi.FieldStorage()`, which stores all the form information from the HTML page that uses it.
5. `cgtib` is a tool that allows for you to see error messages in the browser. It is also helpful to run your python files in the terminal to check that it runs smoothly before dragging it over to the school's server with FileZilla.
6. If you call `convertToDictionary(cgi.FieldStorage())`, you'll get a dictionary back with all the information you filled into the html form.
```python
#!/usr/bin/python
print "Content-type: text/html\n"

import cgi

# displays error messages in your browser
import cgitb
cgitb.enable()

# function that will package all form information in a python dictionary
def convertToDictionary(fieldStorage):
   output = {}
   for key in fieldStorage.keys():
     output[key] = fieldStorage[key].value
   return output

form = convertToDictionary(cgi.FieldStorage())
```
### Reading CSV Files
```python
fh = open("filename", "r")
data = fh.readlines() #returns a list, each item is a line
for row in data[1:]:
  #removes the \n character and turns each row from a string to an array of values
  row = row[:-1].split(",")
```

### HTML String Formatting
1. Triple quotation marks allow for strings to span multiple lines.
```python
html = '''
<!DOCTYPE html>
<html>
  <head></head>
  <body>{}</body>
</html>
'''
html.format("hello world") # returns the string with hello world inserted
```
2. Loops combined with the string format method can help you repetitive HTML patterns.
```python
options = ""
fruits = ["apple", "orange", "banana", "durian"]
for fruit in fruits:
  options += "<option value={fruit}>{fruit}</option>".format(fruit = fruit)

dropdown = "<select>{options}</select>".format(options = options)
```
