import sqlite3
from langchain.tools import Tool

conncetion = sqlite3.conncet("db.sqlite")

def run_sqlite_query(query):
    c = conncetion.cursor()
    c.execute(query)
    return c.fetchall()

# Tool
run_query_toool = Tool.from_function(
    name = "run_sqlite_query",
    description = "Run a sqlite query.",
    func = run_sqlite_query
)