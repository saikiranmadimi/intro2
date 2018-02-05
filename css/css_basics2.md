# CSS

### Linking to an ID tag
Check out any Wikipedia page that has a table of contents. When you click on a link in the table of contents, you'll be brought to a specific section of the page. Notice that the address or URL of the page has changed to have `#<something>` at the end of it. This is because you can actually make a link to something within a webpage with an ID.

```html
<a href="#green">Green</a>
<a href="#red">Red</a>


<div id="green">Granny Smith</div>
<div id="red">Fuji</div>
```
Clicking on the `Green` link will bring you to the HTML element with an id of `#green`. Clicking on the `Red` link will bring you to the HTML element with an id of `#red`.

### Linking to other HTML Pages
Let's say you have multiple HTML pages you want to display. You can link to another HTML page by using the filename of the other HTML page if it is in the same folder as the HTML page you're currently on. <br>
Let's say you have two HTML pages - `index.html` and `recipe.html`. You want to create a link that brings you to the `recipe` from the `index`. In the index.html, you'll want to use the name of the recipe file as the `href` of a link.

### External Stylesheet
````html
<link rel="stylesheet" href="style.css"  charset="utf-8">
````
You place the above link tag in the `<head>` that references a CSS file. <br>

Inside your `.html` file -
````html
<div>Bulbasaur</div>
````
Inside your `.css` file -
````css
div {
  color: green;
}
````
