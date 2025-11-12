from appOrders.models import OrdersModel
from AA_StatePattern_Orders.StateInterface import OrderStates

class PendingState(OrderStates):
    def create(self, user, order_id, isbn, quantity):
        OrdersModel.objects.create(
            user=user,
            order_id=order_id,
            isbn=isbn,
            quantity=quantity,
            status='pending'
        )

    def advance(self, order):
        order.status = 'processing'
        order.save()

    def cancel(self, order):
        order.status = 'cancelled'
        order.save()

class ProcessingState(OrderStates):
    def advance(self, order):
        order.status = 'shipped'
        order.save()

    def cancel(self, order):
        order.status = 'cancelled'
        order.save()

class ShippedState(OrderStates):
    def advance(self, order):
        order.status = 'delivered'
        order.save()

    def cancel(self, order):
        raise Exception("Cannot cancel a shipped order")

class DeliveredState(OrderStates):
    def advance(self, order):
        raise Exception("Order already delivered")

    def cancel(self, order):
        raise Exception("Cannot cancel a delivered order")

class CancelledState(OrderStates):
    def advance(self, order):
        raise Exception("Cannot advance a cancelled order")

    def cancel(self, order):
        raise Exception("Order already cancelled")