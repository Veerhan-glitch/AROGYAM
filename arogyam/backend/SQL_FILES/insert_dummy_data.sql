-- Insert Dummy Data into Users
INSERT INTO Users (UserID, Name, Address, Age, Email, PhoneNumber, Password) VALUES
(1, 'Amit Sharma', 'Mumbai, Maharashtra', 28, 'amit.sharma@example.com', '9876543210', 'password123'),
(2, 'Priya Verma', 'Delhi, Delhi', 25, 'priya.verma@example.com', '8765432109', 'securepass'),
(3, 'Rajesh Kumar', 'Bangalore, Karnataka', 35, 'rajesh.kumar@example.com', '7654321098', 'mypassword'),
(4, 'Neha Singh', 'Hyderabad, Telangana', 22, 'neha.singh@example.com', '6543210987', 'testpass'),
(5, 'Vikram Choudhary', 'Chennai, Tamil Nadu', 30, 'vikram.choudhary@example.com', '5432109876', 'hello123'),
(6, 'Rohit Mehta', 'Pune, Maharashtra', 27, 'rohit.mehta@example.com', '4321098765', 'welcome'),
(7, 'Sanya Kapoor', 'Kolkata, West Bengal', 24, 'sanya.kapoor@example.com', '3210987654', 'password123'),
(8, 'Karan Malhotra', 'Ahmedabad, Gujarat', 29, 'karan.malhotra@example.com', '2109876543', 'passme'),
(9, 'Anjali Nair', 'Jaipur, Rajasthan', 26, 'anjali.nair@example.com', '1098765432', 'supersecure'),
(10, 'Suraj Patil', 'Lucknow, Uttar Pradesh', 32, 'suraj.patil@example.com', '1987654321', 'keepitsecret'),
(11, 'Ramesh Yadav', 'Bareilly, Uttar Pradesh', 34, 'ramesh.yadav@example.com', '6547890123', 'rameshsecure'),
(12, 'Pallavi Iyer', 'Puducherry, Puducherry', 25, 'pallavi.iyer@example.com', '5438901234', 'pallavipass'),
(13, 'Varun Taneja', 'Shimoga, Karnataka', 28, 'varun.taneja@example.com', '4329012345', 'varunsecure'),
(14, 'Ayesha Khan', 'Aligarh, Uttar Pradesh', 27, 'ayesha.khan@example.com', '4329012346', 'ayeshapass'),
(15, 'Dhruv Desai', 'Vadodara, Gujarat', 30, 'dhruv.desai@example.com', '4329012347', 'dhruvsecure'),
(16, 'Meghna Chatterjee', 'Kolkata, West Bengal', 26, 'meghna.chatterjee@example.com', '4329012348', 'meghnapass'),
(17, 'Siddharth Rao', 'Bangalore, Karnataka', 29, 'siddharth.rao@example.com', '4329012349', 'siddharthsecure'),
(18, 'Anusha Shetty', 'Mangalore, Karnataka', 25, 'anusha.shetty@example.com', '4329012350', 'anushapass'),
(19, 'Harshita Mehta', 'Indore, Madhya Pradesh', 32, 'harshita.mehta@example.com', '4329012351', 'harshsecure'),
(20, 'Nakul Sharma', 'Gurgaon, Haryana', 31, 'nakul.sharma@example.com', '4329012352', 'nakulpass'),
(21, 'Veena Nair', 'Trivandrum, Kerala', 33, 'veena.nair@example.com', '4329012353', 'veenasecure'),
(22, 'Akash Joshi', 'Raipur, Chhattisgarh', 27, 'akash.joshi@example.com', '4329012354', 'akashpass'),
(23, 'Kavita Bansal', 'Agartala, Tripura', 29, 'kavita.bansal@example.com', '4329012355', 'kavitasecure'),
(24, 'Ravi Sharma', 'Jabalpur, Madhya Pradesh', 30, 'ravi.sharma@example.com', '4329012356', 'ravipass'),
(25, 'Sanya Kapoor', 'Silchar, Assam', 26, 'sanya.kapoor2@example.com', '4329012357', 'sanyasecure');

