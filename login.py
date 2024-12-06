def login(username, password):
    # Simple hardcoded credentials for demonstration
    valid_username = "admin"
    valid_password = "password123"
    
    if username == valid_username and password == valid_password:
        return "Login successful"
    else:
        return "Invalid username or password"
