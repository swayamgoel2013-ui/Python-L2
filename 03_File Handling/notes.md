- Say this your table

    | Name    | Age | Marks|
    |---------|-----|------|
    | Swayam  |  13 |  67  |
    | Ebad    |  25 |  91  |
    | Prakash |  30 |  85  |

- This is how you store this table in row major format

```Python
row_major = [
    {'Name': 'Swayam',  'Age': 13,  'Marks': 67},
    {'Name': 'Ebad',    'Age': 25,  'Marks': 91},
    {'Name': 'Prakash', 'Age': 30,  'Marks': 85},
]
```

- This is how you store this table in column major format

```Python
col_major = {
    'Name':  ['Swayam', 'Ebad', 'Prakash'],
    'Age':   [13, 25, 30],
    'Marks': [67, 91, 85],
}
```