INSERT INTO Orders (OrderID, UserID, Date, Status, TrackingInfo, DeliveryOption) VALUES
(1, 1, '2024-01-05', 'Delivered', 'Track-100001', 'Express'),
(2, 1, '2024-01-15', 'Pending', 'Track-100002', 'Standard'),
(3, 3, '2024-01-10', 'Shipped', 'Track-100003', 'Express'),
(4, 3, '2024-01-22', 'Cancelled', 'Track-100004', 'Standard'),
(5, 5, '2024-01-14', 'Delivered', 'Track-100005', 'Express'),
(6, 7, '2024-01-17', 'Shipped', 'Track-100006', 'Standard'),
(7, 7, '2024-01-29', 'Pending', 'Track-100007', 'Express'),
(8, 10, '2024-01-21', 'Delivered', 'Track-100008', 'Standard'),
(9, 10, '2024-02-05', 'Pending', 'Track-100009', 'Express'),
(10, 12, '2024-01-25', 'Shipped', 'Track-100010', 'Standard'),
(11, 13, '2024-01-27', 'Delivered', 'Track-100011', 'Express'),
(12, 15, '2024-01-30', 'Cancelled', 'Track-100012', 'Standard'),
(13, 18, '2024-02-02', 'Pending', 'Track-100013', 'Express'),
(14, 19, '2024-02-05', 'Delivered', 'Track-100014', 'Standard'),
(15, 21, '2024-02-08', 'Shipped', 'Track-100015', 'Express'),
(16, 23, '2024-02-10', 'Pending', 'Track-100016', 'Standard'),
(17, 25, '2024-02-13', 'Pending', 'Track-100017', 'Express'),
(18, 25, '2024-02-15', 'Delivered', 'Track-100018', 'Standard'),
(19, 5, '2024-02-17', 'Shipped', 'Track-100019', 'Express'),
(20, 10, '2024-02-20', 'Pending', 'Track-100020', 'Standard'),
(21, 12, '2024-02-22', 'Cancelled', 'Track-100021', 'Express'),
(22, 15, '2024-02-24', 'Delivered', 'Track-100022', 'Standard'),
(23, 18, '2024-02-26', 'Shipped', 'Track-100023', 'Express'),
(24, 21, '2024-02-28', 'Pending', 'Track-100024', 'Standard'),
(25, 23, '2024-03-02', 'Delivered', 'Track-100025', 'Express');


-- Insert Dummy Data into Product
INSERT INTO Product (ProductID, Name, Brand, Price, Composition, Type, PrescriptionNeeded) VALUES
(1, 'Paracetamol 500mg', 'Cipla', 35.00, 'Paracetamol 500mg', 'Tablet', TRUE),
(2, 'Crocin Advance', 'GSK', 40.00, 'Paracetamol 650mg', 'Tablet', TRUE),
(3, 'Dolo 650', 'Micro Labs', 50.00, 'Paracetamol 650mg', 'Tablet', TRUE),
(4, 'Saridon', 'Piramal', 25.00, 'Caffeine + Paracetamol', 'Tablet', FALSE),
(5, 'Zerodol-P', 'Ipca', 60.00, 'Aceclofenac + Paracetamol', 'Tablet', TRUE),
(6, 'Augmentin 625 Duo', 'GSK', 120.00, 'Amoxicillin + Clavulanic Acid', 'Tablet', TRUE),
(7, 'Calpol 650', 'GSK', 45.00, 'Paracetamol 650mg', 'Tablet', TRUE),
(8, 'Metformin 500mg', 'Sun Pharma', 55.00, 'Metformin Hydrochloride', 'Tablet', TRUE),
(9, 'Thyronorm 50mcg', 'Abbott', 140.00, 'Thyroxine Sodium', 'Tablet', TRUE),
(10, 'Azithromycin 500mg', 'Cipla', 80.00, 'Azithromycin', 'Tablet', TRUE),
(11, 'Atorvastatin 10mg', 'Pfizer', 150.00, 'Atorvastatin Calcium', 'Tablet', TRUE),
(12, 'Pantop 40', 'Sun Pharma', 90.00, 'Pantoprazole Sodium', 'Tablet', FALSE),
(13, 'Ibuprofen 400mg', 'Ranbaxy', 30.00, 'Ibuprofen', 'Tablet', FALSE),
(14, 'Allegra 120mg', 'Sanofi', 160.00, 'Fexofenadine Hydrochloride', 'Tablet', FALSE),
(15, 'Cetirizine 10mg', 'Dr. Reddy’s', 25.00, 'Cetirizine Hydrochloride', 'Tablet', FALSE),
(16, 'Aspirin 75mg', 'Bayer', 45.00, 'Acetylsalicylic Acid', 'Tablet', FALSE),
(17, 'Montelukast 10mg', 'Cipla', 95.00, 'Montelukast Sodium', 'Tablet', TRUE),
(18, 'Losartan 50mg', 'Torrent Pharma', 85.00, 'Losartan Potassium', 'Tablet', TRUE),
(19, 'Amlodipine 5mg', 'Pfizer', 75.00, 'Amlodipine Besylate', 'Tablet', TRUE),
(20, 'Telmisartan 40mg', 'Cipla', 105.00, 'Telmisartan', 'Tablet', TRUE),
(21, 'Omeprazole 20mg', 'Dr. Reddy’s', 70.00, 'Omeprazole', 'Capsule', FALSE),
(22, 'Rantac 150', 'J.B. Chemicals', 55.00, 'Ranitidine Hydrochloride', 'Tablet', FALSE),
(23, 'ORS Powder', 'Electral', 35.00, 'Glucose + Sodium + Potassium', 'Powder', FALSE),
(24, 'ORS Liquid', 'Pedialyte', 50.00, 'Oral Rehydration Salts', 'Liquid', FALSE),
(25, 'Betadine Ointment', 'Win Medicare', 110.00, 'Povidone-Iodine', 'Ointment', FALSE);


