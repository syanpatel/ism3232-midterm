# ISM3232 Midterm: Cloudstep Software

- **Name:** Syan Patel
- **Version:** 1.0
- **Date:** October 25, 2026

## What This Program Does

This program applies Cloudstep Software's pricing rules to a list of customer orders. For each order it works out the license total, whether the order needs a contract review, and whether it gets a dedicated trainer. It then prints a report with one line per order and a summary at the end.

## Business Rules

1. The license cost is the price per seat multiplied by the number of seats.
2. Orders under 10 seats dont get a discount, 10 to 49 seats get 7%, and 50 or more seats get 16%.
3. The 16% discount is only for education customers. Any other order of 50 seats or more gets 7%.
4. A $60 onboarding fee is added when the discounted cost is $400 or less.
5. A license total over $5,000 needs a contract review.
6. An order is dedicated to a trainer when it has 25 or more seats or its license total is over $3,000.

## How to Run


git clone https://github.com/syanpatel/ism3232-midterm.git
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py


## How to Test

ruff format .
ruff check .
pytest -v


I wrote 28 tests, and all of them passed.

## Files in This Repository

- `business_rules.py`: the eight functions and named constants that apply the six business rules.
- `main.py`: the order list and the code that prints the report.
- `commands.md`: a record of the terminal commands I used to build and check the project.
- `README.md`: this file, which explains how to run and test the project.
- `requirements.txt`: the Python packages the project needs, made using `pip freeze`.
- `.gitignore`: keeps `.venv/` and `__pycache__/` out of the repository.
- `tests/__init__.py`: an empty file that makes `tests` a Python package.
- `tests/test_business_rules.py`: the pytest tests for the eight functions.

## AI Use Statement

I did not use any AI on this exam.