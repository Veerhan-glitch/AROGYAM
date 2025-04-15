document.addEventListener('DOMContentLoaded', function () {
    // Get doctor info from the hidden element containing data attributes
    const docInfo = document.getElementById('doctor-info');
    const doctorId = docInfo.dataset.doctorId;
    const doctorName = docInfo.dataset.doctorName;
    const doctorRating = docInfo.dataset.doctorRating;
    const doctorSpecialization = docInfo.dataset.doctorSpecialization;

    // Setup loadedTabs to cache first loads for each tab
    const loadedTabs = {
        today: false,
        upcoming: false,
        past: false
    };

    // Today formatted as yyyy-mm-dd (ISO date string)
    const today = new Date().toISOString().split('T')[0];

    // Handlers for loading each tab's appointments
    const appointmentTabHandlers = {
        today: () => {
            if (!loadedTabs.today) {
                loadAppointments('today');
                loadedTabs.today = true;
            }
        },
        upcoming: () => {
            if (!loadedTabs.upcoming) {
                loadAppointments('upcoming');
                loadedTabs.upcoming = true;
            }
        },
        past: () => {
            if (!loadedTabs.past) {
                loadAppointments('past');
                loadedTabs.past = true;
            }
        }
    };

    // Display doctor info in the UI, for example welcome text or ratings
    if (!doctorId || !doctorName) {
        alert('Please log in first.');
        window.location.href = '/login';
    } else {
        document.getElementById('doctorWelcome').innerText = `Welcome, ${doctorName}`;
        document.getElementById('doctorSpecialization').innerText = doctorSpecialization;
        document.getElementById('doctorRatingValue').innerText = doctorRating;
        
        // Render rating stars (assumes rating containers contain <i> elements)
        const ratingContainers = document.querySelectorAll('.rating-value');
        ratingContainers.forEach(container => {
            const rating = parseFloat(doctorRating);
            const stars = container.querySelectorAll('i');
            stars.forEach((star, index) => {
                const starPosition = index + 1;
                if (rating >= starPosition) {
                    star.className = 'fas fa-star';
                } else if (rating >= starPosition - 0.5) {
                    star.className = 'fas fa-star-half-alt';
                } else {
                    star.className = 'far fa-star';
                }
            });
        });
        
        // Load today's appointments immediately
        loadAppointments('today');
        loadedTabs.today = true;
    }

    /**
     * Load appointments for a given tab type.
     * This function builds the request URL based on the selected filters.
     *
     * @param {string} tabType - The tab type: "today", "upcoming", or "past".
     */
    function loadAppointments(tabType) {
        // Start building the URL with the doctor id and tab indicator.
        let url = `/api/appointments/?doctorid=${doctorId}&${tabType}=true`;

        // Get the selected appointment type from the respective filter dropdown.
        // IDs used: typeFilter (today), upcomingTypeFilter, pastTypeFilter.
        let typeFilterId = tabType === 'today' ? 'typeFilter' : (tabType === 'upcoming' ? 'upcomingTypeFilter' : 'pastTypeFilter');
        const selectedType = document.getElementById(typeFilterId)?.value;

        if (selectedType && selectedType.toLowerCase() !== 'all') {
            url += `&type=${encodeURIComponent(selectedType)}`;
        }

        // For upcoming and past tabs, add date range filters.
        if (tabType === 'upcoming' || tabType === 'past') {
            // IDs for upcoming are: dateFrom and dateTo.
            // IDs for past are: pastDateFrom and pastDateTo.
            const fromDateId = tabType === 'upcoming' ? 'dateFrom' : 'pastDateFrom';
            const toDateId = tabType === 'upcoming' ? 'dateTo' : 'pastDateTo';
            const fromDate = document.getElementById(fromDateId)?.value;
            const toDate = document.getElementById(toDateId)?.value;

            if (fromDate) {
                url += `&fromDate=${fromDate}`;
            }
            if (toDate) {
                url += `&toDate=${toDate}`;
            }
        }

        // Debug log to inspect the URL.
        console.log("Fetching:", url);

        // Fetch the appointments from the backend API.
        fetch(url)
            .then(response => response.json())
            .then(data => {
                renderAppointments(data, tabType);
            })
            .catch(error => console.error('Error fetching appointments:', error));
    }

    /**
     * Render appointments in the corresponding list.
     *
     * @param {Array} appointments - The array of appointment objects from the API.
     * @param {string} type - The tab type ("today", "upcoming", or "past").
     */
    function renderAppointments(appointments, type) {
        const appointmentList = document.getElementById(`${type}AppointmentsList`);
        if (!appointments.length) {
            appointmentList.innerHTML = '<p class="empty-state">No appointments found</p>';
        } else {
            appointmentList.innerHTML = '';
            appointments.forEach(app => {
                let appointmentElement = document.createElement('div');
                appointmentElement.classList.add('appointment-item');
                appointmentElement.innerHTML = `
                    <h4>Appointment with ${app.userid}</h4>
                    <p>Date: ${app.date}</p>
                    <p>Status: ${app.status}</p>
                    <p>Type: ${app.type}</p>
                `;
                appointmentList.appendChild(appointmentElement);
            });
        }
    }

    // Setup the tab buttons to load data on first click
    document.querySelectorAll('.tab-btn').forEach(tabButton => {
        tabButton.addEventListener('click', function () {
            const tab = tabButton.dataset.tab;
            // Update UI - mark button active
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            tabButton.classList.add('active');

            // Swap the active tab content panel.
            document.querySelector('.tab-content.active').classList.remove('active');
            document.getElementById(`${tab}-tab`).classList.add('active');

            // If not already loaded for this tab, load appointments.
            if (appointmentTabHandlers[tab]) {
                appointmentTabHandlers[tab]();
            }
        });
    });

    // Set up event listeners for date range filters for upcoming and past appointments.
    // When the user changes the date input values, reload the appointments.
    document.getElementById('dateFrom')?.addEventListener('change', () => loadAppointments('upcoming'));
    document.getElementById('dateTo')?.addEventListener('change', () => loadAppointments('upcoming'));
    document.getElementById('pastDateFrom')?.addEventListener('change', () => loadAppointments('past'));
    document.getElementById('pastDateTo')?.addEventListener('change', () => loadAppointments('past'));

    // Set up event listeners for type filters.
    // When the type filter changes, reload the appointments for that tab.
    document.getElementById('typeFilter')?.addEventListener('change', () => loadAppointments('today'));
    document.getElementById('upcomingTypeFilter')?.addEventListener('change', () => loadAppointments('upcoming'));
    document.getElementById('pastTypeFilter')?.addEventListener('change', () => loadAppointments('past'));
});
