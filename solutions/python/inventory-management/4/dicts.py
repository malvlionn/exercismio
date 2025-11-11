"""Functions to keep track and alter inventory."""

def create_inventory(items):
    unique_items = set(items)
    countitems = {item: items.count(item) for item in unique_items}
    return countitems

def add_items(inventory, items): #di sini harus comment?
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
    for barang in inventory.keys():
        if item == barang:
            del inventory[barang]
            break
    return inventory

def list_inventory(inventory):
    jawaban = list(inventory.items())
    for index, barang in enumerate(jawaban):
        if barang[1] == 0:
            del jawaban[index]
    return jawaban