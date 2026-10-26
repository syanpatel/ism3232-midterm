# Terminal Record: Cloudstep Software

## 1. Building the project

```
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
git init
git branch -M main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
mkdir tests
touch business_rules.py main.py commands.md README.md tests/__init__.py tests/test_business_rules.py
printf '.venv/\n__pycache__/\n' > .gitignore
pip freeze > requirements.txt
git remote add origin https://github.com/syanpatel/ism3232-midterm.git
```

## 2. The virtual environment

```
which python3
```

```
/home/syan/ism3232-midterm/.venv/bin/python3
```

The path goes through the .venv folder inside my project, which shows the virtual environment is active.

## 3. The project structure

```
tree -L 2
```

```
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```

The __pycache__ folder is on my computer but not in my GitHub repository, because .gitignore tells git to leave it out.

## 4. Every function/test

```
rg 'def '
```

```
business_rules.py
16:def calculate_license_cost(seat_price: float, seats: int) -> float:
21:def get_seat_discount(seats: int, education: bool = False) -> float:
30:def calculate_license_total(
42:def needs_contract_review(total: float) -> bool:
47:def gets_trainer(seats: int, total: float) -> bool:
52:def total_licensed(orders: list) -> float:
62:def largest_license(orders: list) -> str:
76:def format_license_line(

tests/test_business_rules.py
13:def test_license_cost_is_price_times_seats():
17:def test_no_discount_below_ten_seats():
21:def test_seven_percent_at_ten_seats():
25:def test_seven_percent_at_forty_nine_seats():
29:def test_education_gets_sixteen_percent_at_fifty_seats():
33:def test_non_education_gets_seven_percent_at_fifty_seats():
37:def test_education_flag_changes_total():
44:def test_onboarding_fee_added_below_four_hundred():
48:def test_onboarding_fee_added_at_exactly_four_hundred():
52:def test_onboarding_fee_not_added_above_four_hundred():
56:def test_contract_review_not_needed_at_five_thousand():
60:def test_contract_review_needed_above_five_thousand():
64:def test_trainer_at_twenty_five_seats():
68:def test_no_trainer_at_twenty_four_seats():
72:def test_no_trainer_at_three_thousand_total():
76:def test_trainer_above_three_thousand_total():
80:def test_total_licensed_adds_every_order():
93:def test_total_licensed_empty_list_is_zero():
97:def test_largest_license_returns_biggest_company():
110:def test_largest_license_tie_returns_first_in_list():
118:def test_largest_license_empty_list_returns_empty_string():
122:def test_format_line_with_no_flags():
127:def test_format_line_with_both_flags():
132:def test_format_line_shows_two_decimal_places():
137:def test_education_at_forty_nine_seats_still_gets_seven_percent():
141:def test_education_below_ten_seats_gets_no_discount():
145:def test_total_at_ten_seats_uses_seven_percent():
149:def test_total_licensed_applies_discounts_to_each_order():
```

business_rules.py defines 8 functions, and tests/test_business_rules.py defines 28 tests.

## 5. Which files print

```
rg -l 'print'
```

```
main.py
README.md
```

main.py is the only Python file that prints, and business_rules.py is not in the list because its functions return values instead of printing them.

## 6. The commit history

```
git log --oneline
```

```
3878590 (HEAD -> main, origin/main) Add README with rules, run steps, and AI use statement
0487055 Add more boundary tests for discounts and totals
feff47d Add main.py order report
39228b0 Add total, largest license, and format functions with test
bac255b Add contract review and trainer functions with tests
76c4ffa Add constants and licence cost, discount, and total functions
38349ec Create project skeleton with empty files and requirements
```

There were 7 commits at that point.