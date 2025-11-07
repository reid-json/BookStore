from AA_StrategyPattern_PaymentInfo.PaymentTypes import (
    CreditCardStrategy, DebitCardStrategy, PayPalStrategy
)

def get_payment_strategy(method):
    if method == 'credit_card':
        return CreditCardStrategy()
    elif method == 'debit_card':
        return DebitCardStrategy()
    elif method == 'paypal':
        return PayPalStrategy()
    else:
        raise ValueError(f"Unsupported payment method: {method}")