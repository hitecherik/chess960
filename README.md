# Chess 960 generator

This is just a quick Python web app I built in Flask to generate multiple [Chess960](https://en.wikipedia.org/wiki/Chess960 "Fischer Random Chess") positions.

## Usage

1. Run `server.py <PORT>` in Python 3 with Flask installed (if the port is unspecified, it defaults to `5000`)
2. Go to the specified path in your web browser
3. Append a number to the path. E.g.: if the app is hosted at `localhost:5000` to generate 10 positions you go to `localhost:5000/10`.

### In the terminal

You can run this in the terminal as well, providing you have Python 3 installed (although it may work in Python 2 - haven't tested it).

Run this in your terminal: `python chess960.py [number of positions]` where the default number of positions is 1.

## Licence

Copyright (c) Alexander Nielsen 2016-17. Licenced under a [CC BY 4.0 licence](https://creativecommons.org/licenses/by/4.0/ "Creative Commons 4.0 International Licence").
