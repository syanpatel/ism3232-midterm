SMALL_ORDER_LIMIT = 10
LARGE_ORDER_LIMIT = 50
NO_DISCOUNT = 0.0
MEDIUM_DISCOUNT = 0.07
EDUCATION_DISCOUNT = 0.16

ONBOARDING_FEE = 60.0
ONBOARDING_FEE_LIMIT = 400.0

CONTRACT_REVIEW_LIMIT = 5000.0

TRAINER_SEATS_LIMIT = 25
TRAINER_TOTAL_LIMIT = 3000.0


def calculate_license_cost(seat_price: float, seats: int) -> float:
    """Return the license cost before any discount."""
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    """Return the discount rate as a decimal for the seat count."""
    if seats >= LARGE_ORDER_LIMIT and education:
        return EDUCATION_DISCOUNT
    if seats >= SMALL_ORDER_LIMIT:
        return MEDIUM_DISCOUNT
    return NO_DISCOUNT


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    """Return the discounted license cost plus the onboarding fee if it applies."""
    cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    discounted = cost * (1 - discount)
    if discounted <= ONBOARDING_FEE_LIMIT:
        discounted += ONBOARDING_FEE
    return discounted


def needs_contract_review(total: float) -> bool:
    """Return True when the license total needs a contract review."""
    return total > CONTRACT_REVIEW_LIMIT


def gets_trainer(seats: int, total: float) -> bool:
    """Return True when the order gets a dedicated trainer."""
    return seats >= TRAINER_SEATS_LIMIT or total > TRAINER_TOTAL_LIMIT


def total_licensed(orders: list) -> float:
    """Return the sum of the license totals for every order in the list."""
    grand_total = 0.0
    for order in orders:
        grand_total += calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
    return grand_total


def largest_license(orders: list) -> str:
    """Return the company with the largest license total, or an empty string."""
    largest_company = ""
    largest_total = 0.0
    for order in orders:
        total = calculate_license_total(
            order["seat_price"], order["seats"], order["education"]
        )
        if total > largest_total:
            largest_total = total
            largest_company = order["company"]
    return largest_company


def format_license_line(
    company: str, total: float, contract_review: bool, trainer: bool
) -> str:
    """Return one report line for an order."""
    review_text = "yes" if contract_review else "no"
    trainer_text = "yes" if trainer else "no"
    return (
        f"{company}: ${total:.2f} | contract review: {review_text} "
        f"| trainer: {trainer_text}"
    )
