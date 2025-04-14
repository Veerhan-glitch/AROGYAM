// Toggle notification panel
function toggleNotifications() {
    const dropdown = document.querySelector('.notif-dropdown');
    dropdown.classList.toggle('show');
    
    // Hide profile dropdown if open
    document.querySelector('.profile-dropdown')?.classList.remove('show');
}

// Toggle profile dropdown menu
function toggleProfileMenu() {
    const dropdown = document.querySelector('.profile-dropdown');
    dropdown.classList.toggle('show');
    
    // Hide notifications if open
    document.querySelector('.notif-dropdown')?.classList.remove('show');
}

// Close dropdowns when clicking outside
document.addEventListener('click', function(event) {
    const notifIcon = document.querySelector('.notification');
    const notifDropdown = document.querySelector('.notif-dropdown');
    const profileIcon = document.querySelector('.profile-icon');
    const profileDropdown = document.querySelector('.profile-dropdown');
    
    // Handle notification dropdown
    if (notifIcon && notifDropdown) {
        if (!notifIcon.contains(event.target) && !notifDropdown.contains(event.target)) {
            notifDropdown.classList.remove('show');
        }
    }
    
    // Handle profile dropdown
    if (profileIcon && profileDropdown) {
        if (!profileIcon.contains(event.target) && !profileDropdown.contains(event.target)) {
            profileDropdown.classList.remove('show');
        }
    }
});

// Function to navigate to different pages
function navigateTo(page) {
    window.location.href = page;
} 