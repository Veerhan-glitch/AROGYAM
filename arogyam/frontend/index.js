// Handle splash screen
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('splash').style.display = 'none';
    
    // Check if user is already logged in
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentUser) {
      showDashboard(currentUser);
    } else {
      document.getElementById('loginSection').style.display = 'flex';
    }
  }, 2500);
  
  // Update cart count
  updateCartCount();
});

// Show Register Section
function showRegister() {
  document.getElementById('loginSection').style.display = 'none';
  document.getElementById('registerSection').style.display = 'flex';
  document.getElementById('userDashboard').style.display = 'none';
  document.getElementById('doctorDashboard').style.display = 'none';
}

// Show Login Section
function showLogin() {
  document.getElementById('registerSection').style.display = 'none';
  document.getElementById('loginSection').style.display = 'flex';
  document.getElementById('userDashboard').style.display = 'none';
  document.getElementById('doctorDashboard').style.display = 'none';
}

// Handle Login
function handleLogin(event) {
  event.preventDefault();
  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;
  const userType = document.getElementById('loginUserType').value;

  // Basic validation
  if (!email || !password || !userType) {
    alert('Please fill in all fields');
    return;
  }

  // Get users from localStorage
  const users = JSON.parse(localStorage.getItem('users')) || [];
  const user = users.find(u => u.email === email && u.password === password && u.userType === userType);

  if (user) {
    // Store current user
    localStorage.setItem('currentUser', JSON.stringify(user));
    document.getElementById('loginForm').reset();
    showDashboard(user);
  } else {
    alert('Invalid credentials or user type');
  }
}

// Handle Register
function handleRegister(event) {
  event.preventDefault();
  const name = document.getElementById('registerName').value;
  const email = document.getElementById('registerEmail').value;
  const password = document.getElementById('registerPassword').value;
  const phone = document.getElementById('registerPhone').value;
  const userType = document.getElementById('registerUserType').value;

  // Basic validation
  if (!name || !email || !password || !phone || !userType) {
    alert('Please fill in all fields');
    return;
  }

  // Validate email format
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    alert('Please enter a valid email address');
    return;
  }

  // Validate phone number (basic)
  const phoneRegex = /^\d{10}$/;
  if (!phoneRegex.test(phone.replace(/[-()\s]/g, ''))) {
    alert('Please enter a valid 10-digit phone number');
    return;
  }

  // Get existing users
  const users = JSON.parse(localStorage.getItem('users')) || [];

  // Check if user already exists
  if (users.some(user => user.email === email)) {
    alert('Email already registered');
    return;
  }

  // Add new user
  const newUser = {
    id: Date.now().toString(),
    name,
    email,
    password,
    phone,
    userType,
    registrationDate: new Date().toISOString()
  };
  users.push(newUser);
  localStorage.setItem('users', JSON.stringify(users));

  alert('Registration successful!');
  document.getElementById('registerForm').reset();
  showLogin();
}

// Show appropriate dashboard based on user type
function showDashboard(user) {
  // Hide all sections first
  document.getElementById('loginSection').style.display = 'none';
  document.getElementById('registerSection').style.display = 'none';
  document.getElementById('userDashboard').style.display = 'none';
  document.getElementById('doctorDashboard').style.display = 'none';

  // Then show only the appropriate dashboard
  switch (user.userType) {
    case 'user':
      document.getElementById('userDashboard').style.display = 'block';
      document.getElementById('userWelcome').textContent = `Welcome, ${user.name}!`;
      loadUserDashboard();
      break;
    case 'doctor':
      document.getElementById('doctorDashboard').style.display = 'block';
      document.getElementById('doctorWelcome').textContent = `Welcome, Dr. ${user.name}`;
      loadDoctorDashboard();
      break;
    case 'admin':
      // Redirect admin to the admin dashboard page
      window.location.href = 'pages/admin/dashboard.html';
      break;
  }
}