-- Insert Dummy Data into OrderItems
INSERT INTO OrderItems (OrderItemID, OrderID, ProductID, Quantity) VALUES
(1, 1, 3, 2),
(2, 1, 7, 1),
(3, 2, 2, 3),
(4, 3, 5, 1),
(5, 4, 10, 2),
(6, 5, 1, 4),
(7, 6, 8, 2),
(8, 7, 6, 1),
(9, 8, 9, 3),
(10, 9, 4, 2),
(11, 10, 3, 5),
(12, 11, 7, 1),
(13, 12, 2, 2),
(14, 13, 5, 4),
(15, 14, 10, 1),
(16, 15, 1, 3),
(17, 16, 8, 2),
(18, 17, 6, 5),
(19, 18, 9, 1),
(20, 19, 4, 2),
(21, 20, 3, 3),
(22, 21, 7, 1),
(23, 22, 2, 4),
(24, 23, 5, 2),
(25, 24, 10, 1);

-- Insert Dummy Data into Prescription
INSERT INTO Prescription (PrescriptionID, UserID, FilePath) VALUES
(1, 1, '/prescriptions/prescription_1.pdf'),
(2, 3, '/prescriptions/prescription_2.pdf'),
(3, 5, '/prescriptions/prescription_3.pdf'),
(4, 7, '/prescriptions/prescription_4.pdf'),
(5, 10, '/prescriptions/prescription_5.pdf'),
(6, 12, '/prescriptions/prescription_6.pdf'),
(7, 15, '/prescriptions/prescription_7.pdf'),
(8, 17, '/prescriptions/prescription_8.pdf'),
(9, 18, '/prescriptions/prescription_9.pdf'),
(10, 21, '/prescriptions/prescription_10.pdf'),
(11, 23, '/prescriptions/prescription_11.pdf'),
(12, 25, '/prescriptions/prescription_12.pdf'),
(13, 1, '/prescriptions/prescription_13.pdf'),
(14, 3, '/prescriptions/prescription_14.pdf'),
(15, 5, '/prescriptions/prescription_15.pdf'),
(16, 8, '/prescriptions/prescription_16.pdf'),
(17, 10, '/prescriptions/prescription_17.pdf'),
(18, 12, '/prescriptions/prescription_18.pdf'),
(19, 15, '/prescriptions/prescription_19.pdf'),
(20, 17, '/prescriptions/prescription_20.pdf'),
(21, 18, '/prescriptions/prescription_21.pdf'),
(22, 21, '/prescriptions/prescription_22.pdf'),
(23, 23, '/prescriptions/prescription_23.pdf'),
(24, 24, '/prescriptions/prescription_24.pdf'),
(25, 25, '/prescriptions/prescription_25.pdf');



