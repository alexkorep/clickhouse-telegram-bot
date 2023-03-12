import os
import clickhouse_connect


CLICKHOUSE_HOST = os.environ.get("CLICKHOUSE_HOST", "localhost")
CLICKHOUSE_PORT = os.environ.get("CLICKHOUSE_PORT", "")
CLICKHOUSE_DATABASE = os.environ.get("CLICKHOUSE_DATABASE", "default")
CLICKHOUSE_USER = os.environ.get("CLICKHOUSE_USER", "default")
CLICKHOUSE_PASSWORD = os.environ.get("CLICKHOUSE_PASSWORD", "")
CLICKHOUSE_SECURE = os.environ.get("CLICKHOUSE_SECURE", "False").lower() == "true"

client = clickhouse_connect.get_client(
    host=CLICKHOUSE_HOST, 
    port=CLICKHOUSE_PORT,
    username=CLICKHOUSE_USER,
    password=CLICKHOUSE_PASSWORD,
    database=CLICKHOUSE_DATABASE,
    secure=CLICKHOUSE_SECURE,
    verify=False)


def get_database_structure():
    result = ""
    tables = client.query("SHOW TABLES")
    for table in tables.result_rows:
        table_name = table[0]
        columns = client.query(f"DESCRIBE TABLE {table_name}")
        result += f"{table_name} (\n"
        for column in columns.result_rows:
            result += f"  {column[0]} {column[1]}, \n"
        result += ")\n"
    return result

def run_query(query):
    # TODO a hack to remove a semicolon at the end of the query
    query = query.replace(";", "")
    result = client.query(query)
    return result.result_rows