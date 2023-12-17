-- 01.02

-- SELECT TOP (5) * FROM [Red30Tech2].[dbo].[OnlineRetailSales$]

SELECT *
FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
WHERE [Order_Total] >= 
        (
    SELECT AVG([Order_Total])
FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
)

-- 01.03

--  SELECT * FROM [Red30Tech2].[dbo].[SpeakerInfo$]
--  SELECT * FROM [Red30Tech2].[dbo].[SessionInfo$]

SELECT [Speaker_Name], [Session_Name], [Start_date], [End_date], [Room_name]
FROM [Red30Tech2].[dbo].[SessionInfo$]
WHERE [Speaker_Name] IN (
    SELECT [Name]
FROM [Red30Tech2].[dbo].[SpeakerInfo$]
WHERE [Organization] = 'Two Trees Olive Oil'
)

-- Another way:
SELECT [Speaker_Name], sess.[Session_Name], [Start_date], [End_date], [Room_name]
FROM [Red30Tech2].[dbo].[SessionInfo$] as sess
    INNER JOIN (
        SELECT [Name]
    FROM [Red30Tech2].[dbo].[SpeakerInfo$]
    WHERE [Organization] = 'Two Trees Olive Oil'
    ) as speak ON sess.[Speaker_Name] = speak.[Name]

-- 01.04
-- Uncorrelated subquery = nested subquery

-- 01.05
-- Show names, state, email and phone of conf attendees that come from states with no Online Retail Sales

-- SELECT * FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
-- SELECT * FROM [Red30Tech2].[dbo].[ConventionAttendees$]

SELECT [First_name], [Last_name], [State], [Email], [Phone_Number]
FROM [Red30Tech2].[dbo].[ConventionAttendees$] as c
WHERE NOT EXISTS
            (
    SELECT [CustState]
FROM [Red30Tech2].[dbo].[OnlineRetailSales$] as o
WHERE c.[State] = o.[CustState]
            )

-- 01.06
-- SELECT * FROM [Red30Tech2].[dbo].[Inventory$]
-- Show ProdCategory, ProdNumber, ProdName, In_Stock of items having less than avg amount of products left

SELECT [ProdCategory], [ProdNumber], [ProdName], [In_Stock]
FROM [Red30Tech2].[dbo].[Inventory$]
WHERE [In_Stock] < (
    SELECT AVG([In_Stock])
FROM [Red30Tech2].[dbo].[Inventory$]
)

-- 02.01
WITH
    avgtotal (AVG_TOTAL)
    as
    (
        SELECT AVG([Order_Total]) as AVG_TOTAL
        FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
    )
SELECT *
FROM [Red30Tech2].[dbo].[OnlineRetailSales$], avgtotal
WHERE [Order_Total] >= AVG_TOTAL

-- 02.02
-- How many direct reports does Grant Nguyen have?
WITH
    DirectReports
    AS
    (
                    SELECT [EmployeeID], [First_name], [Last_name], [Manager]
            FROM [Red30Tech2].[dbo].[EmployeeDirectory$]
            WHERE [EmployeeID] = 42
        UNION ALL
            SELECT e.[EmployeeID], e.[First_name], e.[Last_name], e.[Manager]
            FROM [Red30Tech2].[dbo].[EmployeeDirectory$] as e
                INNER JOIN DirectReports as d on e.[Manager] = d.[EmployeeID]
    )
SELECT COUNT(*) as direct_reports
FROM DirectReports as d
WHERE d.[EmployeeID] != 42

-- 02.03
-- Show ProdCategory, ProdNumber, ProdName, In_Stock of items having less than avg amount of products left

WITH
    avg_in_stock (avgINstock)
    as
    (
        SELECT AVG([In_Stock]) as avgINstock
        FROM [Red30Tech2].[dbo].[Inventory$]
    )
SELECT [ProdCategory], [ProdNumber], [ProdName], [In_Stock]
FROM [Red30Tech2].[dbo].[Inventory$], avg_in_stock
WHERE [In_Stock] < avgINstock

