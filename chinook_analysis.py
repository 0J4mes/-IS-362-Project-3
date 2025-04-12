"""
IS362 Project 3 - Chinook Database Analysis
Python Script Version
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
import urllib.request

def download_database():
    """Download the database if it doesn't exist"""
    if not os.path.exists('data'):
        os.makedirs('data')

    db_path = os.path.join('data', 'Chinook_Sqlite.sqlite')
    if not os.path.exists(db_path):
        try:
            url = 'https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite'
            urllib.request.urlretrieve(url, db_path)
            print("Database downloaded successfully")
        except Exception as e:
            print(f"Error downloading database: {e}")
            return False
    return True

def main():
    # Verify database exists
    if not download_database():
        return

    # Connect to database using absolute path
    db_path = os.path.join(os.path.dirname(__file__), 'data', 'Chinook_Sqlite.sqlite')
    try:
        conn = sqlite3.connect(db_path)
        print(f"Successfully connected to database at {db_path}")

        # Rest of your analysis code...
        query = """
        SELECT 
            i.InvoiceId,
            i.InvoiceDate,
            i.Total,
            c.FirstName || ' ' || c.LastName AS Customer,
            c.Country,
            e.FirstName || ' ' || e.LastName AS SalesAgent,
            t.Name AS Track,
            a.Title AS Album,
            g.Name AS Genre,
            il.Quantity
        FROM Invoice i
        JOIN Customer c ON i.CustomerId = c.CustomerId
        JOIN Employee e ON c.SupportRepId = e.EmployeeId
        JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
        JOIN Track t ON il.TrackId = t.TrackId
        JOIN Album a ON t.AlbumId = a.AlbumId
        JOIN Genre g ON t.GenreId = g.GenreId
        """

        df = pd.read_sql_query(query, conn)
        # ... rest of your analysis

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"General error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()