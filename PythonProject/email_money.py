from datetime import datetime


class Email:

    def __init__(self, sender, recipient, subject, body, date=None):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nDate: {self.date}\nSubject: {self.subject}\n - {self.body} -"

    def __len__(self):
        return len(self.body)

    def __contains__(self, text):
        return text.lower() in self.body.lower() or text.lower() in self.subject.lower()


class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        return NotImplemented

    def __str__(self):
        return f"${self.amount}"

    def __repr__(self):
        return f"Money({self.amount})"


if __name__ == "__main__":
    e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
    e2 = Email("hello@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))

    print(e1)
    print(e2)
    print(f"Length: {len(e1)}")
    print(f"Length: {len(e2)}")
    print(f"Has text: {'10am' in e1}")
    print(f"Is empty: {len(e2) == 0}")

    print("\n")

    money1 = Money(100)
    money2 = Money(50)
    print(money1 + money2)
    print(money1 - money2)
    print(money1 + money1)
    print(money2 - money1)
