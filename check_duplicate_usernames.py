from collections import Counter

def find_repeated_usernames(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip leading/trailing spaces, and filter out empty lines
            usernames = [line.strip() for line in file.read().splitlines() if line.strip()]

        # Count occurrences of each username
        username_counts = Counter(usernames)

        # Filter usernames that appear 2 or more times
        repeated_usernames = {username: count for username, count in username_counts.items() if count >= 2}

        # Output result
        if repeated_usernames:
            print("Usernames that appear 2 or more times:")
            for username, count in repeated_usernames.items():
                print(f"{username} - {count} times")
        else:
            print("No usernames appear more than once.")
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Please check the file path and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace with your actual file path
file_path = "flaggedStudentsPresent.txt"
find_repeated_usernames(file_path)
