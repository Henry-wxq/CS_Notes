# Add CSS Into HTML
## Intro to CSS - Cascading Style Sheets
Style sheet: a type of language, allow us to specify how things should look in our website
e.g. CSS, SASS, LESS

```
“property 1: value 1; property 2: value 2; ...”
```

## Add CSS Into HTML
### Inline
#### Feature
1. Used for a single element on the page
   
#### Specification
Add the 'style' attribute to the element tag whereever want to apply
```
<h1 style=“background: blue; color: red”>Head with context red and background blue</h1>
```

### Internal
#### Feature
1. Can apply to anywhere in our HTML document, and inside we can target or select as many elements as we want
2. Used for a signle webpage.

#### Specification
1. Should be added inside head, not in the body part
```
<html>
	<head>
		<style>
			html{ # the selector, select the tag to apply css code below. ’html’ means for the whole documents, can also use `h1`, `p`, etc.
				background: red; # CSS code, setting the background
				color: blue; # CSS code, setting the context color
			}
			
		</style>
	</head>
</html>
```

### External
#### Feature
1. Lives in a completely separate file, normally see as styles.css or main.css or anything
2. Used mostly in web development, for multipage.

#### Specification
Inside the style.css:
```
html{ # the selector
	background: green;
}
```

Link up css file and html file, also should be added inside the head tag.
```
<html>
	<head>
		<link
			rel=“stylesheet” # relationship
			href=“./style.css” # file location
		/> # self closing tag
	</head>
</html>
```