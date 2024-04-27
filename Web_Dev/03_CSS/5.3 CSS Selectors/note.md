# CSS Selectors
CSS Selector: the part that selects the HTML in order to apply whichever rules go in between these curly braces. 

## Element Selector: 
Selects a particular HTML tag
### Example
```
h2 { # targeting all h2 s
	property: value
}
```

## Class Selector
### Class
1. Something we can add as an attribute to any HTML Element. In order to group elements in HTML file to apply the same CSS rule to all of them.
2. Even for different type of elements, if their class are the same, they will change simultaneously.
```
<h2 class=“red-text”>Red</h2>
```

### Example

```
.red-text { # the name of the class we’re selecting(exactly same)
	property: value # color: red;
}
```

## ID Selector
### Difference compared to Class Selector
- Class: many elements can be applied
- ID: apply to one element in a single HTML file (unique)

### Example
```
<h2 id=“main”>Red</h2> # Set the ID
```

```
#main { # name of the id
	property: value
}
```

## Attribute Selector
### Example
```
h2[draggable=“true”] { # Select all paragraph elements with the attribute draggable equals true
	property: value
}
```

## Universal Selector
Apply the style to everything where the style sheet is active.

### Example
```
* {
    property: value
}
```
