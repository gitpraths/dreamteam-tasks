const routes = {
  '/login': { templateId: 'login' },
  '/register': { templateId: 'register' },
  '/dashboard': { templateId: 'dashboard' },
  '/credits': { templateId: 'credits' },
};

function updateRoute() {
  const path = window.location.pathname;
  const route = routes[path];

  if (!route) {
    return navigate('/login');
  }

  const template = document.getElementById(route.templateId);
  const view = template.content.cloneNode(true);
  const app = document.getElementById('app');
  app.innerHTML = '';
  app.appendChild(view);

  if (path === '/login') {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
      loginForm.addEventListener('submit', (event) => {
        event.preventDefault();
        navigate('/dashboard');
      });
    }
  }

  if (path === '/register') {
    const registerForm = document.getElementById('registerForm');
    if (registerForm) {
      registerForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        await register();
      });
    }
  }
}

function navigate(path) {
  window.history.pushState({}, path, path);
  updateRoute();
}

function onLinkClick(event) {
  event.preventDefault();
  const path = event.target.getAttribute('href');
  navigate(path);
}

window.onpopstate = () => updateRoute();

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

updateRoute();
