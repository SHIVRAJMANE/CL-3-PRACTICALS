import xmlrpc.client

# Create an XML-RPC client
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    try:
        # Prompt the user to enter a number
        input_value_str = input("Enter the number: ")
        input_value = int(input_value_str)
        
        # Call the server's calculate_factorial method
        result = proxy.calculate_factorial(input_value)
        print(f"Factorial of {input_value} is: {result}")
    except Exception as e:
        print(f"Error: {e}")
