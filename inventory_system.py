"""Inventory management system module.

This module provides basic functions to manage an inventory including
adding, removing, saving, loading, and reporting stock data.
"""

import json
from datetime import datetime

# Global variable for in-memory inventory data
STOCK_DATA = {}


def add_item(item="default", qty=0, logs=None):
    """Add a specific quantity of an item to the inventory.

    Args:
        item (str): The name of the item.
        qty (int or float): Quantity to add.
        logs (list): Optional list to append log entries.
    """
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        return
    STOCK_DATA[item] = STOCK_DATA.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove a specified quantity of an item from the inventory.

    Args:
        item (str): The item name.
        qty (int or float): The quantity to remove.
    """
    try:
        STOCK_DATA[item] -= qty
        if STOCK_DATA[item] <= 0:
            del STOCK_DATA[item]
    except KeyError:
        pass


def get_qty(item):
    """Return the current quantity of a specific item.

    Args:
        item (str): The item name.

    Returns:
        int or float: The quantity available. Returns 0 if item not found.
    """
    return STOCK_DATA.get(item, 0)


def load_data(file_path="inventory.json"):
    """Load inventory data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    STOCK_DATA.clear()
    STOCK_DATA.update(data)


def save_data(file_path="inventory.json"):
    """Save current inventory data to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(STOCK_DATA, file)


def print_data():
    """Print a report of all inventory items and their quantities."""
    print("Items Report")
    for item, qty in STOCK_DATA.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items whose stock is below the given threshold.

    Args:
        threshold (int or float): The minimum quantity to consider as low.

    Returns:
        list: Items with stock lower than the threshold.
    """
    result = []
    for item, qty in STOCK_DATA.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Demonstrate basic inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # Invalid types, ignored
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
