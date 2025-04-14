// navigation.js - Handles page navigation and back button functionality

// Function to navigate to a different page while preserving history
function navigateTo(url) {
    window.location.href = url;
}

// Function to navigate back
function navigateBack() {
    window.history.back();
}

// Handle back button navigation from subpages to dashboard
document.addEventListener('DOMContentLoaded', () => {
    // Get all back buttons
    const backButtons = document.querySelectorAll('.back-btn');
    
    backButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent default link behavior
            
            // Check if there's a previous page in history
            if (document.referrer.includes(window.location.hostname)) {
                navigateBack();
            } else {
                // If no previous page or direct access, go to home
                navigateTo('../../index.html');
            }
        });
    });

    // Add event listener for browser back button if this is a page that needs special handling
    window.addEventListener('popstate', function(event) {
        // Custom logic for specific pages if needed
        // This can be extended for specific use cases
    });

    // Check if user is logged in for protected pages
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const isProtectedPage = !window.location.pathname.includes('index.html');
    
    if (isProtectedPage && !currentUser) {
        navigateTo('../../index.html');
    }
});

// Function to show features
function showFeature(feature) {
    switch(feature) {
        case 'labTestsPage':
            navigateTo('pages/user/lab-tests.html');
            break;
        case 'trendingProductsPage':
            navigateTo('pages/user/trending-products.html');
            break;
        case 'allProductsPage':
            navigateTo('pages/user/products.html');
            break;
        case 'bookAppointmentsPage':
            navigateTo('pages/user/appointments.html');
            break;
        default:
            alert(`${feature} feature coming soon!`);
    }
}

// Function to show Profile
function showProfile(userType) {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    if (currentUser) {
        navigateTo(`pages/${userType}/profile.html`);
    }
}

// Function to show Order History
function showOrderHistory() {
    navigateTo('pages/user/orders.html');
}

// Function to show book appointment 
function showBookAppointment() {
    navigateTo('pages/user/appointments.html#book');
} 