-- Insert Dummy Data into Doctors
INSERT INTO Doctor (DoctorID, Name, Rating, Specialization, Fee) VALUES
(1, 'Dr. Arvind Gupta', 4.5, 'Cardiologist', 1200.00),
(2, 'Dr. Sneha Kapoor', 4.7, 'Dermatologist', 800.00),
(3, 'Dr. Ramesh Iyer', 4.2, 'Orthopedic', 1000.00),
(4, 'Dr. Meera Sharma', 4.6, 'Gynecologist', 900.00),
(5, 'Dr. Tarun Bansal', 4.8, 'Neurologist', 1500.00),
(6, 'Dr. Anjali Verma', 4.3, 'ENT Specialist', 700.00),
(7, 'Dr. Rajeev Nair', 4.4, 'General Physician', 600.00),
(8, 'Dr. Pooja Desai', 4.9, 'Endocrinologist', 1400.00),
(9, 'Dr. Nitin Choudhary', 4.1, 'Pediatrician', 750.00),
(10, 'Dr. Kavita Malhotra', 4.5, 'Psychiatrist', 1300.00),
(11, 'Dr. Gaurav Saxena', 4.2, 'Ophthalmologist', 1100.00),
(12, 'Dr. Radhika Menon', 4.6, 'Oncologist', 1800.00),
(13, 'Dr. Vivek Yadav', 4.3, 'Nephrologist', 1600.00),
(14, 'Dr. Sonal Pillai', 4.7, 'Gastroenterologist', 1250.00),
(15, 'Dr. Ankur Tiwari', 4.8, 'Pulmonologist', 1350.00),
(16, 'Dr. Neha Joshi', 4.4, 'Dentist', 500.00),
(17, 'Dr. Sameer Shah', 4.9, 'Rheumatologist', 1550.00),
(18, 'Dr. Priya Kulkarni', 4.2, 'Urologist', 1450.00),
(19, 'Dr. Rohit Reddy', 4.6, 'Hematologist', 1750.00),
(20, 'Dr. Sanya Agrawal', 4.5, 'Allergist', 900.00),
(21, 'Dr. Vikram Patil', 4.3, 'Surgeon', 2000.00),
(22, 'Dr. Shalini Nanda', 4.7, 'Dermatologist', 850.00),
(23, 'Dr. Mohit Sen', 4.5, 'General Physician', 650.00),
(24, 'Dr. Ruchi Thakur', 4.8, 'Cardiologist', 1900.00),
(25, 'Dr. Aditya Mehta', 4.6, 'Endocrinologist', 1300.00);


-- Insert Dummy Data into Appointments
INSERT INTO BooksAppointment (AppointmentID, UserID, DoctorID, Date, Type, Status) VALUES
(1, 1, 5, '2024-02-10', 'Routine', 'Completed'),
(2, 3, 8, '2024-02-12', 'Emergency', 'Scheduled'),
(3, 5, 12, '2024-02-14', 'Follow-up', 'Completed'),
(4, 7, 4, '2024-02-16', 'Routine', 'Scheduled'),
(5, 10, 15, '2024-02-18', 'Emergency', 'Completed'),
(6, 12, 7, '2024-02-20', 'Follow-up', 'Scheduled'),
(7, 15, 10, '2024-02-22', 'Routine', 'Completed'),
(8, 17, 22, '2024-02-24', 'Emergency', 'Scheduled'),
(9, 18, 6, '2024-02-26', 'Routine', 'Completed'),
(10, 21, 14, '2024-02-28', 'Follow-up', 'Scheduled'),
(11, 23, 2, '2024-03-02', 'Emergency', 'Completed'),
(12, 25, 18, '2024-03-04', 'Routine', 'Scheduled'),
(13, 1, 9, '2024-03-06', 'Follow-up', 'Completed'),
(14, 3, 16, '2024-03-08', 'Emergency', 'Scheduled'),
(15, 5, 11, '2024-03-10', 'Routine', 'Completed'),
(16, 8, 1, '2024-03-12', 'Follow-up', 'Scheduled'),
(17, 10, 25, '2024-03-14', 'Emergency', 'Completed'),
(18, 12, 3, '2024-03-16', 'Routine', 'Scheduled'),
(19, 15, 19, '2024-03-18', 'Follow-up', 'Completed'),
(20, 17, 24, '2024-03-20', 'Emergency', 'Scheduled'),
(21, 18, 13, '2024-03-22', 'Routine', 'Completed'),
(22, 21, 20, '2024-03-24', 'Follow-up', 'Scheduled'),
(23, 23, 17, '2024-03-26', 'Emergency', 'Completed'),
(24, 24, 5, '2024-03-28', 'Routine', 'Scheduled'),
(25, 25, 21, '2024-03-30', 'Follow-up', 'Completed');


