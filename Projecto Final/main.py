from item import Item
from category import Category
from transaction import Transaction

def main():
    # Crear algunas instancias de 'Item'
    item1 = Item("Battery", "BAT123", "Batteries", 250.0, 10)
    item2 = Item("Motor", "MOT456", "Motors", 500.0, 5)

    # Crear instancias de 'Category'
    category_batteries = Category("Batteries")
    category_motors = Category("Motors")

    # Agregar items a las categorías
    category_batteries.add_item(item1)
    category_motors.add_item(item2)

    # Mostrar categorías y sus items
    print(f"Category: {category_batteries.category_name}, Items: {len(category_batteries.items)}")
    print(f"Category: {category_motors.category_name}, Items: {len(category_motors.items)}")

    # Mostrar detalles de los items en cada categoría
    print(f"Item in battery category: {category_batteries.items[0]}")
    print(f"Item in motor category: {category_motors.items[0]}")

    # Realizar transacciones
    transaction1 = Transaction("TX1001", "BAT123", 2, "sale")
    print(transaction1.record_transaction())
    print(f"Total sale transaction value: ${transaction1.calculate_total(item1)}")

    # Actualizar stock después de la transacción
    item1.update_stock(-2)
    print(f"Updated battery stock: {item1.quantity}")

    transaction2 = Transaction("TX1002", "BAT123", 5, "restock")
    print(transaction2.record_transaction())
    item1.update_stock(5)
    print(f"Updated battery stock after restock: {item1.quantity}")

    # Mostrar los stocks finales
    print(f"Final battery stock: {item1.quantity}")
    print(f"Final motor stock: {item2.quantity}")

if __name__ == "__main__":
    main()
