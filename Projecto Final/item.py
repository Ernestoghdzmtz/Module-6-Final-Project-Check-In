class Item:
    def __init__(self, name, sku, category, price, quantity):
        # Validación de los parámetros
        if not isinstance(name, str) or not name:
            raise ValueError("El nombre del artículo debe ser una cadena no vacía.")
        if not isinstance(sku, str) or not sku:
            raise ValueError("El SKU debe ser una cadena no vacía.")
        if not isinstance(category, str) or not category:
            raise ValueError("La categoría debe ser una cadena no vacía.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("El precio debe ser un número mayor que 0.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("La cantidad debe ser un número entero no negativo.")

        self.name = name
        self.sku = sku
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_stock(self, quantity):
        """Actualiza la cantidad del artículo en inventario."""
        if not isinstance(quantity, int) or quantity == 0:
            raise ValueError("La cantidad a actualizar debe ser un número entero diferente de cero.")
        self.quantity += quantity

    def adjust_price(self, new_price):
        """Actualiza el precio del artículo."""
        if not isinstance(new_price, (int, float)) or new_price <= 0:
            raise ValueError("El nuevo precio debe ser un número mayor que 0.")
        self.price = new_price

    def get_item_info(self):
        """Devuelve la información del artículo en un formato legible."""
        return f"Item: {self.name}, SKU: {self.sku}, Category: {self.category}, Price: {self.price}, Quantity: {self.quantity}"

    def __str__(self):
        """Método para mostrar una representación legible del artículo."""
        return f"Item: {self.name}, SKU: {self.sku}, Category: {self.category}, Price: ${self.price}, Quantity: {self.quantity}"
