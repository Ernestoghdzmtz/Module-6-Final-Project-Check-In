from datetime import datetime
from item import Item

class Transaction:
    def __init__(self, transaction_id, item_sku, quantity, transaction_type):
        # Validación de los datos
        if not isinstance(transaction_id, str) or not transaction_id:
            raise ValueError("El ID de la transacción debe ser una cadena no vacía.")
        if not isinstance(item_sku, str) or not item_sku:
            raise ValueError("El SKU del artículo debe ser una cadena no vacía.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("La cantidad debe ser un número entero mayor a cero.")
        if transaction_type not in ['sale', 'restock']:
            raise ValueError("El tipo de transacción debe ser 'sale' o 'restock'.")
        
        self.transaction_id = transaction_id
        self.item_sku = item_sku
        self.quantity = quantity
        self.transaction_type = transaction_type
        self.timestamp = datetime.now()

    def record_transaction(self):
        """Registra una transacción (esto puede agregarla a un registro de transacciones)."""
        # Esto es solo un ejemplo. Podrías agregar la transacción a un log o base de datos.
        return f"Transaction Recorded: {self.transaction_id} | Item SKU: {self.item_sku} | Quantity: {self.quantity} | Type: {self.transaction_type} | Date: {self.timestamp}"

    def calculate_total(self, item_info):
        """
        Calculate the total value of the transaction.
        item_info: An instance of the Item class.
        Returns: Total value as a float.
        """
        if not isinstance(item_info, Item):
            raise ValueError("Invalid item_info. Expected an instance of the Item class.")
        return self.quantity * item_info.price
        
        item_info = item.get_item_info()
        if self.transaction_type == 'sale':
            return self.quantity * item_info['price']
        elif self.transaction_type == 'restock':
            return 0  # No calculamos el valor para un restock; solo actualizamos el stock.

    def __str__(self):
        """Método para mostrar una representación legible de la transacción."""
        return f"Transaction ID: {self.transaction_id}, Item SKU: {self.item_sku}, Quantity: {self.quantity}, Type: {self.transaction_type}, Date: {self.timestamp}"
