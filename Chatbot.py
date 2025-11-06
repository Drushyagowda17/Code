from datetime import datetime

name = "Max"

def add(a, b):
    return a + b

def todays_date():
    return datetime.now().strftime("%Y-%m-%d")

while True:
    user_message = input("bot: How may I help you? ").lower()

    if user_message == "what is your name?":
        print(f"bot: My name is {name}.") 

    elif user_message == "what is the date?":
        print(f"bot: Today's date is {todays_date()}.") 

    elif user_message.startswith("add "):  
        try:
            _, num1, num2 = user_message.split()
            result = add(int(num1), int(num2))
            print(f"bot: The sum is {result}.")  
        except ValueError:
            print("bot: Please provide two valid numbers, e.g., 'add 2 3'.")

    elif user_message == "exit":
        print("bot: Bye bye!")
        break

    else:
        print("bot: I didn't understand that. Please try again.")
      
