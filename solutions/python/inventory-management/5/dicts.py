"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    unique_items = set(items)
    countitems = {item: items.count(item) for item in unique_items}
    return countitems


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items = create_inventory(items)
    if len(inventory) == 0:
        return items
    for barangtambah, tambahan in inventory.items():
        if barangtambah not in items:
            items[barangtambah] = tambahan
        else:
            for barangasli in items.keys():
                if barangtambah == barangasli:
                    items[barangasli] += tambahan
                    break
    return items

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    items = create_inventory(items)
    for mauapus, jumlahapus in items.items():
        for barangasli, jumlahasli in inventory.items():
            if mauapus == barangasli:
                if jumlahasli - jumlahapus <= 0:
                    inventory[barangasli] = 0
                else:
                    inventory[barangasli] -= jumlahapus
    return inventory
    
def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    for barang in inventory.keys():
        if item == barang:
            del inventory[barang]
            break
    return inventory

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    jawaban = list(inventory.items())
    for index, barang in enumerate(jawaban):
        if barang[1] == 0:
            del jawaban[index]
    return jawaban