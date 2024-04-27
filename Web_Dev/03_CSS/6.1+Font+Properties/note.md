# Font Propeties
## Font Size
Property Name: font-size

### Values
#### Static
1. pixel size:
    - px
    - 1 pixel = 1/96 inch = 0.26 mm * 0.26 mm
    ```
    font-size: 20px
    ```

2. point size
    - pt
    - 1pt = 1/72 inch = 0.35 mm * 0.35mm
    ```
    font-size: 12pt
    ```

3. named font size
    - xx-large, large, …

#### Relatvie
1. em
    - 1em = 100% of the parent size
    ```
    <body> # set to 20px
	<h1>Hello</h1> # set to 1em, it will be 20px
    </body>
    ```

2. rem
    - 1rem = 100% of the root size
    - the root size is the size the outest tag’s size, often the 'html' tag’s size.
    - a more consistent way of changing than em

## Font Weight
Property Name: font-weight

### Values
#### Directly
```
font-weight: bold
font-weight: normal
```

#### Number: 100-900 (lighter-bolder)

## Font Family
Property Name: font-family
```
font-family: typeface, backup generic font type
```

### Normal
e.g.
```
font-family: Helvetica, sans-serif # sans-serif: font with coner rectangle
```


### Font have many words
Use the quotation mark
e.g.
```
font-family: “Times New Roman”, serif
```

#### [More Free Fonts](https://fonts.google.com/)
1. Use Embed code - <link> copy to the starting file.
2. Use the CSS Class File as described

## Text Align
Property Name: text-align
### Values
```
text-align: center/left/right
```