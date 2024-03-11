import os

from dotenv import find_dotenv, load_dotenv

(function) def find_dotenv(
    filename: str = '.env',
    raise_error_if_not_found: bool = False,
    usecwd: bool = False
) -> str

dotenv_path = find_dotenv()
dotenv_path

load_dotenv(dotenv_path)