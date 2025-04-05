import random
from datetime import datetime, timedelta
from typing import List, Dict

# Categories for realistic transactions
INCOME_CATEGORIES = {
    "Salary": (25000, 80000),
    "Freelance": (2000, 15000),
    "Dividends": (500, 5000),
    "Bonus": (1000, 10000)
}

EXPENSE_CATEGORIES = {
    "Groceries": (200, 5000),
    "Rent": (8000, 20000),
    "Dining": (150, 3000),
    "Transport": (100, 2500),
    "Entertainment": (300, 6000),
    "Utilities": (1000, 5000)
}

class Transaction:
    def __init__(self, amount: float, description: str, category: str, transaction_type: str):
        self.amount = amount
        self.description = description
        self.category = category
        self.type = transaction_type  # 'credit' or 'debit'
        self.date = self._random_date()
    
    def _random_date(self) -> str:
        start_date = datetime.now() - timedelta(days=90)
        random_date = start_date + timedelta(days=random.randint(0, 90))
        return random_date.strftime("%d-%b-%Y")
    
    def to_dict(self) -> Dict:
        return {
            "date": self.date,
            "amount": f"₹{self.amount:,.2f}",
            "description": self.description,
            "category": self.category,
            "type": self.type.upper()
        }

def generate_transactions(user_id: str, count: int = 30) -> List[Dict]:
    transactions = []
    for _ in range(count):
        if random.random() > 0.3:  # 70% chance of expense
            category = random.choice(list(EXPENSE_CATEGORIES.keys()))
            min_val, max_val = EXPENSE_CATEGORIES[category]
            amount = random.uniform(min_val, max_val)
            transaction_type = "debit"
        else:  # 30% chance of income
            category = random.choice(list(INCOME_CATEGORIES.keys()))
            min_val, max_val = INCOME_CATEGORIES[category]
            amount = random.uniform(min_val, max_val)
            transaction_type = "credit"
        
        description = f"{category}: {generate_description(category)}"
        transactions.append(
            Transaction(amount, description, category, transaction_type).to_dict()
        )
    return sorted(transactions, key=lambda x: datetime.strptime(x["date"], "%d-%b-%Y"))

def generate_description(category: str) -> str:
    descriptors = {
        "Salary": ["Monthly salary", "Performance bonus"],
        "Freelance": ["Web design project", "Consulting work"],
        "Groceries": ["Big Bazaar", "D-Mart", "Vegetables"],
        "Rent": ["Apartment rent", "PG payment"],
        "Dining": ["Zomato order", "Restaurant bill"]
    }
    return random.choice(descriptors.get(category, [f"Payment for {category}"]))
