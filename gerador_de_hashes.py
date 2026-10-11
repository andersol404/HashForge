import hashlib
from typing import Callable

# Hash generator / Gerador de hash
# Main interface and messages are in English, with a few Portuguese labels for clarity.
# A interface principal e as mensagens estao em ingles, com algumas legendas em portugues para facilitar.

ASCII_ART = r'''
   ___  _   _  ___  __  __  ___   ___  _   _    ___  ___   __  __
  / __|| | | || _ )|  \/  |/ _ \ / __|| | | |  / __|| __| |  \/  |
  \__ \| |_| || _ \| |\/| | (_) |\__ \| |_| | | (__ | _|  | |\/| |
  |___/ \___/ |___/|_|  |_|\___/ |___/ \___/   \___||___| |_|  |_|

    by: 0xander // hash-core
'''

WATERMARK = "0xander // hash-core // code in stealth mode"


def print_footer() -> None:
    print("=" * 78)
    print(WATERMARK)
    print("=" * 78)


def get_hash_algorithms() -> dict[int, tuple[str, Callable[[str], str]]]:
    return {
        1: ("MD5", lambda value: hashlib.md5(value.encode("UTF-8")).hexdigest()),
        2: ("SHA1", lambda value: hashlib.sha1(value.encode("UTF-8")).hexdigest()),
        3: ("SHA256", lambda value: hashlib.sha256(value.encode("UTF-8")).hexdigest()),
        4: ("SHA512", lambda value: hashlib.sha512(value.encode("UTF-8")).hexdigest()),
    }


def read_hash_type() -> int:
    while True:
        try:
            choice = int(
                input(
                    """Available hash types / Tipos de hash disponiveis:
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
Select the hash type / Selecione o tipo de hash: """
                )
            )
            if choice in get_hash_algorithms():
                return choice
            raise ValueError
        except ValueError:
            print("x" * 78)
            print("Invalid option. Please enter a number from 1 to 4. / Opcao invalida. Digite um numero de 1 a 4.")
            print("x" * 78)


def ask_retry() -> bool:
    answer = input("Would you like to try again? / Gostaria de tentar novamente? [Y/N]: ").strip().lower()
    return answer in {"yes", "y", "sim", "s"}


def generate_hash() -> None:
    """Generate a hash from user input / Gera um hash a partir de um texto digitado."""

    while True:
        hash_type = read_hash_type()
        text_to_hash = input("Enter the text to hash / Digite o texto para gerar o hash: ")

        algorithm_name, hash_function = get_hash_algorithms()[hash_type]
        digest = hash_function(text_to_hash)

        print("-" * 78)
        print(f"Hash {algorithm_name} for the text: \"{text_to_hash}\" / Hash {algorithm_name} para o texto: \"{text_to_hash}\"")
        print(f"Result / Resultado: {digest}")
        print("-" * 78)
        print_footer()

        if not ask_retry():
            print("OK! Closing the generator. / Ok! Encerrando o gerador.")
            return



if __name__ == "__main__":
    generate_hash()