-- Insert Dummy Data into HealthRecords
INSERT INTO HealthRecords (RecordID, UserID, FilePath) VALUES
(1, 1, '/health_records/record_1.pdf'),
(2, 3, '/health_records/record_2.pdf'),
(3, 5, '/health_records/record_3.pdf'),
(4, 7, '/health_records/record_4.pdf'),
(5, 10, '/health_records/record_5.pdf'),
(6, 12, '/health_records/record_6.pdf'),
(7, 15, '/health_records/record_7.pdf'),
(8, 17, '/health_records/record_8.pdf'),
(9, 18, '/health_records/record_9.pdf'),
(10, 21, '/health_records/record_10.pdf'),
(11, 23, '/health_records/record_11.pdf'),
(12, 25, '/health_records/record_12.pdf'),
(13, 2, '/health_records/record_13.pdf'),
(14, 4, '/health_records/record_14.pdf'),
(15, 6, '/health_records/record_15.pdf'),
(16, 8, '/health_records/record_16.pdf'),
(17, 9, '/health_records/record_17.pdf'),
(18, 11, '/health_records/record_18.pdf'),
(19, 13, '/health_records/record_19.pdf'),
(20, 14, '/health_records/record_20.pdf'),
(21, 16, '/health_records/record_21.pdf'),
(22, 19, '/health_records/record_22.pdf'),
(23, 20, '/health_records/record_23.pdf'),
(24, 22, '/health_records/record_24.pdf'),
(25, 24, '/health_records/record_25.pdf');


-- Insert Dummy Data into Payments
INSERT INTO Payments (PaymentID, OrderID, Amount, Method, Status) VALUES
(1, 1, 1200.00, 'Credit Card', 'Success'),
(2, 2, 800.00, 'UPI', 'Failed'),
(3, 3, 1500.00, 'Debit Card', 'Success'),
(4, 4, 600.00, 'Net Banking', 'Success'),
(5, 5, 2000.00, 'Credit Card', 'Pending'),
(6, 6, 750.00, 'UPI', 'Success'),
(7, 7, 900.00, 'Debit Card', 'Success'),
(8, 8, 1400.00, 'Net Banking', 'Failed'),
(9, 9, 500.00, 'Credit Card', 'Success'),
(10, 10, 1000.00, 'UPI', 'Success'),
(11, 11, 1800.00, 'Debit Card', 'Pending'),
(12, 12, 700.00, 'Net Banking', 'Success'),
(13, 13, 1350.00, 'UPI', 'Success'),
(14, 14, 950.00, 'Credit Card', 'Failed'),
(15, 15, 1600.00, 'Debit Card', 'Success'),
(16, 16, 1200.00, 'Net Banking', 'Success'),
(17, 17, 1100.00, 'UPI', 'Pending'),
(18, 18, 1750.00, 'Credit Card', 'Success'),
(19, 19, 850.00, 'Debit Card', 'Success'),
(20, 20, 1950.00, 'Net Banking', 'Failed'),
(21, 21, 1050.00, 'UPI', 'Success'),
(22, 22, 1300.00, 'Credit Card', 'Pending'),
(23, 23, 1450.00, 'Debit Card', 'Success'),
(24, 24, 900.00, 'Net Banking', 'Success'),
(25, 25, 1550.00, 'UPI', 'Success');