// Load User Dashboard Content
function loadUserDashboard() {
  // Remove the previously added advanced search section to avoid duplication
  const existingSearchSection = document.querySelector('.search-section');
  if (existingSearchSection) {
    existingSearchSection.remove();
  }

  // The "Find Doctors & Medicines" button is already in the quick access section,
  // so we don't need to add it again here

  // Load trending products
  const products = getTrendingProducts();
  const productsList = document.getElementById('trendingProductsList');
  productsList.innerHTML = products.slice(0, 5).map(product => `
    <div class="product-card">
      <h4>${product.name}</h4>
      <div class="rating">Rating: ${product.rating} ⭐</div>
      <div class="reviews">${product.reviews} reviews</div>
      <div class="price">₹${product.price || '199'}</div>
      <button class="action-btn" onclick="addToCart('${product.id}')">
        <i class="fas fa-shopping-cart"></i> Add to Cart
      </button>
    </div>
  `).join('');

  // Load top doctors (Only 5) - without advanced search button
  const doctors = getDoctorsByRating();
  const doctorsList = document.getElementById('topDoctorsList');
  doctorsList.innerHTML = doctors.slice(0, 5).map(doctor => `
    <div class="doctor-card">
      <h4>${doctor.name}</h4>
      <div>${doctor.specialization}</div>
      <div class="rating">Rating: ${doctor.rating} ⭐</div>
      <div class="visits">${doctor.patientVisits} patient visits</div>
      <button class="action-btn" onclick="window.location.href='pages/user/appointments.html#book?doctorId=${doctor.id}'">Book Appointment</button>
    </div>
  `).join('');

  // Load appointments
  const appointments = getUpcomingAppointments();
  const appointmentsList = document.getElementById('appointmentsList');
  appointmentsList.innerHTML = appointments.length ? 
    `<div class="dashboard-preview">
      <p>You have ${appointments.length} upcoming appointments</p>
      <button class="action-btn" onclick="window.location.href='pages/user/appointments.html'">Manage Appointments</button>
    </div>` : 
    `<div class="dashboard-preview">
      <p>No upcoming appointments</p>
      <button class="action-btn" onclick="window.location.href='pages/user/appointments.html'">Book Appointment</button>
    </div>`;

  // Load prescriptions section
  const prescriptionsList = document.getElementById('prescriptionsList');
  prescriptionsList.innerHTML = `
    <div class="dashboard-preview">
      <div class="upload-section">
        <button class="action-btn" onclick="window.location.href='pages/user/prescriptions.html'">Manage Prescriptions</button>
      </div>
    </div>
  `;

  // Load order history
  const orders = getOrderHistory();
  const ordersList = document.getElementById('ordersList');
  ordersList.innerHTML = orders.length ? 
    `<div class="dashboard-preview">
      <p>You have ${orders.length} orders</p>
      <button class="action-btn" onclick="showOrderHistory()">View Order History</button>
    </div>` : 
    `<div class="dashboard-preview">
      <p>No order history</p>
      <button class="action-btn" onclick="window.location.href='pages/user/trending-products.html'">Shop Now</button>
    </div>`;
    
  // Initialize user notifications
  initializeUserNotifications();
  loadUserNotifications();
}

// Load Doctor Dashboard Content
function loadDoctorDashboard() {
  // Get current user
  const currentUser = JSON.parse(localStorage.getItem('currentUser'));
  if (!currentUser) return;

  // Initialize dummy appointment data
  initializeDummyAppointments();

  // Update dummy appointments to use current doctor's ID
  updateDummyAppointmentsWithCurrentDoctor(currentUser.id);

  // Load doctor's appointments for today
  const appointments = getTodaysAppointments();
  const appointmentsList = document.getElementById('todayAppointmentsList');
  if (!appointmentsList) return;
  
  // Load doctor rating
  loadDoctorRating();
}

