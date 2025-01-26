exports.handler = async (event, context) => {
  const username = "cse101-admin-w25"; // Set your username here
  const password = "Admin@cse101-w25"; // Set your password here

  const authHeader = event.headers["authorization"];

  // Check if the Authorization header is present and valid
  if (!authHeader || !authHeader.startsWith("Basic ")) {
    return {
      statusCode: 401,
      headers: {
        "WWW-Authenticate": 'Basic realm="Secure Area"',
      },
      body: "Unauthorized",
    };
  }

  // Decode the credentials
  const encodedCredentials = authHeader.split(" ")[1];
  const credentials = Buffer.from(encodedCredentials, "base64").toString("utf-8");
  const [enteredUsername, enteredPassword] = credentials.split(":");

  // Check if the username and password match
  if (enteredUsername === username && enteredPassword === password) {
    // Redirect to the actual site after successful authentication
    return {
      statusCode: 302, // 302 is the HTTP status code for temporary redirect
      headers: {
        Location: "/", // Redirect to the root of your site
      },
      body: "Redirecting...",
    };
  } else {
    return {
      statusCode: 401,
      headers: {
        "WWW-Authenticate": 'Basic realm="Secure Area"',
      },
      body: "Unauthorized",
    };
  }
};