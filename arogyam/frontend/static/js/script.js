// Wait for DOM to load
window.addEventListener('DOMContentLoaded', () => {
  // Splash Screen Timeout
  setTimeout(() => {
    document.getElementById('splash').style.display = 'none';
    document.getElementById('loginSection').style.display = 'block';
  }, 2000);

  // Attach event listeners safely
  const loginForm = document.querySelector('#loginSection form');
  const registerForm = document.querySelector('#registerSection form');

  if (loginForm) {
    loginForm.addEventListener('submit', handleLogin);
  }

  if (registerForm) {
    registerForm.addEventListener('submit', handleRegister);
  }
});

// Show Register Page
function showRegister() {
  document.getElementById('loginSection').style.display = 'none';
  document.getElementById('registerSection').style.display = 'block';
}

// Show Login Page
function showLogin() {
  document.getElementById('registerSection').style.display = 'none';
  document.getElementById('loginSection').style.display = 'block';
}

// Handle Registration
function handleRegister(event) {
  event.preventDefault();

  const name = document.getElementById('regName').value;
  const email = document.getElementById('regEmail').value;
  const phone = document.getElementById('regPhone').value;
  const type = document.getElementById('regType').value;

  if (name && email && phone && type) {
    alert('Registered Successfully');
    showLogin();
  }
}

// Handle Login
function handleLogin(event) {
  event.preventDefault();
  const userType = document.getElementById('usertype').value;

  // Hide all sections first
  document.getElementById('loginSection').style.display = 'none';
  document.getElementById('registerSection').style.display = 'none';
  document.getElementById('dashboardSection').style.display = 'none';
  document.getElementById('doctorSection').style.display = 'none';
  document.getElementById('adminSection').style.display = 'none';

  // Show dashboard based on userType
  if (userType === 'user') {
    document.getElementById('dashboardSection').style.display = 'block';
  } else if (userType === 'doctor') {
    document.getElementById('doctorSection').style.display = 'block';
  } else if (userType === 'admin') {
    document.getElementById('adminSection').style.display = 'block';
  }
}

// Show Profile
function showProfile(type) {
  document.getElementById('userProfile').style.display = 'none';
  document.getElementById('doctorProfile').style.display = 'none';
  document.getElementById('adminProfile').style.display = 'none';

  if (type === 'user') {
    document.getElementById('userProfile').style.display = 'block';
  } else if (type === 'doctor') {
    document.getElementById('doctorProfile').style.display = 'block';
  } else if (type === 'admin') {
    document.getElementById('adminProfile').style.display = 'block';
  }
}

// Toggle Notifications
function toggleNotifications() {
  const dropdown = document.getElementById('notifDropdown');
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
}