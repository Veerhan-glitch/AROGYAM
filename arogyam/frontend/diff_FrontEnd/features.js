// Database Models aligned with ER Diagram
// Each model represents an entity in the diagram

// User model
function User(id, name, email, password, phone, userType) {
  return {
    id,
    name,
    email,
    password,
    phone,
    userType, // 'user', 'doctor', 'admin'
    registrationDate: new Date().toISOString()
  };
}

// Doctor model
function Doctor(id, userId, specialization, qualification, experience, consultationFee) {
  return {
    id,
    userId, // Foreign key to User
    specialization,
    qualification,
    experience,
    consultationFee,
    rating: 0,
    patientVisits: 0
  };
}

// Order model
function Order(id, userId, date, paymentMethod, status, totalAmount) {
  return {
    id,
    userId, // Foreign key to User
    date,
    paymentMethod,
    status, // 'pending', 'confirmed', 'delivered', 'cancelled'
    totalAmount
  };
}

// Product model
function Product(id, name, description, price, category, image, stockQuantity) {
  return {
    id,
    name,
    description,
    price,
    category,
    image,
    stockQuantity,
    rating: 0,
    reviews: 0
  };
}

// OrderItem model (connects Order and Product)
function OrderItem(id, orderId, productId, quantity, price) {
  return {
    id,
    orderId, // Foreign key to Order
    productId, // Foreign key to Product
    quantity,
    price
  };
}

// Prescription model
function Prescription(id, userId, doctorId, date, notes, status) {
  return {
    id,
    userId, // Foreign key to User (patient)
    doctorId, // Foreign key to Doctor
    date,
    notes,
    status, // 'active', 'expired', 'pending'
    isUploaded: true
  };
}

// PrescriptionItem model (Medicines in a prescription)
function PrescriptionItem(id, prescriptionId, name, dosage, duration, notes) {
  return {
    id,
    prescriptionId, // Foreign key to Prescription
    name,
    dosage,
    duration,
    notes
  };
}

// Appointment model
function Appointment(id, userId, doctorId, date, time, reason, status) {
  return {
    id,
    userId, // Foreign key to User (patient)
    doctorId, // Foreign key to Doctor
    date,
    time,
    reason,
    status, // 'pending', 'confirmed', 'cancelled', 'completed'
    createdAt: new Date().toISOString()
  };
}

// LabTest model
function LabTest(id, name, description, price, preparationInfo) {
  return {
    id,
    name,
    description,
    price,
    preparationInfo
  };
}

// UserLabTest model (connects User and LabTest)
function UserLabTest(id, userId, labTestId, date, status, reportPath) {
  return {
    id,
    userId, // Foreign key to User
    labTestId, // Foreign key to LabTest
    date,
    status, // 'pending', 'completed', 'cancelled'
    reportPath
  };
}

// Feedback model
function Feedback(id, userId, type, rating, comment) {
  return {
    id,
    userId, // Foreign key to User
    type, // 'product', 'doctor', 'app'
    rating,
    comment,
    date: new Date().toISOString()
  };
}

// Notification model
function Notification(id, userId, message, type, read) {
  return {
    id,
    userId, // Foreign key to User
    message,
    type, // 'appointment', 'order', 'prescription', 'general'
    read: read || false,
    createdAt: new Date().toISOString()
  };
}

// Payment model
function Payment(id, orderId, amount, method, status, transactionId) {
  return {
    id,
    orderId, // Foreign key to Order
    amount,
    method, // 'card', 'upi', 'cod'
    status, // 'pending', 'completed', 'failed'
    transactionId,
    date: new Date().toISOString()
  };
}

// Health Records model
function HealthRecord(id, userId, recordType, date, details, attachmentPath) {
  return {
    id,
    userId, // Foreign key to User
    recordType, // 'blood test', 'vaccination', 'allergy', 'medical history'
    date,
    details,
    attachmentPath
  };
}

// Data Access Functions (to simulate database operations)