-- Insert Dummy Data into Lab Tests
INSERT INTO LabTests (TestID, Name, Price, Status, TestDetails) VALUES
(1, 'Complete Blood Count (CBC)', 500.00, 'Completed', 'Measures different components of the blood'),
(2, 'Lipid Profile', 1200.00, 'Pending', 'Measures cholesterol levels'),
(3, 'Thyroid Function Test', 800.00, 'Completed', 'Checks T3, T4, TSH levels'),
(4, 'Liver Function Test (LFT)', 1000.00, 'Pending', 'Evaluates liver enzymes and proteins'),
(5, 'Kidney Function Test (KFT)', 900.00, 'Completed', 'Assesses kidney health'),
(6, 'Fasting Blood Sugar (FBS)', 400.00, 'Completed', 'Measures blood sugar levels after fasting'),
(7, 'Postprandial Blood Sugar (PPBS)', 450.00, 'Pending', 'Measures blood sugar levels after eating'),
(8, 'HbA1c', 850.00, 'Completed', 'Long-term blood sugar monitoring'),
(9, 'Vitamin D Test', 1300.00, 'Pending', 'Measures Vitamin D levels'),
(10, 'Vitamin B12 Test', 1100.00, 'Completed', 'Checks Vitamin B12 levels'),
(11, 'Iron Studies', 950.00, 'Pending', 'Assesses iron levels in the blood'),
(12, 'Electrolyte Panel', 700.00, 'Completed', 'Measures sodium, potassium, and chloride levels'),
(13, 'Urine Routine Examination', 300.00, 'Completed', 'Basic urine test for health screening'),
(14, 'Stool Test', 400.00, 'Pending', 'Checks for infections and digestion issues'),
(15, 'ECG (Electrocardiogram)', 1500.00, 'Completed', 'Records the electrical activity of the heart'),
(16, 'Echocardiography', 2500.00, 'Pending', 'Ultrasound imaging of the heart'),
(17, 'X-Ray Chest', 600.00, 'Completed', 'Basic chest X-ray for lung and heart conditions'),
(18, 'MRI Brain', 5000.00, 'Pending', 'Detailed brain scan using magnetic imaging'),
(19, 'CT Scan Abdomen', 4500.00, 'Completed', 'Cross-sectional imaging of the abdomen'),
(20, 'PET Scan', 8000.00, 'Pending', 'Detects cancer and other metabolic diseases'),
(21, 'Allergy Panel Test', 3000.00, 'Completed', 'Tests for various allergic reactions'),
(22, 'COVID-19 RT-PCR', 1200.00, 'Completed', 'Detects active COVID-19 infection'),
(23, 'Dengue NS1 Antigen', 1000.00, 'Pending', 'Early detection of dengue fever'),
(24, 'Malaria Parasite Test', 900.00, 'Completed', 'Checks for malaria infection'),
(25, 'HIV ELISA Test', 1500.00, 'Pending', 'Detects HIV antibodies in the blood');


-- Insert Dummy Data into Reports
INSERT INTO Reports (ReportID, FilePath, TestID) VALUES
(1, '/reports/report_1.pdf', 1),
(2, '/reports/report_2.pdf', 2),
(3, '/reports/report_3.pdf', 3),
(4, '/reports/report_4.pdf', 4),
(5, '/reports/report_5.pdf', 5),
(6, '/reports/report_6.pdf', 6),
(7, '/reports/report_7.pdf', 7),
(8, '/reports/report_8.pdf', 8),
(9, '/reports/report_9.pdf', 9),
(10, '/reports/report_10.pdf', 10),
(11, '/reports/report_11.pdf', 11),
(12, '/reports/report_12.pdf', 12),
(13, '/reports/report_13.pdf', 13),
(14, '/reports/report_14.pdf', 14),
(15, '/reports/report_15.pdf', 15),
(16, '/reports/report_16.pdf', 16),
(17, '/reports/report_17.pdf', 17),
(18, '/reports/report_18.pdf', 18),
(19, '/reports/report_19.pdf', 19),
(20, '/reports/report_20.pdf', 20),
(21, '/reports/report_21.pdf', 21),
(22, '/reports/report_22.pdf', 22),
(23, '/reports/report_23.pdf', 23),
(24, '/reports/report_24.pdf', 24),
(25, '/reports/report_25.pdf', 25);


