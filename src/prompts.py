from src.clickhouse import CLICKHOUSE_DATABASE

def make_prompt(database_structure, user_msg):
    return f"""Here is the database structure:\n\n{database_structure}
The database name is {CLICKHOUSE_DATABASE}
Using ClickHouse database SQL dialect, 
return an SQL statement that answers to this question: {user_msg}
"""


def format_qeury_result(query_result):
    result = ""
    for row in query_result:
        result += " | ".join([str(x) for x in row]) + "\n"
    return result