// User Functions
function getTrendingProducts() {
    // Simulated data for trending products
    return [
        { 
            id: 'prod1',
            name: 'Glucofast Blood Glucose Monitor', 
            rating: 4.8, 
            reviews: 120,
            price: 1499,
            image: 'https://placehold.co/200x150/e2f4ea/0a5c36?text=Glucofast&font=roboto',
            category: 'equipment',
            description: 'Advanced blood glucose monitoring system with accurate readings and smartphone connectivity.',
            stockQuantity: 50
        },
        { 
            id: 'prod2',
            name: 'Zencalm Stress Relief Tablets', 
            rating: 4.7, 
            reviews: 95,
            price: 399,
            image: 'https://placehold.co/200x150/e4f1f9/0a4c8c?text=Zencalm&font=roboto',
            category: 'medicines',
            description: 'Natural herbal supplement to help reduce stress and anxiety with no side effects.',
            stockQuantity: 100
        },
        { 
            id: 'prod3',
            name: 'Vitaforce Multivitamin', 
            rating: 4.6, 
            reviews: 150,
            price: 649,
            image: 'https://placehold.co/200x150/faf1e4/8c640a?text=Vitaforce&font=roboto',
            category: 'medicines',
            description: 'Complete multivitamin formula with essential nutrients for daily immune support.',
            stockQuantity: 200
        },
        { 
            id: 'prod4',
            name: 'Thermocheck Digital Thermometer', 
            rating: 4.5, 
            reviews: 88,
            price: 299,
            image: 'https://placehold.co/200x150/f9e4e4/8c0a0a?text=Thermocheck&font=roboto',
            category: 'equipment',
            description: 'Fast and accurate digital thermometer with fever alert and memory function.',
            stockQuantity: 75
        },
        { 
            id: 'prod5',
            name: 'Breatheasy Nebulizer', 
            rating: 4.9, 
            reviews: 74,
            price: 1999,
            image: 'https://placehold.co/200x150/e4e6f9/0a0a8c?text=Breatheasy&font=roboto',
            category: 'equipment',
            description: 'Compact and portable nebulizer for effective medication delivery for respiratory conditions.',
            stockQuantity: 30
        },
        { 
            id: 'prod6',
            name: 'Ayurheal Immunity Booster', 
            rating: 4.4, 
            reviews: 112,
            price: 549,
            image: 'https://placehold.co/200x150/f4e2fa/5c0a8c?text=Ayurheal&font=roboto',
            category: 'wellness',
            description: 'Traditional ayurvedic formulation to strengthen immunity and improve overall health.',
            stockQuantity: 150
        }
    ];
}

function getDoctorsByRating() {
    // Simulated data for doctors sorted by rating
    return [
        { 
            id: 'doc1',
            name: 'Dr. Rajesh Kumar',
            specialization: 'Cardiology', 
            rating: 4.8,
            reviews: 124,
            patientVisits: 780,
            qualification: 'MD, DM Cardiology',
            experience: '15 years'
        },
        { 
            id: 'doc2',
            name: 'Dr. Priya Sharma',
            specialization: 'Dermatology',
            rating: 4.7,
            reviews: 98,
            patientVisits: 650,
            qualification: 'MD, Dermatology',
            experience: '10 years'
        },
        { 
            id: 'doc3',
            name: 'Dr. Vikram Singh',
            specialization: 'Orthopedics',
            rating: 4.9,
            reviews: 156,
            patientVisits: 920,
            qualification: 'MS, Orthopedics',
            experience: '18 years'
        },
        { 
            id: 'doc4',
            name: 'Dr. Neha Gupta',
            specialization: 'Pediatrics',
            rating: 4.6,
            reviews: 87,
            patientVisits: 540,
            qualification: 'MD, Pediatrics',
            experience: '8 years'
        },
        { 
            id: 'doc5',
            name: 'Dr. Rahul Mehta',
            specialization: 'Neurology',
            rating: 4.9,
            reviews: 143,
            patientVisits: 830,
            qualification: 'MD, DM Neurology',
            experience: '16 years'
        },
        { 
            id: 'doc6',
            name: 'Dr. Aisha Khan',
            specialization: 'Gynecology',
            rating: 4.8,
            reviews: 175,
            patientVisits: 970,
            qualification: 'MS, Gynecology',
            experience: '14 years'
        },
        { 
            id: 'doc7',
            name: 'Dr. Sanjay Patel',
            specialization: 'General Medicine', 
            rating: 4.5,
            reviews: 110,
            patientVisits: 780,
            qualification: 'MD, General Medicine',
            experience: '12 years'
        },
        { 
            id: 'doc8',
            name: 'Dr. Anjali Desai',
            specialization: 'Dermatology',
            rating: 4.6,
            reviews: 90,
            patientVisits: 520,
            qualification: 'MD, Dermatology',
            experience: '9 years'
        }
    ].sort((a, b) => b.rating - a.rating);
}

