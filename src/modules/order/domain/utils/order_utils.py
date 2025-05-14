from modules.order.domain.entities.order_entity import OrderProduct


class OrderUtils:
    @staticmethod
    def calculate_order_total_price(products: list[OrderProduct]) -> float:
        return sum(product.price * product.quantity for product in products)

    @staticmethod
    def calculate_order_total_discounts(products: list[OrderProduct]) -> float:
        return sum(product.total_discount for product in products)
