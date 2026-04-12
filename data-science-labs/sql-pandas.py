import sqlite3
import pandas as pd

def analyze_movies_database(db_path):
    """
    Connects to a SQLite database, executes a complex query, 
    and loads the result directly into a Pandas DataFrame.
    """
    print(f"Connecting to {db_path}...")
    
    try:
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(db_path)
        
        # The Query: Find the top 10 highest-grossing Sci-Fi movies 
        # and calculate the ratio of their budget to their revenue.
        # We push the JOINs and MATH to the database layer for efficiency.
        sql_query = """
            SELECT 
                m.title,
                m.year,
                b.budget,
                b.revenue,
                (b.revenue * 1.0 / b.budget) AS ROI_Multiplier
            FROM movies m
            JOIN box_office b ON m.id = b.movie_id
            JOIN genres g ON m.id = g.movie_id
            WHERE g.genre = 'Sci-Fi' AND b.budget > 0
            ORDER BY ROI_Multiplier DESC
            LIMIT 10;
        """
        
        print("Executing query and fetching payload into Pandas...")
        # pd.read_sql_query is the golden bridge between SQL and Data Science
        df = pd.read_sql_query(sql_query, conn)
        
        return df

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        # Always close the connection
        if conn:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    # Assuming 'imdb.db' is downloaded via the setup script
    # results_df = analyze_movies_database('imdb.db')
    
    # print("\n--- Top 10 Most Profitable Sci-Fi Movies ---")
    # print(results_df.to_string(index=False))
    pass
