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
    
def view_research_projects():
    print("\n----- Research Projects -----")
    cursor.execute("""
                   SELECT project_id, title, topic, date_created
                   FROM research_projects
                   ORDER BY project_id DESC
                   """)
    projects = cursor.fetchall()
    
    if not projects:
        print("No Projects found")
        return
    for project in projects:
        print(f"\n Project ID: {project[0]}")
        print(f"\n Project Title: {project[1]}")
        print(f"\n Project Topic: {project[2]}")
        print(f"\n Created on: {project[3]}")
def search_research_projects():
    print("\n ------ Result of Research Projects Search ------")  
    search_term = input("Enter search term (title or topic): ").strip()
    
    cursor.execute("""
                   SELECT project_id, title, topic, date_created
                   FROM research_projects
                   WHERE title LIKE ? OR topic LIKE ?
                   """, (f"%{search_term}%", f"%{search_term}%"))
    
    projects = cursor.fetchall()

    if not projects:
        print("No projects found.")
        return

    for project in projects:
        print(f"\n Project ID: {project[0]}")
        print(f"\n Project Title: {project[1]}")
        print(f"\n Project Topic: {project[2]}")
        print(f"\n Created on: {project[3]}")
        
def edit_research_project():
    print("\n--- Edit Research Project ---")

    project_id = input("Enter project ID to edit: ").strip()

    cursor.execute("""
        SELECT project_id, title, topic, problem_statement
        FROM research_projects
        WHERE project_id = ?
    """, (project_id,))

    project = cursor.fetchone()

    if not project:
        print("Research project not found.")
        return

    print("\nCurrent Information:")
    print(f"Title: {project[1]}")
    print(f"Topic: {project[2]}")
    print(f"Problem Statement: {project[3]}")

    title = input("\nEnter new title (press Enter to keep current): ").strip()
    topic = input("Enter new topic (press Enter to keep current): ").strip()
    problem_statement = input(
        "Enter new problem statement (press Enter to keep current): "
    ).strip()

    title = title if title else project[1]
    topic = topic if topic else project[2]
    problem_statement = (
        problem_statement if problem_statement else project[3]
    )

    cursor.execute("""
        UPDATE research_projects
        SET title = ?,
            topic = ?,
            problem_statement = ?
        WHERE project_id = ?
    """, (title, topic, problem_statement, project_id))

    connection.commit()

    print("\nResearch project updated successfully!")
    
def delete_research_project():
    print("\n--- Delete Research Project ---")

    project_id = input("Enter project ID to delete: ").strip()

    # Check if the project exists
    cursor.execute("""
        SELECT title
        FROM research_projects
        WHERE project_id = ?
    """, (project_id,))

    project = cursor.fetchone()

    if not project:
        print("Research project not found.")
        return

    print(f"\nProject found: {project[0]}")

    confirm = input("Are you sure you want to delete it? (y/n): ").strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    cursor.execute("""
        DELETE FROM research_projects
        WHERE project_id = ?
    """, (project_id,))

    connection.commit()

    print("\nResearch project deleted successfully!")
    

create_research_project()
view_research_projects()
search_research_projects()
edit_research_project()
delete_research_project()