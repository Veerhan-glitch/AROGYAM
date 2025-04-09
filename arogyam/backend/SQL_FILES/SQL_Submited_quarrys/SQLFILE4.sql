SELECT 
    DoctorID,
    Name AS DoctorName,
    Specialization,
    MAX(Rating) AS HighestRating,
    MIN(Rating) AS LowestRating
FROM Doctor
GROUP BY DoctorID, Name, Specialization;