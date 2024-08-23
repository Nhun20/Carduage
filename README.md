# Carduage
Programming language with the logic of a deck of cards... Written in python. To run the code, write: python interpreter.py (in the terminal)
    
    Available Commands:
    -------------------
    move_top_to_bottom n
        - Move the top `n` cards to the bottom of the deck.
        - `n` can be a number, an expression like `count-2`, or a variable.
        - Example: move_top_to_bottom 3
        - Example: move_top_to_bottom count-2
        - Example: move_top_to_bottom x

    flip_deck
        - Flip the entire deck (reverse the order of cards).
        - Example: flip_deck

    cut_deck n
        - Cut the deck at position `n` and create a new deck with the top `n` cards.
        - `n` can be a number, an expression like `count/2`, or a variable.
        - Example: cut_deck 5
        - Example: cut_deck count/2
        - Example: cut_deck x

    peek_top n
        - View the top `n` cards without modifying the deck.
        - `n` can be a number, an expression like `count-1`, or a variable.
        - Example: peek_top 2
        - Example: peek_top count-1
        - Example: peek_top x

    take_top n
        - Remove and store the top `n` cards from the deck.
        - The top card of the original deck will be at the bottom of the removed cards.
        - `n` can be a number, an expression like `count-3`, or a variable.
        - Example: take_top 4
        - Example: take_top count-3
        - Example: take_top x

    return_top
        - Place the last removed cards back on top of the deck in reverse order.
        - Example: return_top

    count_cards
        - Return the number of cards currently in the deck.
        - Example: count_cards

    shuffle
        - Shuffle the deck randomly.
        - Example: shuffle

    insert_deck deck pos
        - Insert a new deck into the current deck at position `pos`.
        - The new deck should be a comma-separated list of cards.
        - `pos` can be a number, an expression like `count/2`, or a variable.
        - Example: insert_deck 2S,3H,4D 10
        - Example: insert_deck 2S,3H,4D count/2
        - Example: insert_deck 2S,3H,4D x

    print_card_name index
        - Print the name of the card at position `index` in the deck.
        - `index` can be a number, an expression like `count-1`, or a variable.
        - Example: print_card_name 2
        - Example: print_card_name count-1
        - Example: print_card_name x

    print_card_number index
        - Print the number of the card at position `index` in the deck.
        - `index` can be a number, an expression like `count-1`, or a variable.
        - Example: print_card_number 2
        - Example: print_card_number count-1
        - Example: print_card_number x

    set_card_value card value
        - Assign a custom value to a specific card.
        - If the value exceeds 55, the interpreter will exit with an error.
        - Example: set_card_value J2 22

    Variables and Assignment:
    -------------------------
    - Assign a value to a variable using `var = expression`.
    - The expression can be a number, an expression like `count-2`, or another variable.
    - The sum of all variable values cannot exceed 55.
    - Example: var x = count-2
    - Example: var y = x

    Conditionals:
    -------------
    - Perform actions conditionally using `if condition then command`.
    - Supports simple comparisons: `==`, `!=`, `<`, `>`, `<=`, `>=`.
    - Supports addition, but if the result exceeds 55 at any point, the interpreter will exit.
    - Example: if count + 10 > 26 then shuffle

    Referring to the Number of Cards in the Deck:
    ---------------------------------------------
    - You can use the keyword 'count' to refer to the number of cards in the deck.
    - Example: move_top_to_bottom count-2 -> Move the top (count-2) cards to the bottom.

    Command Chaining:
    -----------------
    - You can chain multiple commands together using '&&'.
    - The commands will be executed sequentially.
    - Example: move_top_to_bottom 3 && flip_deck && count_cards

    help
        - Display this help message.
        - Example: help

    exit
        - Exit the interpreter.
        - Example: exit
