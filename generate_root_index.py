# generate_root_index.py

html_content = """<!DOCTYPE html>
<html>
<head>
    <title>MOSS Reports Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #0056b3;
        }
        .pa-list {
            list-style: none;
            padding: 0;
        }
        .pa-list li {
            margin: 15px 0;
        }
        .pa-list a {
            text-decoration: none;
            color: #007BFF;
            font-size: 20px;
            transition: color 0.3s;
        }
        .pa-list a:hover {
            color: #0056b3;
            text-decoration: underline;
        }
    </style>
    <script>
        // Password protection
        const username = "cse101-admin-w25"; // Set your username here
        const password = "Admin@cse101-w25"; // Set your password here
        const maxAttempts = 3; // Maximum number of password attempts
        let attempts = 0; // Counter for password attempts

        function checkPassword() {
            // Check if the user is already authenticated
            if (localStorage.getItem("authenticated") === "true") {
                document.body.style.display = "block"; // Show the content
                return;
            }

            // Prompt for username and password together
            const credentials = prompt("Enter your username and password (format: username:password):");
            if (!credentials) {
                // User clicked "Cancel" or closed the prompt
                window.location.href = "about:blank"; // Redirect to a blank page
                return;
            }

            // Split the input into username and password
            const [enteredUsername, enteredPassword] = credentials.split(":");

            // Check if the username and password are correct
            if (enteredUsername === username && enteredPassword === password) {
                // Password is correct, show the content
                document.body.style.display = "block";
                localStorage.setItem("authenticated", "true"); // Store authentication status
            } else {
                // Increment the attempt counter
                attempts++;

                // Check if the user has exceeded the maximum number of attempts
                if (attempts < maxAttempts) {
                    alert(`Incorrect username or password. You have ${maxAttempts - attempts} attempts remaining.`);
                    checkPassword(); // Retry
                } else {
                    // Redirect to a blank page after max attempts
                    alert("Maximum attempts reached. Access denied.");
                    window.location.href = "about:blank"; // Redirect to a blank page
                }
            }
        }

        // Hide the body content initially
        document.addEventListener("DOMContentLoaded", function () {
            document.body.style.display = "none";
            checkPassword();
        });
    </script>
</head>
<body>
    <h1>MOSS Reports Dashboard</h1>
    <ul class="pa-list">
        <li><a href="./PA1/index.html">PA1 Reports</a></li>
        <li><a href="./PA2/index.html">PA2 Reports</a></li>
        <!-- Add more PAs as needed -->
    </ul>
</body>
</html>
"""

# Write the content to the root index.html
with open("index.html", "w") as f:
    f.write(html_content)

print("Root index.html generated successfully!")