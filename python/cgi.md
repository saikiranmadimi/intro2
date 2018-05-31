1. Make an html file named `survey.html`.
```html
<form method="GET" action="survey.py">

  Name: <input type="text" name="name" size="20" value="Bob"><br>

  Borough: <br>
  <input type="radio" name="boro" value="queens">Queens <br>
  <input type="radio" name="boro" value="brooklyn">Brooklyn <br>
  <input type="radio" name="boro" value="manhattan">Manhattan <br>
  <input type="radio" name="boro" value="bronx">Bronx <br>
  <input type="radio" name="boro" value="staten_island">Staten Island <br>

  Gender: <br>
  <input type="radio" name="gender" value="male">Male <br>
  <input type="radio" name="gender" value="female">Female <br>
  <input type="radio" name="gender" value="other">Other <br>

  Class: <select name="class">
    <option value="2018">2018</option>
    <option value="2019">2019</option>
    <option value="2020">2020</option>
    <option value="2021">2021</option>
  </select> <br>

  Birthday: <input type="date" name="date"> <br>

  Favorite Food: <input type="text" name="food" size="20" value="pizza"><br>

  <input type="submit" name="varname" value="submit">
</form>
```

2. Make a python file named `survey.py`.
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
  <body>
'''

# I include this function to convert a python cgi field storage to a standard dictionary.
# This is good enough for 95% of all forms you would want to create!
def convertToDictionary(fieldStorage):
   """Get a plain dictionary, rather than a """
   output = {}
   for key in fieldStorage.keys():
     output[key] = fieldStorage[key].value
   return output

def main():
    form = convertToDictionary(cgi.FieldStorage())


    year, pronoun, food = "", "", "nothing"
    classes = {"2018": "senior", "2019": "junior", "2020": "sophomore", "2021": "freshman"}
    if "class" in form.keys():
        year = classes[form["class"]]
    if "gender" in form.keys():
        if form["gender"] == "female":
            pronoun = "she"
        elif form["gender"] == "male":
            pronoun = "he"
    if "food" in form.keys():
        food = form["food"]

    sentence = "<div>{name} is a {year} at Stuyvesant.</div>".format(name = form["name"], year=year)
    sentence2 = "<div>{pronoun} likes to eat {food}.</div>".format(pronoun=pronoun, food = form["food"])
    print sentence + sentence2
    print "<br>"

print head

main()

print ''' </body>
</html>'''
```
