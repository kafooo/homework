# homework

## Testing

To test excercise 1 example graph is provided:
```
testNode = specificNode("A", [
        specificNode("B", [
            specificNode("E", []),
            specificNode("F", []),
        ]),
        specificNode("C", [
            specificNode("E", []),
            specificNode("G", []),
            specificNode("H", []),
        ]),
        specificNode("D", [
            specificNode("J", []),
        ]),
    ])
```

```
python3 excercise_1/main.py
walkGraph result:
['A', 'B', 'E', 'F', 'C', 'G', 'H', 'D', 'J']

paths result:
[['A', 'B', 'E'], ['A', 'B', 'F'], ['A', 'C', 'E'], ['A', 'C', 'G'], ['A', 'C', 'H'], ['A', 'D', 'J']]
```

To test excercise 2 text file needs to be provided as argument:
```
python3 excercise_2/main.py excercise_2/sample_text.txt
Doe 22
in 15
John 14
or 13
the 11
...
```

To test excercise 3 first we need to start flask server:
```
cd excercise_3
excercise_3 % flask --app flask_server run
 * Serving Flask app 'flask_server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

then we can test returned documents. For example with curl:
```
excercise_3 % curl "127.0.0.1:5000/taggedContent?tag=fish"   
["http://127.0.0.1:5000/doc5","http://127.0.0.1:5000/doc4","http://127.0.0.1:5000/doc1","http://127.0.0.1:5000/doc3"]
```
