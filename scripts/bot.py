import os

from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyCompleter, WordCompleter

# list all python file names in current folder, except this one
files = os.listdir(os.path.dirname(__file__))
pys = []
for file in files:
    if file.endswith(".py") and file != os.path.basename(__file__):
        pys.append(file)


def get_input(
    user_prompt: str,
    valid_inputs: list,
) -> str:
    """Until user give valid input, or return default input if allow_empty is True and user input is empty."""
    completer = FuzzyCompleter(WordCompleter(valid_inputs))  # list completion

    while True:
        user_input: str = prompt(user_prompt, completer=completer).strip()
        if user_input not in valid_inputs:
            continue
        else:
            return user_input


while True:
    for py in pys:
        print(py)
    aim = get_input("chose a script name: ", pys)
    os.system(f"python {os.path.dirname(__file__)}/{aim}")
