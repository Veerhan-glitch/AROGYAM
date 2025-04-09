SELECT  
   u.userid AS "User ID",  u.name AS "Patient Name",   d.name AS "Doctor",  
    ba.status AS "Appt. Status",   lt.name AS "Lab Test",  lt.status AS "Test Status",
   pr.prescriptionid AS "Prescription ID"
FROM users u
LEFT JOIN booksappointment ba ON u.userid = ba.userid
LEFT JOIN doctor d ON ba.doctorid = d.doctorid
LEFT JOIN labtests lt ON u.userid = lt.testid
LEFT JOIN prescription pr ON u.userid = pr.userid
ORDER BY u.name;