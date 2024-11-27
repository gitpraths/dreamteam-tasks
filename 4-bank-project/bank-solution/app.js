// Constants
const API_BASE_URL = '//localhost:5001/api/accounts'; // Server API base URL

// Global account variable
let account = null;

/**
 * Initiates login process.
 */
async function login() {
  const loginForm = document.getElementById('loginForm');
  const user = loginForm.user.value.trim();

  // Check if username is provided
  if (!user) {
    return updateElement('loginError', 'Username cannot be empty.');
  }

  // Fetch account data
  const data = await getAccount(user);

  // Handle errors
  if (data.error) {
    return updateElement('loginError', data.error);
  }

  // Store account data and navigate to dashboard
  account = data;
  navigate('/dashboard');
}

/**
 * Sends a GET request to fetch account data for a given username.
 * @param {string} user - Username to fetch account data for.
 * @returns {Object} - Account data or error message.
 */
async function getAccount(user) {
  return sendRequest('GET', `${API_BASE_URL}/${encodeURIComponent(user)}`);
}

/**
 * Sends a request to the server API.
 * @param {string} method - HTTP method (GET, POST, etc.).
 * @param {string} url - URL for the request.
 * @param {Object} [body] - Optional request body (for POST requests).
 * @returns {Object} - Response data or error message.
 */
async function sendRequest(method, url, body = null) {
  try {
    const options = {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: body ? JSON.stringify(body) : null
    };

    const response = await fetch(url, options);
    if (!response.ok) {
      throw new Error(`Error ${response.status}: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    return { error: error.message || 'Unknown error' };
  }
}

/**
 * Updates an element's content by its ID.
 * @param {string} id - Element ID.
 * @param {string|Node} textOrNode - Text or node to update the element with.
 */
function updateElement(id, textOrNode) {
  const element = document.getElementById(id);
  element.textContent = '';
  element.append(textOrNode);
}

/**
 * Registers a new user.
 */
async function register() {
  const registerForm = document.getElementById('registerForm');
  const username = registerForm.username.value.trim();
  const password = registerForm.password.value.trim();

  // Validate input fields
  if (!username || !password) {
    return updateElement('registerError', 'Both fields are required.');
  }

  // Create account
  const data = await createAccount(username, password);

  // Handle errors
  if (data.error) {
    return updateElement('registerError', data.error);
  }

  // Store account data and navigate to dashboard
  account = data;
  navigate('/dashboard');
}

/**
 * Sends a POST request to create a new account.
 * @param {string} username - Username for the new account.
 * @param {string} password - Password for the new account.
 * @returns {Object} - Account data or error message.
 */
async function createAccount(username, password) {
  return sendRequest('POST', API_BASE_URL, { username, password });
}

/**
 * Updates the dashboard with account details.
 */
function updateDashboard() {
  if (!account) {
    return navigate('/login');
  }

  // Update account information
  updateElement('description', account.description || 'No description available.');
  updateElement('balance', account.balance ? account.balance.toFixed(2) : '0.00');
  updateElement('currency', account.currency || 'USD');

  // Update transactions
  const transactionsContainer = document.getElementById('transactions');
  transactionsContainer.innerHTML = '';

  const transactionsFragment = document.createDocumentFragment();
  for (const transaction of account.transactions || []) {
    const transactionRow = createTransactionRow(transaction);
    transactionsFragment.appendChild(transactionRow);
  }
  transactionsContainer.appendChild(transactionsFragment);
}

/**
 * Creates a row for a transaction in the dashboard.
 * @param {Object} transaction - Transaction data.
 * @returns {Node} - Transaction row element.
 */
function createTransactionRow(transaction) {
  const template = document.getElementById('transaction');
  const transactionRow = template.content.cloneNode(true);
  const tr = transactionRow.querySelector('tr');
  tr.children[0].textContent = transaction.date || 'N/A';
  tr.children[1].textContent = transaction.object || 'N/A';
  tr.children[2].textContent = transaction.amount ? transaction.amount.toFixed(2) : '0.00';
  return transactionRow;
}

/**
 * Defines the routing system for navigating between pages.
 */
const routes = {
  '/login': { templateId: 'login' },
  '/register': { templateId: 'register' },
  '/dashboard': { templateId: 'dashboard', init: updateDashboard }
};

/**
 * Navigates to a specific route.
 * @param {string} path - Route path.
 */
function navigate(path) {
  const route = routes[path];
  if (!route) {
    console.error(`Route "${path}" not found.`);
    return;
  }

  const template = document.getElementById(route.templateId);
  const clone = document.importNode(template.content, true);
  const appElement = document.getElementById('app');
  appElement.innerHTML = ''; 
  appElement.appendChild(clone);

  if (route.init) {
    route.init();
  }
}

/**
 * Handles link clicks to prevent default behavior and navigate programmatically.
 * @param {Event} event - The click event.
 */
function onLinkClick(event) {
  event.preventDefault();
  const path = event.target.getAttribute('href');
  navigate(path);
}

// Initialize the app by navigating to the login page
document.addEventListener('DOMContentLoaded', () => navigate('/login'));