// Update dummy appointments to use current doctor's ID
function updateDummyAppointmentsWithCurrentDoctor(doctorId) {
  // Get appointments from localStorage
  const appointments = JSON.parse(localStorage.getItem('appointments')) || [];
  
  // Find appointments with doctorId 'doc1' (our dummy default) and update to current doctor
  let updated = false;
  appointments.forEach(app => {
    if (app.doctorId === 'doc1') {
      app.doctorId = doctorId;
      updated = true;
    }
  });
  
  // Save back if updated
  if (updated) {
    localStorage.setItem('appointments', JSON.stringify(appointments));
  }
}

// Get today's appointments
function getTodaysAppointments() {
  const currentUser = JSON.parse(localStorage.getItem('currentUser'));
  if (!currentUser) return [];
  
  // Create today's date without time
  const today = new Date();
  const todayStr = today.toISOString().split('T')[0]; // YYYY-MM-DD format
  
  const appointments = JSON.parse(localStorage.getItem('appointments')) || [];
  
  console.log('Today string:', todayStr);
  console.log('All appointments:', appointments);
  
  // Filter appointments for today using string comparison for consistent results
  const todayAppointments = appointments.filter(app => {
    console.log(`Comparing ${app.date} with ${todayStr}`, app.date === todayStr, app.doctorId, currentUser.id);
    return app.doctorId === currentUser.id && app.date === todayStr;
  });
  
  console.log('Today appointments:', todayAppointments);
  
  return todayAppointments;
}

// Load Doctor Rating
function loadDoctorRating() {
  const currentUser = JSON.parse(localStorage.getItem('currentUser'));
  if (!currentUser) return;
  
  // Get doctors from localStorage
  const doctors = JSON.parse(localStorage.getItem('doctors')) || [];
  let doctor = doctors.find(doc => doc.userId === currentUser.id);
  
  // If not found in localStorage, use demo data
  if (!doctor) {
    const demoData = getDoctorsByRating().find(doc => 
      doc.name.includes(currentUser.name) || doc.name.includes(currentUser.name.replace('Dr. ', '')));
    
    if (demoData) {
      doctor = demoData;
    } else {
      doctor = {
        rating: 4.5
      };
    }
  }
  
  // Update rating display
  document.getElementById('doctorRatingValue').textContent = doctor.rating ? doctor.rating.toFixed(1) : '0.0';
  
  // Update star rating visually
  updateStarRating(doctor.rating || 0);
}

// Update star rating display
function updateStarRating(rating) {
  const starsContainer = document.querySelector('.rating-stars');
  if (!starsContainer) return;
  
  // Clear existing stars
  starsContainer.innerHTML = '';
  
  // Calculate full and partial stars
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 >= 0.5;
  const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
  
  // Add full stars
  for (let i = 0; i < fullStars; i++) {
    starsContainer.innerHTML += '<i class="fas fa-star"></i>';
  }
  
  // Add half star if needed
  if (hasHalfStar) {
    starsContainer.innerHTML += '<i class="fas fa-star-half-alt"></i>';
  }
  
  // Add empty stars
  for (let i = 0; i < emptyStars; i++) {
    starsContainer.innerHTML += '<i class="far fa-star"></i>';
  }
}

// Load Admin Dashboard Content
function loadAdminDashboard() {
  // This function is no longer needed as we redirect to the admin dashboard page
  // But kept for backwards compatibility
}

// Handle prescription upload for users
function handlePrescriptionUpload() {
  window.location.href = 'pages/user/prescriptions.html';
}

// Handle prescription upload for doctors
function handleDoctorPrescriptionUpload() {
  const patientId = document.getElementById('patientSelect').value;
  
  if (!patientId) {
    alert('Please select a patient');
    return;
  }
  
  window.location.href = 'pages/doctor/prescriptions.html?patientId=' + patientId;
}

// Toggle Notifications
function toggleNotifications() {
  const dropdown = document.getElementById('notifDropdown');
  
  // Load notifications from localStorage
  loadUserNotifications();
  
  // Toggle dropdown visibility
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';

  // Close dropdown when clicking outside
  document.addEventListener('click', function closeDropdown(e) {
    if (!e.target.closest('.notification')) {
      dropdown.style.display = 'none';
      document.removeEventListener('click', closeDropdown);
    }
  });
}

