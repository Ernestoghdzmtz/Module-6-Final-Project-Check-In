from item import Item

class Category:
    def __init__(self, category_name):
        # Validación de la categoría
        if not isinstance(category_name, str) or not category_name:
            raise ValueError("El nombre de la categoría debe ser una cadena no vacía.")
        
        self.category_name = category_name
        self.items = []

    def add_item(self, item):
        """Añade un artículo a la categoría."""
        if not isinstance(item, Item):
            raise ValueError("El artículo debe ser una instancia de la clase Item.")
        self.items.append(item)

    def remove_item(self, sku):
        """Elimina un artículo de la categoría por SKU."""
        item_to_remove = next((item for item in self.items if item.sku == sku), None)
        if item_to_remove:
            self.items.remove(item_to_remove)
        else:
            raise ValueError(f"El artículo con SKU {sku} no fue encontrado en la categoría.")

    def search_item(self, sku):
        """Busca un artículo en la categoría por SKU."""
        return next((item for item in self.items if item.sku == sku), None)

    def __str__(self):
        """Método para mostrar una representación legible de la categoría."""
        return f"Category: {self.category_name}, Items: {len(self.items)}"