-- ROW NUMBER WINDOW FUNCTION
SELECT CustName, COUNT(DISTINCT OrderNum)
FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
GROUP BY CustName

--
SELECT [OrderNum], [OrderDate], [CustName], [ProdName], [Quantity],
    ROW_NUMBER() OVER(PARTITION BY [CustName] ORDER BY [OrderDate]) as Row_Num
FROM [Red30Tech2].[dbo].[OnlineRetailSales$]

-- 
WITH 
    Row_Numbers
AS
(
    SELECT [OrderNum], [OrderDate], [CustName], [ProdName], [Quantity],
    ROW_NUMBER() OVER(PARTITION BY [CustName] ORDER BY [OrderDate]) as Row_Num
FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
    )
SELECT *
FROM Row_Numbers
WHERE Row_Num = 1


-- Show info for 3 orders with the highest Order Totals
-- from each ProdCategory purchased by Boehm Inc
WITH
    Boehms_Orders
    as
    (
        SELECT [OrderNum], [OrderDate], [CustName], [ProdCategory], [ProdName], [Order_Total],
            ROW_NUMBER() OVER(PARTITION BY [ProdCategory] ORDER BY [Order_Total] DESC) as Row_Num
        FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
        WHERE [CustName] = 'Boehm Inc.'
    )
SELECT *
FROM Boehms_Orders
WHERE Row_Num <= 3
ORDER BY [ProdCategory], [Order_Total] DESC


-- LAG / LEAD
SELECT [Start_Date], [End_Date], [Session_Name],
    LAG([Session_Name], 1) OVER(ORDER BY [Start_Date] DESC) as Prev_Sess,
    LAG([Start_Date], 1) OVER(ORDER BY [Start_Date] DESC) as Prev_Sess_Start_Time,

    LEAD([Session_Name], 1) OVER(ORDER BY [Start_Date] DESC) as Next_Sess,
    LEAD([Start_Date], 1) OVER(ORDER BY [Start_Date] DESC) as Next_Sess_Start_Time

FROM [Red30Tech2].[dbo].[SessionInfo$]
WHERE [Room_Name] = 'Room 102'

-- Show info for each drone order from the last 5 order dates:
SELECT [OrderDate], SUM([Quantity]),
    LAG(SUM([Quantity]), 1) OVER(ORDER BY [OrderDate]) as sum_1_day_before,
    LAG(SUM([Quantity]), 2) OVER(ORDER BY [OrderDate]) as sum_2_days_before,
    LAG(SUM([Quantity]), 3) OVER(ORDER BY [OrderDate]) as sum_3_days_before,
    LAG(SUM([Quantity]), 4) OVER(ORDER BY [OrderDate]) as sum_4_days_before,
    LAG(SUM([Quantity]), 5) OVER(ORDER BY [OrderDate]) as sum_5_days_before
FROM [Red30Tech2].[dbo].[OnlineRetailSales$]
WHERE [ProdCategory] = 'Drones'
GROUP BY [OrderDate]


-- RANKing
SELECT *,
    RANK() OVER(ORDER BY [Last_name]) as Rank_,
    DENSE_RANK() OVER(ORDER BY [Last_name]) as Dense_Rank_
FROM [Red30Tech2].[dbo].[EmployeeDirectory$]

-- First 3 attendees that registered from each state
WITH 
    States_Ranks
AS
(SELECT
    [State],
    ROW_NUMBER() OVER(PARTITION BY [State] ORDER BY [Registration_Date]) as Row_Num,
    RANK() OVER(PARTITION BY [State] ORDER BY [Registration_Date]) as Rank_,
    DENSE_RANK() OVER(PARTITION BY [State] ORDER BY [Registration_Date]) as Dense_Rank_,
    [Registration_Date], [First_name], [Last_name]
FROM [Red30Tech2].[dbo].[ConventionAttendees$]
)
SELECT *
FROM States_Ranks
-- WHERE Row_Num < 4
-- WHERE Dense_Rank_ < 4
WHERE Rank_ < 4