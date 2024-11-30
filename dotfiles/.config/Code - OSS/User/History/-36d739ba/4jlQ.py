import mechanize
import re

# Create a Browser object
br = mechanize.Browser()

# Set some options (optional)
br.set_handle_robots(False)  # Ignore robots.txt
br.set_handle_redirect(True)  # Follow redirects

# Open the page (for example, a hypothetical quiz page)
br.open("https://play.ttrockstars.com/gamel/play/garage")

# Read the page's content
page_content = br.read()

# Example: Use regex to extract a question with an operator (e.g., "What is 12 + 7?")
match = re.search(r"What is (\d+) (\*|\/) (\d+)\?", str(page_content))

if match:
    # Extract the numbers and the operator
    num1 = int(match.group(1))
    operator = match.group(2)
    num2 = int(match.group(3))
    
    # Calculate the result based on the operator
    if operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Ensure division by zero doesn't occur
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Undefined (division by zero)"
    
    # Print the result
    print(f"Result of the question: {num1} {operator} {num2} = {result}")
    
    # Select the form where the answer is submitted
    br.select_form(nr=0)  # Select the first form on the page (adjust if needed)
    
    # Fill the form with the result (answer)
    br["answer"] = str(result)  # Assuming the input field for the answer has the name "answer"
    
    # Submit the form
    response = br.submit()

    # Print the result after submitting (e.g., a confirmation page)
    print(response.read())
else:
    print("Question not found on the page.")
