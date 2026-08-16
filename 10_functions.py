# Functions are reusable pieces of code that can be called multiple times.

def my_function():
    """
    This is a simple function that prints a message.
    """
    print(f"Hello, this is my function!")

# Calling the function
my_function()
my_function()  # Calling the function again

print(f"\n")

def sum_two_numbers(first_number: int, second_number): # Note: The second parameter does not have a type hint, but it can be any type.
    """
    This function takes two numbers as arguments and returns their sum.
    """
    return first_number + second_number

sum_result = sum_two_numbers(5, 10)  # Calling the function with arguments
print(f"The sum is:, {sum_result}")  # Printing the result of the function call

sum_result = sum_two_numbers(2035421, 301611)  # Calling the function with different arguments
print(f"The sum is:, {sum_result}")  # Printing the result of the function call

sum_result = sum_two_numbers(1.5, 2.5)  # Calling the function with float arguments
print(f"The sum is:, {sum_result}")  # Printing the result of the function call

sum_result = sum_two_numbers("Hello ", "World!")  # Calling the function with string arguments
print(f"The sum is:, {sum_result}")  # Printing the result of the function call

print(f"\n")

def print_name(name: str, surname: str = "Zurita", alias = "no alias"):
    """
    This function takes a name as an argument and prints it.
    """
    print(f"Hello, {name} {surname}! #{alias}")  # Printing the name and surname

# Calling the function with a name and surname
print_name("Dafne", "Zurita", "Nane")  # Calling the function with both arguments
# Calling the function with only a name, using the default surname
print_name(f"Dafne")  # Calling the function with only the name argument

print(f"\n")

def print_texts(*texts):
    print(f"{texts}")  # Printing the text
    print(f"{type(texts)}")  # Printing the type of texts, which will be a tuple
    print(f"Number of texts: {len(texts)}\n")  # Printing the number of texts
    for text in texts:  # Iterating over each text in the texts tuple
        print(f"{text}")  # Printing each text

print_texts("Hola", "Mundo", "Python")  # Calling the function with multiple arguments
print_texts("Hola", "Mundo")  # Calling the function with two arguments
print_texts("Hola", 4, 23.4, True, dict(name="Saul", surname="Zurita"))  # Calling the function with mixed arguments