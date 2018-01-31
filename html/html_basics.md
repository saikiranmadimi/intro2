# HTML

## Objectives
* Be able to use foundational HTML tags(`head`, `body`, `a`, `div`...) to build a simple webpage

## Introduction
HTML stands for HyperText Markup Language. It is used to organize the content on a webpage. Web browsers recognize files with the suffix - `.html`. Content that you want displayed onto a webpage is placed between one opening and one closing tag:

```html
<div> Hello World </div>
```

The opening tag is characterized by the tag name enclosed in angled brackets: `< tagName >`. The closing tag is also characterized by angled brackets, but the tag name is preceded with a backslash: `< / tagName >`

### Standard Template
```html
<!DOCTYPE HTML>
<html>
  <head></head>
  <body></body>
</html>
```

### Common HTML Tags
#### Page Title
```html
<head>
  <title>WOOPEGSOOIE</title>
</head>
```

#### Headers
```html
<h1> Hello World </h1>
<h2> Hello World </h2>
<h3> Hello World </h3>
<h4> Hello World </h4>
<h5> Hello World </h5>
<h6> Hello World </h6>
```

#### Lists
```html
  <ul> Numbers
    <li> 1 </li>
    <li> 2 </li>
    <li> 3 </li>
  </ul>
```
```html
  <ol> Pokemon
    <li>Bulbasaur</li>
    <li>Charmander</li>
    <li>Squirtle</li>
  </ol>
```

#### Line Break
```html
Congratulations! <br>
Today is your day. <br>
You're off to Great Places! <br>
You're off and away! <br>

You have brains in your head. <br>
You have feet in your shoes. <br>
You can steer yourself <br>
any direction you choose. <br>
You're on your own. And you know what you know. <br>
And YOU are the guy who'll decide where to go. <br>
```

#### Images
```html
<tag attribute="value"></tag>
```

```html
<img src="http://www.arborbrothers.org/wp-content/uploads/2014/10/C4Q_official-logo-horizontal-color-green.jpg" alt="c4q-logo"/>
```
The source(src) attribute specifies what image is being rendered onto the page, whereas the alternate(alt) attribute provides what text to display if the image cannot render.

Notice anything weird about the code above? It's called a self-closing tag. Because the image doesn't have any text content, we don't need two tags.

#### Links
The URL(https://developer.mozilla.org) within the quotation marks determines where you're taken when the link is clicked. Whatever is inside of the html tags(MDN) is what's displayed on your actual page.
```html
<a href="https://developer.mozilla.org">MDN</a>
```

## Activity
[Source: Coder](https://googlecreativelab.github.io/coder-projects/projects/perfect_recipe/)

### Instructions
Make a page of your favorite recipe. It should look similar to this:

![pb&j](https://github.com/C4Q/AC_4_Web/blob/master/units/html/projects/lists/assets/screenshot.png?raw=true)

Include the following:
1. A main heading
2. A description
3. An unordered list of ingredients
4. An ordered list of directions
5. Add an image below the main heading

## Resources
1) [HTMLDog - HTML Tags](http://www.htmldog.com/references/html/tags/)
2) [Mozilla - HTML Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes)
