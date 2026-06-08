from faker import Faker

fake = Faker()


def generate_customer() -> dict:
    """Returns a dict with random customer data for checkout."""
    return {
        "first_name": fake.first_name(),
        "last_name":  fake.last_name(),
        "zip_code":   fake.postcode(),
    }


def parse_price(price_str: str) -> float:
    """Converts '$12.99' → 12.99"""
    return float(price_str.replace("$", "").strip())