-- Insert Dummy Data into Support Tickets
INSERT INTO SupportTickets (TicketID, UserID, IssueType, Status, Description) VALUES
(1, 1, 'Order Issue', 'Resolved', 'User reported a delayed delivery.'),
(2, 3, 'Payment Issue', 'Open', 'Payment failed, but money was deducted.'),
(3, 5, 'Account Issue', 'Open', 'User unable to reset password.'),
(4, 7, 'Technical Glitch', 'Resolved', 'App crashes on order confirmation.'),
(5, 10, 'Order Issue', 'Open', 'Received wrong product.'),
(6, 12, 'Payment Issue', 'Resolved', 'Double charge on UPI transaction.'),
(7, 15, 'Account Issue', 'Open', 'Cannot update profile details.'),
(8, 17, 'Order Issue', 'Resolved', 'Product damaged on arrival.'),
(9, 18, 'Technical Glitch', 'Open', 'Error message on login screen.'),
(10, 21, 'Order Issue', 'Resolved', 'Tracking link not working.'),
(11, 23, 'Payment Issue', 'Open', 'Refund not received for canceled order.'),
(12, 25, 'Account Issue', 'Resolved', 'User locked out after multiple attempts.'),
(13, 2, 'Order Issue', 'Open', 'Item missing from order.'),
(14, 4, 'Technical Glitch', 'Resolved', 'App logout issue reported.'),
(15, 6, 'Payment Issue', 'Open', 'UPI payment stuck on processing.'),
(16, 8, 'Order Issue', 'Resolved', 'Order marked as delivered but not received.'),
(17, 9, 'Technical Glitch', 'Open', 'Cannot add product to cart.'),
(18, 11, 'Order Issue', 'Resolved', 'Courier attempted delivery at the wrong address.'),
(19, 13, 'Account Issue', 'Open', 'Unable to change registered email.'),
(20, 14, 'Payment Issue', 'Open', 'Credit card payment failed multiple times.'),
(21, 16, 'Technical Glitch', 'Resolved', 'Images not loading on product page.'),
(22, 19, 'Order Issue', 'Open', 'Return request not processed.'),
(23, 20, 'Payment Issue', 'Resolved', 'Discount code not applied at checkout.'),
(24, 22, 'Account Issue', 'Open', 'Error while updating shipping address.'),
(25, 24, 'Order Issue', 'Resolved', 'Incorrect invoice received.');


-- Insert Dummy Data into Feedback
INSERT INTO Feedback (FeedbackID, UserID, Description, Rating) VALUES
(1, 1, 'Great service and fast delivery!', 5.0),
(2, 3, 'Product quality is good, but delivery was late.', 3.5),
(3, 5, 'Very satisfied with the consultation service.', 4.5),
(4, 7, 'App is easy to use. Had no issues.', 4.8),
(5, 10, 'Customer support was helpful with my issue.', 4.0),
(6, 12, 'Received wrong product but replacement was quick.', 3.9),
(7, 15, 'Payment process was smooth. No issues.', 5.0),
(8, 17, 'Great variety of products available.', 4.7),
(9, 18, 'Had trouble with login but support helped.', 3.8),
(10, 21, 'Order was delayed, but packaging was good.', 3.6),
(11, 23, 'Love the discounts and offers.', 4.9),
(12, 25, 'App needs improvement in loading speed.', 3.5),
(13, 2, 'Doctors are very professional and helpful.', 5.0),
(14, 4, 'Return process was a bit slow.', 3.7),
(15, 6, 'Happy with the medicine recommendations.', 4.6),
(16, 8, 'Prescription upload process was simple.', 4.4),
(17, 9, 'Wish there were more payment options.', 3.9),
(18, 11, 'Great experience using the app.', 4.8),
(19, 13, 'Need better tracking updates for orders.', 3.6),
(20, 14, 'Live chat support was very helpful.', 4.5),
(21, 16, 'Good product packaging, but delivery took time.', 3.8),
(22, 19, 'Easy to book doctor appointments.', 4.7),
(23, 20, 'Received a damaged product, but got a refund.', 3.5),
(24, 22, 'Medicine prices are reasonable compared to stores.', 4.8),
(25, 24, 'Overall a great experience. Will shop again!', 5.0);


