# CSS

## Introduction
CSS stands for Cascading Style Sheets. It is used to add styling and format to HTML. There are three ways to add styling: using inline CSS, adding an internal stylesheet, or adding an external stylesheet.

![css](http://media2.giphy.com/media/13FrpeVH09Zrb2/giphy.gif)

### Inline CSS
````html
<div style="color: green;">Bulbasaur</div>
````
The code above turns the word, `Bulbasaur` green.

### Internal Stylesheet
```html
<head>
  <style>
    body {
      width: 800px;
      background-color: rebeccapurple;
    }
  </style>
</head>
```

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


### CSS Syntax
````css
selector {
  property1: value1;
  property2: value2;
  property3: value3;
}
````
The basic format of CSS - you have a selector that picks an HTML element by tag name, id name, or class name.
* To select for a tag, just write the tag name.
```html
<div>hello world</div>
```
```css
div {
  color: blue;
}
```
* To select for an element with a particular `id`, precede the id name with a hashtag, `#`.
```html
<div id="greeting">hello world</div>
```
```css
#greeting {
  color: yellow;
}
```
* To select for an element with a particular `class`, precede the class name with a period, `.`
```html
<div class="stuy">stuyvesant</div>
```
```css
.stuy {
  color: red;
}
```


### Display: block vs inline
Block elements extend as far across the page as possible. A `<div>` is the standard block element.

Inline elements take up on the space they need. A `<span>` is the standard inline element.  

Paste the code below to observe the difference between a `div` and a `span`.
```html
<span style="background: rebeccapurple;">It was the best of times,</span>
<span style="background: rebeccapurple;">it was the worst of times,</span>
<div style="background: cornflowerblue;">it was the age of wisdom,</div>
<span style="background: rebeccapurple;">it was the age of foolishness,</span>
<span style="background: rebeccapurple;">it was the epoch of belief,</span>
<span style="background: rebeccapurple;">it was the epoch of incredulity,</span>
<div style="background: cornflowerblue;">it was the season of Light, </div>
```

## Activity
1) Find your favorite CSS color [here](http://colours.neilorangepeel.com/).
2) Split the list of CSS properties below with the person next to you and research what they do and what possible values are.
* `color`
* `background-color`
* `font-family`
* `font-size`
* `width`
* `height`
* `border-radius`
* `text-align`
* `text-decoration`
* `font-weight`


## Resources
* Import a font - [instructions here](./importing_fonts.md)
* Upload a webpage to GitHub - [instructions here](../html/github_pages.md)