function getLabTests() {
    // Get lab tests from storage
    const labTests = JSON.parse(localStorage.getItem('labTests')) || [];
    
    if (labTests.length > 0) {
        return labTests;
    }
    
    // Simulated data for lab tests if none exist
    return [
        {
            id: 'lab1',
            name: 'Complete Blood Count (CBC)',
            description: 'Measures different components and features of your blood',
            price: 800,
            preparationInfo: 'No special preparation required. Fasting not necessary.'
        },
        {
            id: 'lab2',
            name: 'Blood Glucose Test',
            description: 'Measures the amount of glucose in your blood',
            price: 350,
            preparationInfo: 'Fast for at least 8 hours before the test.'
        },
        {
            id: 'lab3',
            name: 'Lipid Profile',
            description: 'Measures cholesterol and triglycerides in your blood',
            price: 900,
            preparationInfo: 'Fast for 9-12 hours before the test. Water is allowed.'
        },
        {
            id: 'lab4',
            name: 'Thyroid Function Test',
            description: 'Measures thyroid hormones in your blood',
            price: 1200,
            preparationInfo: 'No special preparation required.'
        },
        {
            id: 'lab5',
            name: 'Liver Function Test',
            description: 'Assesses liver function and detects liver damage',
            price: 950,
            preparationInfo: 'Fast for 8 hours before the test.'
        }
    ];
}

function bookAppointment(doctorId, date, time, reason) {
    // Store appointment in localStorage
    const appointments = JSON.parse(localStorage.getItem('appointments')) || [];
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const doctors = getDoctorsByRating();
    const doctor = doctors.find(doc => doc.id === doctorId);
    
    if (!doctor) {
        return { success: false, message: 'Doctor not found' };
    }
    
    const newAppointment = Appointment(
        'app_' + Date.now(),
        currentUser.id,
        doctorId,
        date,
        time,
        reason,
        'pending'
    );
    
    // Add additional fields for display purposes
    newAppointment.doctorName = doctor.name;
    newAppointment.specialization = doctor.specialization;
    newAppointment.patientName = currentUser.name;
    newAppointment.patientEmail = currentUser.email;
    newAppointment.patientPhone = currentUser.phone;
    
    appointments.push(newAppointment);
    localStorage.setItem('appointments', JSON.stringify(appointments));
    
    // Create notification for the user
    createNotification(
        currentUser.id,
        `Your appointment with ${doctor.name} on ${date} at ${time} has been booked.`,
        'appointment'
    );
    
    return { success: true, appointment: newAppointment };
}