-- Insert Dummy Data into Notifications
INSERT INTO Notifications (NotificationID, UserID, Message, DateTime, Type) VALUES
(1, 1, 'Your order has been shipped.', '2024-02-10 10:30:00', 'Order Update'),
(2, 3, 'Your appointment with Dr. Sneha Kapoor is confirmed.', '2024-02-11 14:00:00', 'Appointment'),
(3, 5, 'Payment received successfully.', '2024-02-12 09:15:00', 'Payment'),
(4, 7, 'Prescription uploaded successfully.', '2024-02-13 16:45:00', 'Prescription'),
(5, 10, 'Your order has been delivered.', '2024-02-14 18:20:00', 'Order Update'),
(6, 12, 'New discount offers are available for you.', '2024-02-15 12:00:00', 'Offer'),
(7, 15, 'Reminder: Your lab test results are ready.', '2024-02-16 08:30:00', 'Lab Test'),
(8, 17, 'Your support ticket has been resolved.', '2024-02-17 11:10:00', 'Support'),
(9, 18, 'Upcoming appointment reminder.', '2024-02-18 17:50:00', 'Appointment'),
(10, 21, 'Payment for your recent order failed.', '2024-02-19 13:25:00', 'Payment'),
(11, 23, 'Your medicine subscription is expiring soon.', '2024-02-20 09:40:00', 'Reminder'),
(12, 25, 'Flash sale! Get up to 20% off on medicines.', '2024-02-21 15:30:00', 'Offer'),
(13, 2, 'Your refund has been processed.', '2024-02-22 10:05:00', 'Payment'),
(14, 4, 'Your doctor consultation report is ready.', '2024-02-23 14:20:00', 'Health Record'),
(15, 6, 'Your order is out for delivery.', '2024-02-24 18:00:00', 'Order Update'),
(16, 8, 'Exclusive deal: Buy one get one free on vitamins.', '2024-02-25 07:30:00', 'Offer'),
(17, 9, 'Check your test results now.', '2024-02-26 16:10:00', 'Lab Test'),
(18, 11, 'We’ve added new products to our store.', '2024-02-27 08:45:00', 'General'),
(19, 13, 'Rate your last purchase experience.', '2024-02-28 12:55:00', 'Feedback'),
(20, 14, 'New feature: Track your prescriptions easily.', '2024-02-29 11:20:00', 'General'),
(21, 16, 'Reminder: Your next dose is due.', '2024-03-01 07:00:00', 'Reminder'),
(22, 19, 'Your cashback has been credited.', '2024-03-02 15:40:00', 'Payment'),
(23, 20, 'Thank you for your feedback!', '2024-03-03 09:35:00', 'Feedback'),
(24, 22, 'A doctor is available for your requested consultation.', '2024-03-04 17:10:00', 'Appointment'),
(25, 24, 'Limited time offer: Get 15% off on lab tests.', '2024-03-05 14:50:00', 'Offer');


-- Insert Dummy Data into Offers
INSERT INTO Offers (OfferID, Discount, ValidUntil) VALUES
(1, 10.00, '2024-03-10'),
(2, 15.00, '2024-03-15'),
(3, 20.00, '2024-03-20'),
(4, 5.00, '2024-03-25'),
(5, 12.50, '2024-03-30'),
(6, 18.00, '2024-04-05'),
(7, 25.00, '2024-04-10'),
(8, 7.00, '2024-04-15'),
(9, 30.00, '2024-04-20'),
(10, 22.00, '2024-04-25'),
(11, 8.00, '2024-05-01'),
(12, 14.00, '2024-05-05'),
(13, 16.50, '2024-05-10'),
(14, 28.00, '2024-05-15'),
(15, 9.00, '2024-05-20'),
(16, 11.00, '2024-05-25'),
(17, 35.00, '2024-05-30'),
(18, 6.00, '2024-06-05'),
(19, 17.00, '2024-06-10'),
(20, 23.50, '2024-06-15'),
(21, 19.00, '2024-06-20'),
(22, 13.00, '2024-06-25'),
(23, 21.00, '2024-06-30'),
(24, 26.00, '2024-07-05'),
(25, 32.00, '2024-07-10');


-- Insert Dummy Data into UserOffers
INSERT INTO UserOffers (UserID, OfferID) VALUES
(1, 3),
(2, 5),
(3, 7),
(4, 10),
(5, 12),
(6, 15),
(7, 18),
(8, 20),
(9, 22),
(10, 25),
(11, 1),
(12, 4),
(13, 6),
(14, 8),
(15, 9),
(16, 11),
(17, 13),
(18, 14),
(19, 16),
(20, 17),
(21, 19),
(22, 21),
(23, 23),
(24, 24),
(25, 2);
