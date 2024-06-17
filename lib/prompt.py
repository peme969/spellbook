from simple_term_menu import TerminalMenu


class Prompt:
    def ask(question):
        value = input(question)
        return value

    def yes_or_no(question, on_yes, on_no):
        value = input(question + " y/n: ").lower()
        if value in ["y", "yes"]:
            on_yes()
        elif value in ["n", "no"]:
            on_no()
        else:
            print("Command not recognized.")
            Prompt.yes_or_no(question, on_yes, on_no)

    def menu(options):
        terminal_menu = TerminalMenu(
            options, skip_empty_entries=True, menu_cursor_style=("fg_purple", "bold"), menu_cursor=("◈ "), menu_highlight_style=("fg_purple", "standout")
        )
        menu_entry_index = terminal_menu.show()
        selection = options[menu_entry_index]
        return selection

    def dict_menu(options):
        selection = Prompt.menu(list(options.keys()))
        selected_function = options.get(selection)
        selected_function()
