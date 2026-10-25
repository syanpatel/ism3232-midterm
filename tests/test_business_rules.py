from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)


def test_license_cost_is_price_times_seats():
    assert round(calculate_license_cost(40.0, 5), 2) == 200.0


def test_no_discount_below_ten_seats():
    assert get_seat_discount(9) == 0.0


def test_seven_percent_at_ten_seats():
    assert get_seat_discount(10) == 0.07


def test_seven_percent_at_forty_nine_seats():
    assert get_seat_discount(49) == 0.07


def test_education_gets_sixteen_percent_at_fifty_seats():
    assert get_seat_discount(50, education=True) == 0.16


def test_non_education_gets_seven_percent_at_fifty_seats():
    assert get_seat_discount(50, education=False) == 0.07


def test_education_flag_changes_total():
    regular = calculate_license_total(50.0, 150, education=False)
    education = calculate_license_total(50.0, 150, education=True)
    assert round(regular, 2) == 6975.0
    assert round(education, 2) == 6300.0


def test_onboarding_fee_added_below_four_hundred():
    assert round(calculate_license_total(40.0, 9), 2) == 420.0


def test_onboarding_fee_added_at_exactly_four_hundred():
    assert round(calculate_license_total(50.0, 8), 2) == 460.0


def test_onboarding_fee_not_added_above_four_hundred():
    assert round(calculate_license_total(44.5, 9), 2) == 400.5


def test_contract_review_not_needed_at_five_thousand():
    assert needs_contract_review(5000.0) is False


def test_contract_review_needed_above_five_thousand():
    assert needs_contract_review(5000.01) is True


def test_trainer_at_twenty_five_seats():
    assert gets_trainer(25, 100.0) is True


def test_no_trainer_at_twenty_four_seats():
    assert gets_trainer(24, 100.0) is False


def test_no_trainer_at_three_thousand_total():
    assert gets_trainer(5, 3000.0) is False


def test_trainer_above_three_thousand_total():
    assert gets_trainer(5, 3000.01) is True


def test_total_licensed_adds_every_order():
    orders = [
        {"company": "Pine Books", "seat_price": 40.0, "seats": 5, "education": False},
        {
            "company": "Quarry School",
            "seat_price": 35.0,
            "seats": 12,
            "education": True,
        },
    ]
    assert round(total_licensed(orders), 2) == 710.6


def test_total_licensed_empty_list_is_zero():
    assert total_licensed([]) == 0.0


def test_largest_license_returns_biggest_company():
    orders = [
        {"company": "Pine Books", "seat_price": 40.0, "seats": 5, "education": False},
        {
            "company": "Redwood Cargo",
            "seat_price": 45.0,
            "seats": 60,
            "education": False,
        },
    ]
    assert largest_license(orders) == "Redwood Cargo"


def test_largest_license_tie_returns_first_in_list():
    orders = [
        {"company": "First", "seat_price": 40.0, "seats": 5, "education": False},
        {"company": "Second", "seat_price": 40.0, "seats": 5, "education": False},
    ]
    assert largest_license(orders) == "First"


def test_largest_license_empty_list_returns_empty_string():
    assert largest_license([]) == ""


def test_format_line_with_no_flags():
    line = format_license_line("Pine Books", 260.0, False, False)
    assert line == "Pine Books: $260.00 | contract review: no | trainer: no"


def test_format_line_with_both_flags():
    line = format_license_line("Summit College", 6300.0, True, True)
    assert line == "Summit College: $6300.00 | contract review: yes | trainer: yes"


def test_format_line_shows_two_decimal_places():
    line = format_license_line("Test Co", 5.5, False, True)
    assert line == "Test Co: $5.50 | contract review: no | trainer: yes"


def test_education_at_forty_nine_seats_still_gets_seven_percent():
    assert get_seat_discount(49, education=True) == 0.07


def test_education_below_ten_seats_gets_no_discount():
    assert get_seat_discount(9, education=True) == 0.0


def test_total_at_ten_seats_uses_seven_percent():
    assert round(calculate_license_total(100.0, 10), 2) == 930.0


def test_total_licensed_applies_discounts_to_each_order():
    orders = [
        {"company": "Big Co", "seat_price": 100.0, "seats": 10, "education": False},
        {"company": "Small Co", "seat_price": 40.0, "seats": 5, "education": False},
    ]
    assert round(total_licensed(orders), 2) == 1190.0
