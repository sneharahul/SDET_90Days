def validate_login(username, password):
    if username == "admin" and password == "Test@123":
        return "Login Success" 
    return "Login Failed"
def safe_divide(a, b):
    try:
       return a / b
    except ZeroDivisionError:
        return "Error: Zero division"
    assert validate_login("admin", "Test@123") == "Login Success"
    assert validate_login("user", "wrong") == "Login Failed"
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) == "Error: Zero division"
    
print("Day 2 SDET: All function + assert tests passed!")
     