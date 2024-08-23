from carduage import Deck

variables = {}
MAX_SUM = 55  
removed_cards = []  
card_values = {}  

def display_help():
    help_text = """
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
        - Example: really? quick reminder you already know how to use this command because you just used it xd

    exit
        - Exit the interpreter.
        - Example: exit
    """
    print(help_text)

def evaluate_expression(expr, deck, check_sum=False):
    try:
        if "count" in expr:
            count = deck.count_cards()
            expr = expr.replace("count", str(count))
        if expr in variables:
            return variables[expr]

        result = eval(expr)
        if check_sum and isinstance(result, int):
            terms = [int(term) for term in expr.split('+')]
            for term in terms:
                if term > MAX_SUM:
                    print(f"Error: A term {term} exceeds the maximum allowed value of {MAX_SUM}. Exiting.")
                    exit(1)
            if result > MAX_SUM:
                print(f"Error: The sum {result} exceeds the maximum allowed value of {MAX_SUM}. Exiting.")
                exit(1)
        return result
    except Exception as e:
        print(f"Error evaluating expression '{expr}': {e}")
        return None

def check_variable_sum():
    total_sum = sum(variables.values())
    if total_sum > MAX_SUM:
        print(f"Error: The sum of all variable values cannot exceed {MAX_SUM}. Current sum is {total_sum}. Exiting.")
        exit(1)

def set_card_value(card_name, value):
    if value > 55:
        print(f"Error: The assigned value for {card_name} cannot exceed 55. Exiting.")
        exit(1)
    card_values[card_name] = value
    print(f"Set value of {card_name} to {value}")

def print_card_name(deck, index):
    try:
        card = deck.get_card(index)
        print("Card name:", card.name)
    except Exception as e:
        print(f"Error printing card name at index {index}: {e}")

def print_card_number(deck, index):
    try:
        card = deck.get_card(index)
        print("Card number:", card.number)
    except Exception as e:
        print(f"Error printing card number at index {index}: {e}")

def interpret_command(deck, command):
    global variables, removed_cards
    command = command.strip()
    if not command:
        return

    tokens = command.split()

    try:
        if tokens[0] == "var":
            var_name = tokens[1]
            if tokens[2] == '=':
                value = evaluate_expression(" ".join(tokens[3:]), deck)
                if value is not None:
                    variables[var_name] = value
                    check_variable_sum()
                    print(f"Variable {var_name} set to {value}")
        elif tokens[0] == "move_top_to_bottom":
            n = evaluate_expression(tokens[1], deck)
            if n is not None:
                deck.move_top_to_bottom(n)
        elif tokens[0] == "flip_deck":
            deck.flip_deck()
        elif tokens[0] == "cut_deck":
            n = evaluate_expression(tokens[1], deck)
            if n is not None:
                new_deck = deck.cut_deck(n)
                print("New deck created:", ", ".join(new_deck))
        elif tokens[0] == "peek_top":
            n = evaluate_expression(tokens[1], deck)
            if n is not None:
                print("Top cards:", ", ".join(deck.peek_top(n)))
        elif tokens[0] == "take_top":
            n = evaluate_expression(tokens[1], deck)
            if n is not None:
                removed_cards = deck.take_top(n)[::-1]
                print("Taken cards:", ", ".join(removed_cards))
        elif tokens[0] == "return_top":
            if removed_cards:
                deck.insert_deck(removed_cards, 0)
                removed_cards = []
                print("Returned cards to top of the deck.")
            else:
                print("No cards to return.")
        elif tokens[0] == "count_cards":
            print("Number of cards in deck:", deck.count_cards())
        elif tokens[0] == "shuffle":
            deck.shuffle()
        elif tokens[0] == "insert_deck":
            new_deck_str = tokens[1].split(",")
            pos = evaluate_expression(tokens[2], deck)
            if pos is not None:
                deck.insert_deck(new_deck_str, pos)
        elif tokens[0] == "set_card_value":
            card_name = tokens[1]
            value = evaluate_expression(tokens[2], deck)
            if value is not None:
                set_card_value(card_name, value)
        elif tokens[0] == "print_card_name":
            index = evaluate_expression(tokens[1], deck)
            if index is not None:
                print_card_name(deck, index)
        elif tokens[0] == "print_card_number":
            index = evaluate_expression(tokens[1], deck)
            if index is not None:
                print_card_number(deck, index)
        elif tokens[0] == "if":
            condition = " ".join(tokens[1:tokens.index('then')])
            if evaluate_expression(condition, deck, check_sum=True):
                command_to_run = " ".join(tokens[tokens.index('then') + 1:])
                interpret_command(deck, command_to_run)
        elif tokens[0] == "help":
            display_help()
        else:
            print("Unknown command! Type 'help' to see a list of available commands.")
    except Exception as e:
        print(f"An error occurred while executing command '{command}': {e}")

def run_interpreter(deck):
    print("Initial Deck:", deck)

    while True:
        command = input("Enter command: ")
        if command == "exit":
            break

        commands = command.split('&&')
        for cmd in commands:
            interpret_command(deck, cmd.strip())
        
        print("Current Deck:", deck)

if __name__ == "__main__":
    deck = Deck()
    run_interpreter(deck)
