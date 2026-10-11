# HashForge

HashForge is a small terminal-based hash generator written in Python. It allows the user to enter any text and generate a digest using common hashing algorithms such as MD5, SHA1, SHA256, and SHA512.

The project is designed to be simple, readable, and easy to extend. It also has a cyber-themed ASCII header and a custom watermark to give the tool a distinctive look.

## Features

- MD5 generation
- SHA1 generation
- SHA256 generation
- SHA512 generation
- interactive terminal menu
- validation for invalid options
- retry flow for repeated use
- professional structure with small helper functions

## How it works

1. The script starts in the main block:
   `if __name__ == "__main__": generate_hash()`
2. `generate_hash()` prints the ASCII banner and watermark.
3. The user is prompted to choose a hash algorithm.
4. The script validates the input and only accepts values from 1 to 4.
5. The user enters the text to hash.
6. The selected algorithm is applied with Python's `hashlib` module.
7. The digest is printed in the terminal.
8. The program asks whether the user wants to generate another hash.

## Supported algorithms

- MD5
- SHA1
- SHA256
- SHA512

## Example

```bash
python gerador_de_hashes.py
```

Then choose one of these options:

```text
1) MD5
2) SHA1
3) SHA256
4) SHA512
```

Example output:

```text
Hash SHA256 for the text: "teste"
Result / Resultado: 46070d4bf934fb0d4b06d9e2c46e346944e322444900a435d7d9a95e6d7435f5
```

## File structure

- `gerador_de_hashes.py` — main script
- `README.md` — project documentation

## Notes

This tool is intended for educational and development use. Hashing is a one-way process, so the generated digests should not be treated as reversible encryption.

## Portuguese summary

Este projeto e um gerador de hash em terminal, escrito em Python. Ele recebe um texto digitado pelo usuario e gera o digest com algoritmos populares como MD5, SHA1, SHA256 e SHA512. A estrutura foi organizada em funcoes pequenas para facilitar a leitura, validaao e manutencao do codigo.

The main logic is concentrated in a few functions:

- `print_header()` — prints the banner and watermark
- `get_hash_algorithms()` — maps the numeric choice to a hash algorithm
- `read_hash_type()` — validates the user's choice
- `ask_retry()` — asks if the user wants to continue
- `generate_hash()` — orchestrates everything and prints the result

This approach keeps the code clean and makes it easier to expand with new algorithms or UI improvements later.
