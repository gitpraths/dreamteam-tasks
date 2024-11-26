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