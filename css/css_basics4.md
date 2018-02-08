# CSS

## Importing fonts
1) Search for a font [here](https://fonts.google.com/).
2) Click the (+) add button. A small window will appear at the bottom.
3) Click the small window.
4) Copy and paste the `<link>` tag into the `head` section of your html page.
```html
<head>
  <link href="https://fonts.googleapis.com/css?family=Rammetto+One" rel="stylesheet">
</head>
```
5) You now have access to the font you added.
```css
body {
  font-family: "Rammetto One";
}
```


## float
The `float` property can force elements to be on the same level. `div` elements are supposed to be block elements that take up their own line, but `float` overrides that default setting of `div`s.
```html
<div class="parent">
  <div class="child">1</div>
  <div class="child">2</div>
  <div class="child">3</div>
</div>
```

```css
.parent {
  width: 400px;
  height: 120px;
  background: cornflowerblue;
}
.child {
  width: 100px;
  height: 100px;
  float: right;
  background-color: rebeccapurple;
  margin-right: 25px;
  margin-top: 10px;
}
```

## percentage
The width and height property can also be set as a percentage, in which case the element assumes a percentage of its parent's height or width.
```html
<div id="taller">I'm 50 pixels tall.</div>
<div id="shorter">I'm 25 pixels tall.</div>
<div id="parent">
  <div id="child">
    I'm half the height of my parent.
  </div>
</div>
```
```css
div {
  width: 250px;
  margin-bottom: 5px;
  border: 2px solid blue;
}

#taller {
  height: 50px;
}

#shorter {
  height: 25px;
}

#parent {
  height: 100px;
}

#child {
  height: 50%;
  width: 75%;
}
```