// Load user notifications
function loadUserNotifications() {
  const currentUser = JSON.parse(localStorage.getItem('currentUser'));
  if (!currentUser) return;
  
  // Get notifications from localStorage
  const allNotifications = JSON.parse(localStorage.getItem('notifications')) || [];
  
  // Filter notifications for current user
  const userNotifications = allNotifications.filter(notif => notif.userId === currentUser.id)
    .sort((a, b) => new Date(b.date) - new Date(a.date)) // Most recent first
    .slice(0, 5); // Limit to 5 notifications
  
  // Update notification count
  const unreadCount = userNotifications.filter(notif => !notif.read).length;
  const notifCountElements = document.querySelectorAll('.notification .notif-count');
  notifCountElements.forEach(element => {
    element.textContent = unreadCount;
    // Hide count if zero
    element.style.display = unreadCount > 0 ? 'inline-block' : 'none';
  });
  
  // Update notification list
  const notifList = document.getElementById('notificationsList');
  if (!notifList) return;
  
  if (userNotifications.length === 0) {
    notifList.innerHTML = '<li class="no-notifications">No notifications</li>';
    return;
  }
  
  notifList.innerHTML = userNotifications.map(notification => {
    // Format date
    const notifDate = new Date(notification.date);
    const today = new Date();
    let dateText;
    
    if (notifDate.toDateString() === today.toDateString()) {
      // Today - show time
      dateText = notifDate.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    } else {
      // Not today - show date
      dateText = notifDate.toLocaleDateString();
    }
    
    // Format notification item
    return `
      <li class="${notification.read ? 'read' : 'unread'}" onclick="markNotificationAsRead('${notification.id}')">
        <div class="notif-content">
          <strong>${notification.title || 'Notification'}</strong>
          <p>${notification.message}</p>
          <span class="notif-time">${dateText}</span>
        </div>
      </li>
    `;
  }).join('');
}

// Mark notification as read
function markNotificationAsRead(notificationId) {
  // Get notifications from localStorage
  const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
  
  // Find and update the notification
  const notification = notifications.find(n => n.id === notificationId);
  if (notification) {
    notification.read = true;
    
    // Save updated notifications
    localStorage.setItem('notifications', JSON.stringify(notifications));
    
    // Reload notifications
    loadUserNotifications();
  }
}

// Logout
function logout() {
  if (confirm('Are you sure you want to logout?')) {
    localStorage.removeItem('currentUser');
    
    // Hide all dashboards
    document.getElementById('userDashboard').style.display = 'none';
    document.getElementById('doctorDashboard').style.display = 'none';
    
    // Show login section
    document.getElementById('loginSection').style.display = 'flex';
  }
}

// Show feature (placeholder)
function showFeature(feature) {
  switch(feature) {
    case 'labTestsPage':
      window.location.href = 'pages/user/lab-tests.html';
      break;
    case 'trendingProductsPage':
    case 'allProductsPage':
    case 'topDoctorsPage':
      // Redirect to our analytics page that includes both doctors and medicines
      window.location.href = 'pages/user/doctor-analytics.html';
      break;
    case 'bookAppointmentsPage':
      window.location.href = 'pages/user/appointments.html';
      break;
    default:
      alert(`${feature} feature coming soon!`);
  }
}

// Show Order History
function showOrderHistory() {
  window.location.href = 'pages/user/orders.html';
}

// Show Profile
function showProfile(userType) {
  const currentUser = JSON.parse(localStorage.getItem('currentUser'));
  if (currentUser) {
    window.location.href = `pages/${userType}/profile.html`;
  }
}

