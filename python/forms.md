# Forms
You use form elements to input data onto a website. Today we'll discuss some common ones that you come across.

## Text
You use text inputs whenever you need to write to a form.
```html
<input type="text">
```

## Radio Buttons
Think of surveys when you think of radio buttons. Take this personality test in your free time! - [16 personalities](https://www.16personalities.com/)
```html
<input type="radio" name="title" value="Mr.">
  Male <br>
<input type="radio" name="title" value="Ms.">
  Female <br>
```
**What happens when you remove the title attribute?**

## Dropdown List

```html
<select name="usercard">
  <option value="visa">Visa</option>
  <option value="mc">Mastercard</option>
  <option value="amex">American Express</option>
</select>
```
Create a list of all the the classes at Stuyvesant!

## Typical Checkout Page
```html
<h2>Personal information</h2>
<form>
  <div>Title</div>
  <input type="radio" name="title" value="Mr.">
    Male <br>
  <input type="radio" name="title" value="Ms.">
    Female <br>
  <div>Name: </div>
  <input type="text">
  <div>E-mail: </div>
  <input type="email">
  <div>Password: </div>
  <input type="password">
</form>

<h2>Payment information</h2>
<form>
  <select name="usercard">
    <option value="visa">Visa</option>
    <option value="mc">Mastercard</option>
    <option value="amex">American Express</option>
  </select>
</form>

```
