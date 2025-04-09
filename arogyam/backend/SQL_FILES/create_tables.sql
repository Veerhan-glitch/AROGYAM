-- -- Drop tables if they already exist
DROP TABLE IF EXISTS UserOffers, Orders, OrderItems, Product, Prescription, Doctor, BooksAppointment, HealthRecords, Payments, LabTests, Reports, SupportTickets, Feedback, Notifications, Offers, Users CASCADE;

-- Create Users Table
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address TEXT NOT NULL,
    Age INT CHECK (Age >= 0),
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL
);

-- Create Orders Table
CREATE TABLE Orders (
    OrderID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    Date DATE DEFAULT CURRENT_DATE,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')),
    TrackingInfo VARCHAR(100),
    DeliveryOption VARCHAR(50) NOT NULL CHECK (DeliveryOption IN ('Standard', 'Express'))
);

-- Create Product Table
CREATE TABLE Product (
    ProductID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Brand VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) CHECK (Price > 0) NOT NULL,
    Composition TEXT NOT NULL,
    Type VARCHAR(50) NOT NULL,
    PrescriptionNeeded BOOLEAN NOT NULL DEFAULT FALSE
);

-- Create OrderItems Table
CREATE TABLE OrderItems (
    OrderItemID SERIAL PRIMARY KEY,
    OrderID INT NOT NULL REFERENCES Orders(OrderID) ON DELETE CASCADE,
    ProductID INT NOT NULL REFERENCES Product(ProductID) ON DELETE CASCADE,
    Quantity INT NOT NULL CHECK (Quantity > 0)
);

-- Create Prescription Table
CREATE TABLE Prescription (
    PrescriptionID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    FilePath TEXT NOT NULL
);

-- Create Doctor Table
CREATE TABLE Doctor (
    DoctorID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Rating DECIMAL(3,2) CHECK (Rating BETWEEN 0 AND 5) NOT NULL,
    Specialization VARCHAR(100) NOT NULL,
    Fee DECIMAL(10,2) CHECK (Fee >= 0) NOT NULL
);

-- Create BooksAppointment Table
CREATE TABLE BooksAppointment (
    AppointmentID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    DoctorID INT NOT NULL REFERENCES Doctor(DoctorID) ON DELETE CASCADE,
    Date DATE NOT NULL,
    Type VARCHAR(50) NOT NULL CHECK (Type IN ('Checkup', 'Consultation', 'Follow-up', 'Emergency', 'Routine')),
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Scheduled', 'Completed', 'Cancelled'))
);

-- Create HealthRecords Table
CREATE TABLE HealthRecords (
    RecordID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    FilePath TEXT NOT NULL
);

-- Create Payments Table
CREATE TABLE Payments (
    PaymentID SERIAL PRIMARY KEY,
    OrderID INT NOT NULL REFERENCES Orders(OrderID) ON DELETE CASCADE,
    Amount DECIMAL(10,2) CHECK (Amount >= 0) NOT NULL,
    Method VARCHAR(50) NOT NULL CHECK (Method IN ('Credit Card', 'PayPal', 'Debit Card', 'UPI', 'Bank Transfer', 'Net Banking')),
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Success', 'Failed'))
);

-- Create LabTests Table
CREATE TABLE LabTests (
    TestID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) CHECK (Price >= 0) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Pending', 'Completed', 'Cancelled', '')),
    TestDetails TEXT NOT NULL
);

-- Create Reports Table
CREATE TABLE Reports (
    ReportID SERIAL PRIMARY KEY,
    FilePath TEXT NOT NULL,
    TestID INT NOT NULL REFERENCES LabTests(TestID) ON DELETE CASCADE
);

-- Create SupportTickets Table
CREATE TABLE SupportTickets (
    TicketID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    IssueType VARCHAR(100) NOT NULL,
    Status VARCHAR(50) NOT NULL CHECK (Status IN ('Open', 'Resolved', 'Closed')),
    Description TEXT NOT NULL
);

-- Create Feedback Table
CREATE TABLE Feedback (
    FeedbackID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    Description TEXT NOT NULL,
    Rating DECIMAL(3,2) CHECK (Rating BETWEEN 0 AND 5) NOT NULL
);

-- Create Notifications Table
CREATE TABLE Notifications (
    NotificationID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    Message TEXT NOT NULL,
    DateTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Type VARCHAR(50) NOT NULL CHECK (Type IN ('Appointment', 'Order Update', 'Payment', 'Prescription', 'Offer', 'Lab Test', 'Support', 'Health Record', 'General', 'Feedback', 'Reminder'))
);

-- Create Offers Table
CREATE TABLE Offers (
    OfferID SERIAL PRIMARY KEY,
    Discount DECIMAL(5,2) CHECK (Discount BETWEEN 0 AND 100) NOT NULL,
    ValidUntil DATE NOT NULL
);

-- Create UserOffers Table
CREATE TABLE UserOffers (
    UserOffersID SERIAL PRIMARY KEY,
    UserID INT NOT NULL REFERENCES Users(UserID) ON DELETE CASCADE,
    OfferID INT NOT NULL REFERENCES Offers(OfferID) ON DELETE CASCADE
);

-- Indexing for faster queries
CREATE INDEX idx_orders_user ON Orders(UserID);
CREATE INDEX idx_orderitems_order ON OrderItems(OrderID);
CREATE INDEX idx_orderitems_product ON OrderItems(ProductID);
CREATE INDEX idx_payments_order ON Payments(OrderID);
CREATE INDEX idx_feedback_user ON Feedback(UserID);
CREATE INDEX idx_supporttickets_user ON SupportTickets(UserID);
CREATE INDEX idx_notifications_user ON Notifications(UserID);
CREATE INDEX idx_healthrecords_user ON HealthRecords(UserID);
CREATE INDEX idx_booksappointment_user ON BooksAppointment(UserID);
CREATE INDEX idx_booksappointment_doctor ON BooksAppointment(DoctorID);
