![Build](https://github.com/AmilaIndika789/Password_Generator/actions/workflows/build_and_test.yml/badge.svg?branch=main&event=push)
[![codecov](https://codecov.io/gh/AmilaIndika789/Password_Generator/graph/badge.svg?token=BMS7KABWU5)](https://codecov.io/gh/AmilaIndika789/Password_Generator)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b565d7fce9694ab8b5ecc2cb6e41d753)](https://app.codacy.com/gh/AmilaIndika789/Password_Generator/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

# Password Generator

A password generator implemented using Python.

## Instructions

1. Install required dependencies.

   ~~~zsh
   pip install -r requirements.txt
   ~~~
   
2. Run the following command from the root directory.

   ~~~zsh
   python -m src.pkg.password_generator src/pkg/password_generator.py
   ~~~
   
3. [Optional] Run unit tests with coverage and pytest

   ~~~zsh
   coverage run --source src.pkg -m pytest -vv tests && coverage report --show-missing
   ~~~
