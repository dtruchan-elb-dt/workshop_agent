import sqlite3
from langchain.tools import Tool

conncetion = sqlite3.connect("db.sqlite")

def run_sqlite_query(query):
    c = conncetion.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as err:
        return f"The following error occured:{err}"

# Tool
run_query_tool = Tool.from_function(
    name = "run_sqlite_query",
    description = "Run a sqlite query.",
    func = run_sqlite_query
)