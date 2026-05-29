# xml-sql-compiler-demo

A compiler demo built for an Automata Theory course. It parses a domain-specific XML schema and translates it into SQL `INSERT` statements using [PLY](https://github.com/dabeaz/ply) (Python Lex-Yacc).

The lexer tokenizes XML tags and values; the parser applies a context-free grammar to produce `INSERT` statements for `cars` and `services` tables. The input schema is based on a car rental dataset.

## Requirements

- Python 3

## Setup

1. Create a virtual environment:
   ```sh
   python -m venv .venv
   ```

2. Activate it:
   ```sh
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

```sh
python yacc.py
```

Output is written to `output.sql`.
