1. Sub Topic 1

Assignment:

```javascript
// Global function to handle page navigation and template rendering
function onLinkClick(event) {
  event.preventDefault();  // Prevent default link behavior
  const target = event.target.getAttribute('href');  // Get the target route
  renderPage(target);  // Render the page corresponding to the target route
}

// Function to render a page based on route
function renderPage(route) {
  const templates = {
    '/login': {
      templateId: 'login',
      title: 'Login - Bank App',
      onShow: () => {} // No custom action for login
    },
    '/dashboard': {
      templateId: 'dashboard',
      title: 'Dashboard - Bank App',
      onShow: () => {
        console.log('Dashboard is shown');
      }
    },
    '/credits': {
      templateId: 'credits',
      title: 'Credits - Bank App',
      onShow: () => {} // No custom action for credits
    }
  };

  // Fetch the relevant template and title
  const { templateId, title, onShow } = templates[route];

  // Update the window title
  document.title = title;

  // Get the template content
  const template = document.getElementById(templateId).content;

  // Replace the current content with the selected template
  const app = document.getElementById('app');
  app.innerHTML = '';  // Clear current content
  app.appendChild(template.cloneNode(true)); // Add new template content

  // Run the custom code after the template changes
  onShow();
}

// Initialize the app with the login template by default
document.addEventListener('DOMContentLoaded', () => {
  renderPage('/login');  // Render the login page initially
});


```

#### Adding Titles to Each Template:

- In the `renderPage` function, we added a `title` property to each route (like `/login`, `/dashboard`, and `/credits`).
- When we navigate to a route (like when the user clicks on a link), we update the page's title using `document.title = title;`.
- For example, when we go to the dashboard, the page title will be updated to "Dashboard - Bank App".

#### Running Code After the Template Changes:

- For each route, we have an `onShow` function. This function is a place where we can put code to run every time that page is displayed.

- For the dashboard route (`/dashboard`), we added `console.log('Dashboard is shown');` inside the `onShow` function. This means that every time the dashboard is shown, you'll see the message "Dashboard is shown" in the developer console.

Challenge:

```html
<template id="credits">
      <header>
        <h1>Credits</h1>
        <a href="/dashboard" onclick="onLinkClick(event)">Back to Dashboard</a>
      </header>
      <section>
        <h2>App Development</h2>
        <p>Developed by: Prarthana</p>
        <h2>Special Thanks</h2>
        <p>Special thanks to all contributors and open-source libraries used.</p>
      </section>
</template>

```
```javascript

'/credits': { templateId: 'credits' }

```

2. Sub Topic 2:

Challenge:

```html
template id="register">
  <h1>Bank App</h1>
  <section>
    <h2>Register</h2>
    <form id="registerForm" action="javascript:register()" method="POST">
      <!-- Error Message -->
      <div id="errorMessage" style="display: none; color: red; font-size: 0.9rem; margin-bottom: 10px;">
        User already exists! Please choose a different username.
      </div>

      <label for="user">Username <span aria-label="required">*</span></label>
      <input id="user" name="user" type="text" maxlength="20" placeholder="Choose a username" required>

      <label for="currency">Currency <span aria-label="required">*</span></label>
      <input id="currency" name="currency" type="text" value="$" maxlength="5" placeholder="e.g., $, €, ₹" required>

      <label for="description">Description</label>
      <input id="description" name="description" type="text" maxlength="100" placeholder="Tell us about yourself (optional)">

      <label for="balance">Starting Balance</label>
      <input id="balance" name="balance" type="number" value="0" placeholder="Enter initial balance">

      <button type="submit">Register</button>
    </form>
  </section>
  <section>
    <p>Already registered? <a href="/login" onclick="onLinkClick(event)">Login here</a></p>
  </section>
</template>
```

```javascript
async function register() {
  const registerForm = document.getElementById('registerForm');
  const formData = new FormData(registerForm);
  const jsonData = JSON.stringify(Object.fromEntries(formData));

  try {
    const result = await createAccount(jsonData);

    const errorMessage = document.getElementById('errorMessage');

    if (result.error) {
      // Show the error message dynamically
      errorMessage.style.display = 'block';
      errorMessage.textContent = `Registration failed: ${result.error}`;
    } else {
      alert('Registration successful!');
      navigate('/login');
    }
  } catch (error) {
    console.error('An unexpected error occurred:', error);
    alert('An unexpected error occurred. Please try again.');
  }
}

async function createAccount(account) {
  try {
    const response = await fetch('//localhost:5001/api/accounts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: account,
    });
    return await response.json();
  } catch (error) {
    return { error: error.message || 'Unknown error' };
  }
}

```

Assignment:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Arial', sans-serif;
  background: linear-gradient(180deg, #008cff, #6ec1ff);
  color: #333;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

/* App Container */
#app {
  width: 400px;
  background-color: #f7f7f7;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* Headings */
h1 {
  color: #007bff;
  font-size: 1.8rem;
  margin-bottom: 20px;
}

h2 {
  font-size: 1.3rem;
  margin-bottom: 15px;
  color: #333;
}

/* Forms */
form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-bottom: 20px;
}

label {
  text-align: left;
  font-size: 0.9rem;
  color: #555;
}

input {
  padding: 10px;
  font-size: 0.9rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  transition: border-color 0.3s ease;
}

input:focus {
  outline: none;
  border-color: #007bff;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}

/* Links */
a {
  color: #007bff;
  text-decoration: none;
  font-size: 0.9rem;
  transition: color 0.3s ease;
}

a:hover {
  color: #0056b3;
}

/* Sections */
section {
  margin-bottom: 20px;
}

p {
  font-size: 0.9rem;
}

/* Table */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 15px;
}

th, td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f7f7f7;
}

td {
  font-size: 0.9rem;
}

/* Header for Dashboard */
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

header a {
  font-size: 0.9rem;
}
```
