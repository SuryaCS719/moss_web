# generate_root_index.py
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MOSS Reports Dashboard</title>
    <style>
        :root {
            --primary: #2c3e50;
            --secondary: #3498db;
            --light: #ecf0f1;
            --dark: #2c3e50;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: var(--light);
            min-height: 100vh;
            padding: 2rem;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
        }

        h1 {
            color: var(--primary);
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .pa-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            padding: 1rem;
        }

        .pa-card {
            background: white;
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            text-decoration: none;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        .pa-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.1);
        }

        .pa-card h2 {
            color: var(--secondary);
            margin-bottom: 0.5rem;
        }

        .auth-modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            justify-content: center;
            align-items: center;
        }

        .auth-box {
            background: white;
            padding: 2rem;
            border-radius: 10px;
            width: 90%;
            max-width: 400px;
        }

        .auth-input {
            width: 100%;
            padding: 0.8rem;
            margin: 0.8rem 0;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 1rem;
        }

        .auth-button {
            background: var(--secondary);
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
            font-size: 1rem;
            margin-top: 1rem;
        }
    </style>
    <script>
        function checkCredentials() {
            const enteredUser = document.getElementById('username').value;
            const enteredPass = document.getElementById('password').value;
            
            if(enteredUser === "cse101-admin-w25" && enteredPass === "Admin@cse101-w25") {
                window.location.href = window.location.href + "?auth=true";
                localStorage.setItem('authenticated', 'true');
            } else {
                alert('Invalid credentials');
            }
        }

        // Check URL parameter for auth
        const urlParams = new URLSearchParams(window.location.search);
        if(urlParams.has('auth') || localStorage.getItem('authenticated') === 'true') {
            document.body.style.display = 'block';
        } else {
            document.getElementById('authModal').style.display = 'flex';
        }
    </script>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔍 MOSS Reports Dashboard</h1>
            <p>Select a programming assignment to view reports</p>
        </div>
        
        <div class="pa-grid">
            <a href="./PA1/index.html" class="pa-card">
                <h2>PA1 Reports</h2>
                <p>View similarity analysis</p>
            </a>
            <a href="./PA2/index.html" class="pa-card">
                <h2>PA2 Reports</h2>
                <p>View similarity analysis</p>
            </a>
            <!-- Add more PA cards as needed -->
        </div>
    </div>

    <div id="authModal" class="auth-modal">
        <div class="auth-box">
            <h2 style="margin-bottom: 1.5rem;">🔒 Admin Login</h2>
            <input type="text" id="username" class="auth-input" placeholder="Username">
            <input type="password" id="password" class="auth-input" placeholder="Password">
            <button onclick="checkCredentials()" class="auth-button">Continue</button>
        </div>
    </div>
</body>
</html>
"""

# Write the content to the root index.html
with open("index.html", "w") as f:
    f.write(html_content)

print("Root index.html generated successfully!")