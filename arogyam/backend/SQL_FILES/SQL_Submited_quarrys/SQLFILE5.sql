WITH DoctorAvgRating AS (
    SELECT 
        Specialization, 
        DoctorID, 
        Name AS DoctorName, 
        ROUND(AVG(Rating), 2) AS AvgRating
    FROM Doctor
    GROUP BY Specialization, DoctorID, Name
)
SELECT d1.DoctorID, d1.DoctorName, d1.Specialization, d1.AvgRating
FROM DoctorAvgRating d1
WHERE d1.AvgRating = (
    SELECT MAX(d2.AvgRating) 
    FROM DoctorAvgRating d2 
    WHERE d2.Specialization = d1.Specialization
);