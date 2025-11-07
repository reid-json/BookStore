from AA_StatePattern_Orders.OrderStates import (
    PendingState, ProcessingState, ShippedState, DeliveredState, CancelledState
)

def get_order_state(status):
    if status == 'pending':
        return PendingState()
    elif status == 'processing':
        return ProcessingState()
    elif status == 'shipped':
        return ShippedState()
    elif status == 'delivered':
        return DeliveredState()
    elif status == 'cancelled':
        return CancelledState()
    else:
        raise ValueError(f"Unknown order status: {status}")