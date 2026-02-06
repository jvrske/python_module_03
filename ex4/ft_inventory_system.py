import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = {}
    args = sys.argv[1:]

    for i in args:
        name, qty = i.split(":")
        inventory[name] = int(qty)

    total_items = 0
    for item in inventory.values():
        total_items += item
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}\n")

    print("=== Current Inventory ===")
    for name, qty in inventory.items():
        percent = (qty / total_items) * 100
        if qty > 1:
            print(f"{name}: {qty} units ({percent:.1f}%)")
        else:
            print(f"{name}: {qty} unit ({percent:.1f}%)")

    print("\n=== Inventory Statistics ===")
    most_abundant = -1
    name_abundant = None
    for name, qty in inventory.items():
        if qty > most_abundant:
            most_abundant = qty
            name_abundant = name
    print(f"Most abundant: {name_abundant} ({most_abundant} units)")

    least_abundant = 9999
    least_name = None
    for name, qty in inventory.items():
        if qty < least_abundant:
            least_abundant = qty
            least_name = name
    print(f"Least abundant: {least_name} ({least_abundant} unit)")

    print("\n=== Item Categories ===")
    moderate = {}
    scarce = {}
    for item in inventory.items():
        key, value = item
        if value <= 3:
            scarce.update({key: value})
        else:
            moderate.update({key: value})
    print(f"Moderate: {moderate}")        
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock = []
    for item in inventory.items():
        key, value = item
        if value < 2:
            restock.append(key)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    dict_keys = []
    dict_values = []
    for item in inventory.items():
        key, value = item
        dict_keys.append(key)
        dict_values.append(value)
    print(f"Dictionary keys: {dict_keys}")
    print(f"Dictionary values: {dict_values}")
    tru = inventory.get("sword")
    if tru:
        exist = True
    else:
        exist = False
    print(f"Sample lookup - 'sword' in inventory: {exist}")