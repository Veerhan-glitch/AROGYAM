SELECT 
    d.DoctorID, 
    d.Name AS DoctorName, 
    d.Specialization, 
    COUNT(ba.AppointmentID) AS TotalVisits
FROM Doctor d
LEFT JOIN BooksAppointment ba 
ON d.DoctorID = ba.DoctorID
GROUP BY d.DoctorID, d.Name, d.Specialization
ORDER BY TotalVisits DESC;