// Add to cart functionality
function addToCart(productId) {
  // Get cart items from localStorage
  let cart = JSON.parse(localStorage.getItem('cart')) || [];
  
  // Get products
  const products = JSON.parse(localStorage.getItem('products')) || [];
  const medicine = JSON.parse(localStorage.getItem('medicines')) || [];
  
  // Try to find the product in products first, then in medicines
  let product = products.find(p => p.id === productId);
  if (!product) {
    product = medicine.find(p => p.id === productId);
  }
  
  if (!product) {
    alert('Product not found');
    return;
  }
  
  // Check if product already in cart
  const existingItem = cart.find(item => item.productId === productId);
  
  if (existingItem) {
    existingItem.quantity += 1;
  } else {
    cart.push({
      productId,
      productName: product.name,
      price: product.price,
      quantity: 1
    });
  }
  
  // Save cart
  localStorage.setItem('cart', JSON.stringify(cart));
  
  // Update cart count in UI
  updateCartCount();
  
  alert(`${product.name} added to cart`);
}

// Update cart count in UI
function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem('cart')) || [];
  const totalItems = cart.reduce((total, item) => total + item.quantity, 0);
  const cartCountElement = document.getElementById('cartCount');
  if (cartCountElement) {
    cartCountElement.textContent = totalItems;
    // Hide count if zero
    cartCountElement.style.display = totalItems > 0 ? 'inline-block' : 'none';
  }
}

function initializeApp() {
    initializeLocalStorage();
    setupEventListeners();
    
    if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
        loadDashboard();
    }
    
    // Initialize user notifications if they don't exist
    initializeUserNotifications();
}

function initializeUserNotifications() {
    // Get existing notifications or create empty array
    let notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    
    // Get current user
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (!currentUser) return;
    
    // Check if user already has notifications
    const userHasNotifications = notifications.some(notif => notif.userId === currentUser.id);
    
    // If user doesn't have notifications, create some default ones
    if (!userHasNotifications) {
        const today = new Date();
        const yesterday = new Date(today);
        yesterday.setDate(yesterday.getDate() - 1);
        const twoDaysAgo = new Date(today);
        twoDaysAgo.setDate(twoDaysAgo.getDate() - 2);
        
        const defaultNotifications = [
            {
                id: 'notif_' + Date.now() + '_1',
                userId: currentUser.id,
                title: "Welcome to Arogyam",
                message: "Thank you for joining our healthcare platform. Explore our features to manage your health better.",
                type: "system",
                read: false,
                date: today.toISOString()
            },
            {
                id: 'notif_' + Date.now() + '_2',
                userId: currentUser.id,
                title: "New Products Available",
                message: "Check out our newly added prescription medications and health products.",
                type: "product",
                read: false,
                date: yesterday.toISOString()
            },
            {
                id: 'notif_' + Date.now() + '_3',
                userId: currentUser.id,
                title: "Health Tip",
                message: "Remember to stay hydrated and take regular breaks from screen time for better eye health.",
                type: "health",
                read: false,
                date: twoDaysAgo.toISOString()
            },
            {
                id: 'notif_' + Date.now() + '_4',
                userId: currentUser.id,
                title: "Appointment Reminder",
                message: "Don't forget to schedule your regular health check-up this month.",
                type: "appointment",
                read: false,
                date: twoDaysAgo.toISOString()
            }
        ];
        
        // Add default notifications to storage
        notifications = [...notifications, ...defaultNotifications];
        localStorage.setItem('notifications', JSON.stringify(notifications));
    }
}

function updateNotificationCount() {
    const notificationCountBadge = document.querySelector('.notification-count');
    if (!notificationCountBadge) return;
    
    const currentUser = getCurrentUser();
    if (!currentUser) return;
    
    const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    const userNotifications = notifications.filter(notif => 
        notif.userId === currentUser.id && !notif.read
    );
    
    // Update badge
    notificationCountBadge.textContent = userNotifications.length;
    
    // Show/hide badge based on count
    if (userNotifications.length > 0) {
        notificationCountBadge.style.display = 'flex';
    } else {
        notificationCountBadge.style.display = 'none';
    }
}

