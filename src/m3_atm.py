import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
class ATMApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ATM")
        self.current_balance = 1000
        
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(pady=20)

        self.balance_label = tk.Label(self.main_frame, text="Current Balance ($):")
        self.balance_label.grid(row=0, column=0, columnspan=2, pady=5)

        self.balance_amount_label = tk.Label(self.main_frame, text=f"{self.current_balance}")
        self.balance_amount_label.grid(row=0, column=2, columnspan=2, pady=5)

        self.amount_label = tk.Label(self.main_frame, text="Amount ($):")
        self.amount_label.grid(row=1, column=0, columnspan=2, pady=5)

        self.amount_entry = tk.Entry(self.main_frame, width=15)
        self.amount_entry.grid(row=1, column=2, columnspan=2, pady=5)

        button_texts = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            'Withdrawal', '0', 'Deposit'
        ]

        for i, button_text in enumerate(button_texts):
            row = i // 3 + 2
            col = i % 3
            if button_text in {'Withdrawal', 'Deposit'}:
                button = tk.Button(self.main_frame, text=button_text, width=10, height=2, command=lambda text=button_text: self.process_transaction(text))
            else:
                button = tk.Button(self.main_frame, text=button_text, width=5, height=2, command=lambda text=button_text: self.add_to_amount(text))
            button.grid(row=row, column=col, padx=5, pady=5)

        self.bind("<Key>", self.key_pressed)

    def add_to_amount(self, text):
        current_text = self.amount_entry.get()
        if text == 'Withdrawal' or text == 'Deposit':
            self.process_transaction(text)
        else:
            new_text = current_text + text
            self.amount_entry.delete(0, tk.END)
            self.amount_entry.insert(0, new_text)

    def key_pressed(self, event):
        if event.char.isdigit() or event.char == '.':
            self.add_to_amount(event.char)

    def process_transaction(self, transaction_type):
        amount_text = self.amount_entry.get()
        if amount_text:
            try:
                amount_value = float(amount_text)
                if amount_value <= 0:
                    self.display_message("Invalid Amount", "Please enter a valid amount.")
                elif transaction_type == 'Withdrawal' and amount_value > self.current_balance:
                    self.display_message("Insufficient Funds", "You do not have enough balance.")
                else:
                    if transaction_type == 'Withdrawal':
                        transaction_amount = -amount_value
                        transaction_desc = "withdrawn"
                    else:
                        transaction_amount = amount_value
                        transaction_desc = "deposited"
                    
                    self.current_balance += transaction_amount
                    self.balance_amount_label.config(text=f"{self.current_balance}")
                    self.amount_entry.delete(0, tk.END)
                    self.display_message("Transaction Successful", f"${abs(amount_value):.2f} {transaction_desc} successfully.")
            except ValueError:
                self.display_message("Invalid Amount", "Please enter a valid amount.")

    def display_message(self, title, message):
        print(f"{title}: {message}")

if __name__ == "__main__":
    app = ATMApp()
    app.mainloop()

