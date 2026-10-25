from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    get_seat_discount,
    gets_trainer,
    needs_contract_review,
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
