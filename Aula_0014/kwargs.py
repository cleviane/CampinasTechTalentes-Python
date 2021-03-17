def calculate_price(value, **kwargs):
    """
    Essa funçao irá realizar cálculos
    value: Valor
    **kwargs: tax_percentage (imposto), discount (desconto)
    """
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value


print(calculate_price(100.00))
print(calculate_price(100.00, discount=2, tax_percentage=4))