// Helper function to format notification time
function formatNotificationTime(dateString) {
    const date = new Date(dateString);
    const now = new Date();
    
    // Check if notification is from today
    if (date.toDateString() === now.toDateString()) {
        return `Today at ${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')}`;
    }
    
    // Check if notification is from yesterday
    const yesterday = new Date(now);
    yesterday.setDate(now.getDate() - 1);
    if (date.toDateString() === yesterday.toDateString()) {
        return `Yesterday at ${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')}`;
    }
    
    // Return formatted date for older notifications
    return `${date.toLocaleDateString()} at ${date.getHours()}:${date.getMinutes().toString().padStart(2, '0')}`;
}

// Setup event listeners for buttons, links, etc.
function setupEventListeners() {
    // ... existing code ...
    
    // Notification dropdown toggle
    const notificationBtn = document.querySelector('.notification-btn');
    if (notificationBtn) {
        notificationBtn.addEventListener('click', toggleNotificationDropdown);
    }
    
    // Close notification dropdown when clicking outside
    document.addEventListener('click', function(event) {
        const dropdown = document.querySelector('.notification-dropdown');
        const notificationBtn = document.querySelector('.notification-btn');
        
        if (dropdown && dropdown.style.display === 'block' && 
            !dropdown.contains(event.target) && 
            !notificationBtn.contains(event.target)) {
            dropdown.style.display = 'none';
        }
    });
    
    // ... existing code ...
}

function toggleNotificationDropdown(event) {
    event.stopPropagation();
    
    const dropdown = document.querySelector('.notification-dropdown');
    
    if (dropdown.style.display === 'block') {
        dropdown.style.display = 'none';
    } else {
        // Load and display notifications
        loadUserNotifications();
        dropdown.style.display = 'block';
    }
}

function loadUserNotifications() {
    const dropdown = document.querySelector('.notification-dropdown');
    const notificationList = dropdown.querySelector('.notification-list');
    
    // Clear existing notifications
    notificationList.innerHTML = '';
    
    // Get current user
    const currentUser = getCurrentUser();
    if (!currentUser) return;
    
    // Get notifications from localStorage
    const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    const userNotifications = notifications.filter(notif => notif.userId === currentUser.id);
    
    // Sort notifications by date (newest first)
    userNotifications.sort((a, b) => new Date(b.date) - new Date(a.date));
    
    if (userNotifications.length === 0) {
        // No notifications
        notificationList.innerHTML = '<li class="no-notifications">No notifications</li>';
    } else {
        // Create notification items
        userNotifications.forEach(notification => {
            const notificationItem = document.createElement('li');
            notificationItem.classList.add('notification-item');
            
            // Add unread class if notification is not read
            if (!notification.read) {
                notificationItem.classList.add('unread');
            }
            
            // Add classes based on notification type
            notificationItem.classList.add(`notification-${notification.type}`);
            
            // Create notification content
            const formattedTime = formatNotificationTime(notification.date);
            
            notificationItem.innerHTML = `
                <div class="notification-content">
                    <h4>${notification.title}</h4>
                    <p>${notification.message}</p>
                    <span class="notification-time">${formattedTime}</span>
                </div>
                <div class="notification-actions">
                    <button class="mark-read-btn" data-id="${notification.id}">
                        ${notification.read ? 'Mark as Unread' : 'Mark as Read'}
                    </button>
                </div>
            `;
            
            // Add event listener to mark as read/unread button
            notificationItem.querySelector('.mark-read-btn').addEventListener('click', function(event) {
                event.stopPropagation();
                const notificationId = this.dataset.id;
                toggleNotificationReadStatus(notificationId);
            });
            
            // Add event listener to open notification details
            notificationItem.addEventListener('click', function() {
                openNotificationDetails(notification);
            });
            
            notificationList.appendChild(notificationItem);
        });
    }
}

