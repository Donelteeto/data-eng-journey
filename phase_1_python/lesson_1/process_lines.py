with open("servers.txt", "r") as file:
    for line in file:

        clean_line = line.strip()
        if "CRITICAL" in clean_line:
            print(f"ALERT! system down: {clean_line}")
        elif "WARNING" in clean_line:
            print(f"System requires attention: {clean_line}")
        elif "OK" in clean_line:
            print(f"System healthy: {clean_line}")

print("-"*60)