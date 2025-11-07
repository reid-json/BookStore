from AA_StrategyPattern_PaymentInfo.StrategyInterface import PaymentStrategy

class CreditCardStrategy(PaymentStrategy):
    def process_payment(self, user, amount, **kwargs):
        print(f"Processing credit card payment for {user} of ${amount}")
        # Add real logic or mock here

class DebitCardStrategy(PaymentStrategy):
    def process_payment(self, user, amount, **kwargs):
        print(f"Processing debit card payment for {user} of ${amount}")

class PayPalStrategy(PaymentStrategy):
    def process_payment(self, user, amount, **kwargs):
        print(f"Processing PayPal payment for {user} of ${amount}")