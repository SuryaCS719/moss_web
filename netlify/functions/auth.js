exports.handler = async (event, context) => {
  const username = "cse101-admin-w25"; // Set your username here
  const password = "Admin@cse101-w25"; // Set your password here

  const authHeader = event.headers["authorization"];

  if (!authHeader || !authHeader.startsWith("Basic ")) {
    return {
      statusCode: 401,
      headers: {
        "WWW-Authenticate": 'Basic realm="Secure Area"',
      },
      body: "Unauthorized",
    };
  }

  const encodedCredentials = authHeader.split(" ")[1];
  const credentials = Buffer.from(encodedCredentials, "base64").toString("utf-8");
  const [enteredUsername, enteredPassword] = credentials.split(":");

  if (enteredUsername === username && enteredPassword === password) {
    return {
      statusCode: 200,
      body: "Access granted",
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