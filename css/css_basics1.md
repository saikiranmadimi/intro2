# CSS

## Introduction
CSS stands for Cascading Style Sheets. It is used to add styling and format to HTML. There are three ways to add styling: using inline CSS, adding an internal stylesheet, or adding an external stylesheet.

### Inline CSS
````html
<div style="color: green;">Bulbasaur</div>
````
The code above turns the word, `bulbasaur` green.

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
* To select for an element with a particular `id`, precede the id name with a `#`.
```html
<div id="greeting">hello world</div>
```
```css
#greeting {
  color: yellow;
}
```
* To select for an element with a particular `class`, precede the class name with a `#`
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
<span>It was the best of times,</span>
<span>it was the worst of times,</span>
<div>it was the age of wisdom...</div>
<span>it was the age of foolishness,</span>
<div>it was the epoch of belief,</div>
<span>it was the epoch of incredulity,</span>
<div>it was the season of Light, </div>
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
* Use [Google Fonts](https://www.google.com/fonts)!
* Post your website to Github.
  - Create a new repository named `<username>.github.io`.
  - Upload an `index.html` to the repo.
  - Type `<username>.github.io` in the address bar of your browser. Your stuff is live! (But it might actually take a few minutes to go live.)
