def order_status(amount, items, is_vip):
    """
    Determine the status of an order based on amount, number of items,
    and VIP customer status.

    Parameters:
        amount (numeric): Total order amount
        items (int): Number of items in the order
        is_vip (bool): VIP customer flag

    Returns:
        str: Order status classification
    """

    if amount < 0 or items < 0:
        return "invalid"

    if is_vip and amount >= 200:
        return "vip priority"

    if not is_vip and amount < 100 and items < 3:
        return "small order"

    if not is_vip and (amount < 300 or items < 5):
        return "medium order"

    return "large order"


orders = [
    (50, 1, False),
    (250, 2, True),
    (150, 4, False),
    (400, 6, False),
    (-10, 2, True)
]

results = [order_status(amount, items, is_vip) for amount, items, is_vip in orders]
print(results)
