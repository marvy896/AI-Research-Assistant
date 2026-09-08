# First lets create the database that will store all the info
import sqlite3

connection = sqlite3.connect("research.db")
cursor = connection.cursor()
cursor.execute("""
                            CREATE TABLE IF NOT EXISTS research_projects(
                                project_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT,
                                topic TEXT,
                                problem_statement TEXT,
                                date_created TEXT DEFAULT CURRENT_TIMESTAMP
                            )
                            """)
connection.commit()
print("Research Database initialised successfully")

# connection.close()
# Dtabase created 

# SECONDLY, Lets create a Research project and stoe it
def create_research_project():
    print("\n ---- Create Research Project ----")
    
    title = input("Enter Research Title: ").strip()
    topic = input("Enter Research Topic: ").strip()
    problem_statement = input("Enter problem statement: ").strip()
    
    cursor.execute("""
                   INSERT INTO research_projects
                   (title, topic, problem_statement)
                   VALUES (?, ?, ?)
                   """, (title, topic, problem_statement))
    
    connection.commit()
    print("\nResearch project created successfully")
    
create_research_project()