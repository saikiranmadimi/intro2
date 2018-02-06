# CSS

## `<div>` vs `span`
A `div` is the standard block element. A block-level element occupies the entire space of its parent element (container), thereby creating a "block."
```html
<span style="background: rebeccapurple;">It was the best of times,</span>
<span style="background: rebeccapurple;">it was the worst of times,</span>
<div style="background: cornflowerblue;">it was the age of wisdom,</div>
<span style="background: rebeccapurple;">it was the age of foolishness,</span>
<span style="background: rebeccapurple;">it was the epoch of belief,</span>
<span style="background: rebeccapurple;">it was the epoch of incredulity,</span>
<div style="background: cornflowerblue;">it was the season of Light, </div>
```


## Box Model
Every HTML element has three properties you can manipulate:
* padding
* border
* margin
![boxmodel](http://czechowski.pl/images/posts/box-model.png)
```css
body {
  padding: 25px 50px 75px 100px;
  border: 2px solid black;
  margin: 25px 50px 75px 100px;
}
```
In the code above:
* top padding and margin are 25px
* right padding and margin are 50px
* bottom padding and margin are 75px
* left padding and margin are 100px
* the border is 2px wide and colored black