function toggleNotificationReadStatus(notificationId) {
    // Get notifications from localStorage
    const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    
    // Find notification index
    const notificationIndex = notifications.findIndex(notif => notif.id === notificationId);
    
    if (notificationIndex !== -1) {
        // Toggle read status
        notifications[notificationIndex].read = !notifications[notificationIndex].read;
        
        // Save updated notifications
        localStorage.setItem('notifications', JSON.stringify(notifications));
        
        // Reload notifications UI
        loadUserNotifications();
        
        // Update notification count badge
        updateNotificationCount();
    }
}

function openNotificationDetails(notification) {
    // Mark notification as read if it's unread
    if (!notification.read) {
        // Find notification in localStorage
        const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
        const notificationIndex = notifications.findIndex(notif => notif.id === notification.id);
        
        if (notificationIndex !== -1) {
            // Mark as read
            notifications[notificationIndex].read = true;
            
            // Save updated notifications
            localStorage.setItem('notifications', JSON.stringify(notifications));
            
            // Update notification count badge
            updateNotificationCount();
        }
    }
    
    // Handle notification based on type
    switch(notification.type) {
        case 'appointment':
            // Navigate to appointments page
            window.location.href = 'appointments.html';
            break;
        case 'product':
            // Navigate to products page
            window.location.href = 'products.html';
            break;
        case 'health':
            // Navigate to health tips page
            window.location.href = 'health-tips.html';
            break;
        default:
            // For system notifications, just show the message
            alert(notification.message);
            break;
    }
}

// Toggle Profile Menu
function toggleProfileMenu() {
  const dropdown = document.getElementById('profileDropdown');
  
  // Toggle dropdown visibility
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';

  // Close dropdown when clicking outside
  document.addEventListener('click', function closeDropdown(e) {
    if (!e.target.closest('.profile-icon')) {
      dropdown.style.display = 'none';
      document.removeEventListener('click', closeDropdown);
    }
  });
}

// Toggle Doctor Profile Menu
function toggleDoctorProfileMenu() {
  const dropdown = document.getElementById('doctorProfileDropdown');
  
  // Toggle dropdown visibility
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';

  // Close dropdown when clicking outside
  document.addEventListener('click', function closeDropdown(e) {
    if (!e.target.closest('.profile-icon')) {
      dropdown.style.display = 'none';
      document.removeEventListener('click', closeDropdown);
    }
  });
}

// Toggle Admin Profile Menu
function toggleAdminProfileMenu() {
  const dropdown = document.getElementById('adminProfileDropdown');
  
  // Toggle dropdown visibility
  dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';

  // Close dropdown when clicking outside
  document.addEventListener('click', function closeDropdown(e) {
    if (!e.target.closest('.profile-icon')) {
      dropdown.style.display = 'none';
      document.removeEventListener('click', closeDropdown);
    }
  });
}

