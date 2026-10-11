"""Functions to manage a users shopping cart items."""


def add_item(current_cart:dict, items_to_add:list | tuple):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    user_cart = dict.fromkeys(notes, 1)
    return user_cart


def update_recipes(ideas:dict, recipe_updates:iter):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas |= recipe_updates
    return ideas


def sort_entries(cart:dict):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart:dict, aisle_mapping:dict):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item, count in sorted(cart.items(), reverse=True):
        fulfillment_cart[item] = [count] + aisle_mapping[item]
    return fulfillment_cart



def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for items, inventory in fulfillment_cart.items():
        required_items = inventory[0]
        items_in_store = store_inventory[items][0]
        remaining_inventory = items_in_store - required_items
        if remaining_inventory == 0:
            store_inventory[items][0] = 'Out of Stock'
        else:
            store_inventory[items][0] = remaining_inventory
    return store_inventory
