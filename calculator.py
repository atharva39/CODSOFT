# Written by [Your Name] on [Date]
# Task 2: Calculator given by CodSoft
import streamlit as st

# Define functions for arithmetic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    else:
        return a / b

# Main function to create the Streamlit app
def main():
    # Set title of the app
    st.title("Simple Calculator")
    
    # Input fields for two numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    
    # Radio buttons to select the arithmetic operation
    operation = st.radio("Select operation:", ("Addition", "Subtraction", "Multiplication", "Division"))
    
    # Button to perform calculation
    if st.button("Calculate"):
        # Perform the selected operation based on user input
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        
        # Display the result
        st.success(f"Result: {result}")

# Entry point of the program
if __name__ == "__main__":
    main()