// Initialize dummy appointment data for testing
function initializeDummyAppointments() {
  // Check if appointments already exist
  let appointments = JSON.parse(localStorage.getItem('appointments')) || [];
  
  // If there are already appointments, don't add dummy data
  if (appointments.length > 0) return;
  
  // Get current date
  const today = new Date();
  const todayStr = today.toISOString().split('T')[0];
  
  // Create tomorrow's date
  const tomorrow = new Date(today);
  tomorrow.setDate(tomorrow.getDate() + 1);
  const tomorrowStr = tomorrow.toISOString().split('T')[0];
  
  // Create yesterday's date
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);
  const yesterdayStr = yesterday.toISOString().split('T')[0];
  
  // Create dates for next week
  const nextWeek = new Date(today);
  nextWeek.setDate(nextWeek.getDate() + 7);
  const nextWeekStr = nextWeek.toISOString().split('T')[0];
  
  // Create dates for last week
  const lastWeek = new Date(today);
  lastWeek.setDate(lastWeek.getDate() - 7);
  const lastWeekStr = lastWeek.toISOString().split('T')[0];
  
  // Sample patient IDs
  const patientIds = ['p1', 'p2', 'p3', 'p4', 'p5'];
  
  // Create dummy patients if they don't exist
  let patients = JSON.parse(localStorage.getItem('patients')) || [];
  
  if (patients.length === 0) {
    patients = [
      { id: 'p1', name: 'Anil Kumar', age: 42, gender: 'Male', contactNumber: '9876543210' },
      { id: 'p2', name: 'Priya Verma', age: 35, gender: 'Female', contactNumber: '8765432109' },
      { id: 'p4', name: 'Deepika Patel', age: 45, gender: 'Female', contactNumber: '6543210987' },
      { id: 'p5', name: 'Suresh Singh', age: 60, gender: 'Male', contactNumber: '5432109876' }
    ];
    
    localStorage.setItem('patients', JSON.stringify(patients));
  }
  
  // Sample appointment types
  const appointmentTypes = ['checkup', 'consultation', 'followup', 'emergency', 'routine'];
  
  // Sample appointment statuses
  const statuses = ['scheduled', 'completed', 'cancelled'];
  
  // Sample time slots
  const timeSlots = ['09:00', '10:00', '11:30', '14:00', '15:30', '16:45'];
  
  // Create dummy appointments
  const dummyAppointments = [
    // Today's appointments
    {
      id: 'app1',
      doctorId: 'doc1', // Will be replaced with current user's id
      patientId: 'p1',
      date: todayStr,
      time: '09:00',
      type: 'checkup',
      status: 'scheduled',
      notes: 'Regular health checkup'
    },
    {
      id: 'app2',
      doctorId: 'doc1',
      patientId: 'p2',
      date: todayStr,
      time: '11:30',
      type: 'consultation',
      status: 'scheduled',
      notes: 'New patient consultation'
    },
    {
      id: 'app3',
      doctorId: 'doc1',
      patientId: 'p3',
      date: todayStr,
      time: '14:00',
      type: 'followup',
      status: 'completed',
      notes: 'Follow-up after medication'
    },
    
    // Tomorrow's appointments
    {
      id: 'app4',
      doctorId: 'doc1',
      patientId: 'p4',
      date: tomorrowStr,
      time: '10:00',
      type: 'routine',
      status: 'scheduled',
      notes: 'Routine check'
    },
    {
      id: 'app5',
      doctorId: 'doc1',
      patientId: 'p5',
      date: tomorrowStr,
      time: '15:30',
      type: 'emergency',
      status: 'scheduled',
      notes: 'Urgent consultation'
    },
    
    // Yesterday's appointments
    {
      id: 'app6',
      doctorId: 'doc1',
      patientId: 'p1',
      date: yesterdayStr,
      time: '09:00',
      type: 'checkup',
      status: 'completed',
      notes: 'Regular health checkup'
    },
    {
      id: 'app7',
      doctorId: 'doc1',
      patientId: 'p3',
      date: yesterdayStr,
      time: '16:45',
      type: 'emergency',
      status: 'completed',
      notes: 'Emergency consultation'
    },
    
    // Next week appointments
    {
      id: 'app8',
      doctorId: 'doc1',
      patientId: 'p2',
      date: nextWeekStr,
      time: '14:00',
      type: 'followup',
      status: 'scheduled',
      notes: 'Follow-up after treatment'
    },
    
    // Last week appointments
    {
      id: 'app9',
      doctorId: 'doc1',
      patientId: 'p4',
      date: lastWeekStr,
      time: '11:30',
      type: 'consultation',
      status: 'cancelled',
      notes: 'Initial consultation'
    },
    {
      id: 'app10',
      doctorId: 'doc1',
      patientId: 'p5',
      date: lastWeekStr,
      time: '15:30',
      type: 'checkup',
      status: 'completed',
      notes: 'Annual checkup'
    }
  ];
  
  // Update with existing appointments
  appointments = [...appointments, ...dummyAppointments];
  
  // Save to localStorage
  localStorage.setItem('appointments', JSON.stringify(appointments));
}