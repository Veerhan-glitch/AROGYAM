SELECT 
    d.DoctorID, 
    d.Name, 
    d.Fee, 
    COUNT(ba.AppointmentID) AS AppointmentCount,
    ( SELECT AVG(d2.Fee)
      FROM Doctor d2
      WHERE d2.DoctorID IN (
            SELECT DISTINCT ba2.DoctorID
            FROM BooksAppointment ba2
            WHERE ba2.Date >= CURRENT_DATE - INTERVAL '360 DAY'
      )
    ) AS AvgRecentDoctorFee
FROM Doctor d
JOIN BooksAppointment ba ON d.DoctorID = ba.DoctorID
WHERE ba.Date >= CURRENT_DATE - INTERVAL '360 DAY'
GROUP BY d.DoctorID, d.Name, d.Fee;