function getUpcomingAppointments() {
    const appointments = JSON.parse(localStorage.getItem('appointments')) || [];
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    // Filter appointments for current user
    if (currentUser) {
        const userAppointments = appointments.filter(app => app.userId === currentUser.id);
        
        // If no appointments, add demo data
        if (userAppointments.length === 0) {
            const doctors = getDoctorsByRating();
            
            // Demo appointments
        const demoAppointments = [
                Appointment(
                    'app_demo1',
                    currentUser.id,
                    doctors[0].id,
                    new Date(Date.now() + 2 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                    '10:00 AM',
                    'Routine heart checkup',
                    'confirmed'
                ),
                Appointment(
                    'app_demo2',
                    currentUser.id,
                    doctors[3].id,
                    new Date(Date.now() + 5 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
                    '03:30 PM',
                    'Skin rash consultation',
                    'pending'
                )
            ];
            
            // Add doctor details for display
            demoAppointments[0].doctorName = doctors[0].name;
            demoAppointments[0].specialization = doctors[0].specialization;
            demoAppointments[0].patientName = currentUser.name;
            
            demoAppointments[1].doctorName = doctors[3].name;
            demoAppointments[1].specialization = doctors[3].specialization;
            demoAppointments[1].patientName = currentUser.name;
            
            // Save demo appointments
            appointments.push(...demoAppointments);
            localStorage.setItem('appointments', JSON.stringify(appointments));
            
            return demoAppointments;
        }
        
        return userAppointments;
    }
    
    return [];
}

function uploadPrescription(file, type, notes) {
    // Simulated prescription upload
    const prescriptions = JSON.parse(localStorage.getItem('prescriptions')) || [];
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    const newPrescription = Prescription(
        'pres_' + Date.now(),
        currentUser.id,
        null, // No doctor ID for user uploads
        new Date().toISOString(),
        notes || '',
        'pending'
    );
    
    // Add fields for display
    newPrescription.patientName = currentUser.name;
    newPrescription.type = type || 'medication';
    newPrescription.fileName = file.name;
    newPrescription.validUntil = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString();
    
    prescriptions.push(newPrescription);
    localStorage.setItem('prescriptions', JSON.stringify(prescriptions));
    
    // Create notification
    createNotification(
        currentUser.id,
        'Your prescription has been uploaded and is under review.',
        'prescription'
    );
    
    return { success: true, prescription: newPrescription };
}

function getOrderHistory() {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    const orders = JSON.parse(localStorage.getItem('orders')) || [];
    
    // Filter orders for current user
    if (currentUser) {
        const userOrders = orders.filter(order => order.userId === currentUser.id);
        
        // If no orders, add demo data
        if (userOrders.length === 0) {
            const products = getTrendingProducts();
            
            // Create demo orders
        const demoOrders = [
                Order(
                    'ord_demo1',
                    currentUser.id,
                    new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(),
                    'card',
                    'delivered',
                    2847
                ),
                Order(
                    'ord_demo2',
                    currentUser.id,
                    new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
                    'upi',
                    'confirmed',
                    499
                )
            ];
            
            // Add order items
            const orderItems = [
                OrderItem('item1', 'ord_demo1', products[0].id, 1, products[0].price),
                OrderItem('item2', 'ord_demo1', products[2].id, 2, products[2].price),
                OrderItem('item3', 'ord_demo2', products[1].id, 1, products[1].price)
            ];
            
            // Attach order items to orders for display
            demoOrders[0].items = [
                { ...products[0], quantity: 1 },
                { ...products[2], quantity: 2 }
            ];
            
            demoOrders[1].items = [
                { ...products[1], quantity: 1 }
            ];
            
            // Save demo data
            localStorage.setItem('orders', JSON.stringify([...orders, ...demoOrders]));
            localStorage.setItem('orderItems', JSON.stringify([...JSON.parse(localStorage.getItem('orderItems') || '[]'), ...orderItems]));
            
            return demoOrders;
        }
        
        return userOrders;
    }
    
    return [];
}

// Doctor Features
function getTodaysAppointments() {
    const appointments = JSON.parse(localStorage.getItem('appointments')) || [];
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    // Get doctor info for current user
    const doctors = JSON.parse(localStorage.getItem('doctors')) || [];
    const doctor = doctors.find(doc => doc.userId === currentUser?.id);
    
    if (doctor) {
        // Today's date in YYYY-MM-DD format
    const today = new Date().toISOString().split('T')[0];
    
        // Filter appointments for this doctor and today
        return appointments.filter(app => 
            app.doctorId === doctor.id && 
            app.date === today
        );
    }
    
    // If the user is a doctor but no appointments found, return demo data
    if (currentUser?.userType === 'doctor') {
        const users = JSON.parse(localStorage.getItem('users')) || [];
        const patients = users.filter(u => u.userType === 'user');
        
        if (patients.length === 0) return [];
        
        // Demo patient
        const patient = patients[0];
        
        // Demo appointments for today
        return [
            Appointment(
                'app_doc_demo1',
                patient.id,
                'doc_current',
                new Date().toISOString().split('T')[0],
                '11:30 AM',
                'Regular checkup',
                'confirmed'
            ),
            Appointment(
                'app_doc_demo2',
                patient.id,
                'doc_current',
                new Date().toISOString().split('T')[0],
                '02:15 PM',
                'Follow-up consultation',
                'confirmed'
            )
        ];
    }
    
    return [];
}

function uploadPrescriptionForPatient(patientId, notes, medicines) {
    const prescriptions = JSON.parse(localStorage.getItem('prescriptions')) || [];
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    // Get doctor info for current user
    const doctors = JSON.parse(localStorage.getItem('doctors')) || [];
    const doctor = doctors.find(doc => doc.userId === currentUser?.id);
    
    if (!doctor) {
        return { success: false, message: 'Not authorized to upload prescriptions' };
    }
    
    // Get patient info
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const patient = users.find(u => u.id === patientId);
    
    if (!patient) {
        return { success: false, message: 'Patient not found' };
    }
    
    // Create new prescription
    const newPrescription = Prescription(
        'pres_' + Date.now(),
        patient.id,
        doctor.id,
        new Date().toISOString(),
        notes,
        'active'
    );
    
    // Add fields for display
    newPrescription.patientName = patient.name;
    newPrescription.doctorName = currentUser.name;
    newPrescription.validUntil = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString();
    
    // Add prescription items (medicines)
    const prescriptionItems = [];
    if (medicines && medicines.length > 0) {
        medicines.forEach((med, index) => {
            prescriptionItems.push(
                PrescriptionItem(
                    `presItem_${Date.now()}_${index}`,
                    newPrescription.id,
                    med.name,
                    med.dosage,
                    med.duration,
                    med.notes
                )
            );
        });
        
        // Attach items for display
        newPrescription.medicines = medicines;
    }
    
    // Save prescription and items
    prescriptions.push(newPrescription);
    localStorage.setItem('prescriptions', JSON.stringify(prescriptions));
    
    // Save prescription items if any
    if (prescriptionItems.length > 0) {
        const allPrescriptionItems = JSON.parse(localStorage.getItem('prescriptionItems') || '[]');
        localStorage.setItem('prescriptionItems', JSON.stringify([...allPrescriptionItems, ...prescriptionItems]));
    }
    
    // Create notification for patient
    createNotification(
        patient.id,
        `Dr. ${currentUser.name} has prescribed medicines for you.`,
        'prescription'
    );
    
    return { success: true, prescription: newPrescription };
}

// Admin Features
function getHighValueCustomers() {
    const users = JSON.parse(localStorage.getItem('users')) || [];
    const orders = JSON.parse(localStorage.getItem('orders')) || [];
    
    // Get patients/users
    const patients = users.filter(u => u.userType === 'user');
    
    // Calculate total spending for each user
    const customerSpending = patients.map(patient => {
        const userOrders = orders.filter(order => order.userId === patient.id);
        const totalSpent = userOrders.reduce((sum, order) => sum + order.totalAmount, 0);
        
        return {
            ...patient,
            totalSpent,
            orderCount: userOrders.length
        };
    });
    
    // Sort by total spent and get top 5
    return customerSpending
        .sort((a, b) => b.totalSpent - a.totalSpent)
        .slice(0, 5);
}

function getTopProducts() {
    const orderItems = JSON.parse(localStorage.getItem('orderItems')) || [];
    const products = getTrendingProducts();
    
    // Count sales for each product
    const productSales = products.map(product => {
        const sales = orderItems.filter(item => item.productId === product.id);
        const totalQuantity = sales.reduce((sum, item) => sum + item.quantity, 0);
        const totalRevenue = sales.reduce((sum, item) => sum + (item.quantity * item.price), 0);
        
        return {
            ...product,
            totalQuantity,
            totalRevenue
        };
    });
    
    // Sort by revenue and get top 5
    return productSales
        .sort((a, b) => b.totalRevenue - a.totalRevenue)
        .slice(0, 5);
}

function getUserGrowthStats() {
    const users = JSON.parse(localStorage.getItem('users')) || [];
    
    // For demo purposes, return fixed stats
    return {
        totalUsers: users.length || 100,
        newUsersThisMonth: 24,
        growthRate: 12.5,
        activeUsers: Math.floor((users.length || 100) * 0.8)
    };
}

// Utility Functions
function createNotification(userId, message, type) {
    const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    
    const newNotification = Notification(
        'notif_' + Date.now(),
        userId,
        message,
        type || 'general',
        false
    );
    
    notifications.push(newNotification);
    localStorage.setItem('notifications', JSON.stringify(notifications));
    
    return newNotification;
}

function getNotifications() {
    const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));
    
    if (currentUser) {
        return notifications.filter(notif => notif.userId === currentUser.id)
            .sort((a, b) => new Date(b.createdAt) - new Date(a.createdAt));
    }
    
    return [];
}

function markNotificationAsRead(notificationId) {
    const notifications = JSON.parse(localStorage.getItem('notifications')) || [];
    
    const updatedNotifications = notifications.map(notif => {
        if (notif.id === notificationId) {
            return { ...notif, read: true };
        }
        return notif;
    });
    
    localStorage.setItem('notifications', JSON.stringify(updatedNotifications));
}

// Export all functions to be used in other JS files
// This ensures compatibility with existing index.js 