import os
from clickhouse_driver import Client

CLICKHOUSE_HOST = os.environ.get("CLICKHOUSE_HOST", "localhost")
CLICKHOUSE_PORT = os.environ.get("CLICKHOUSE_PORT", "")
CLICKHOUSE_DATABASE = os.environ.get("CLICKHOUSE_DATABASE", "default")
CLICKHOUSE_USER = os.environ.get("CLICKHOUSE_USER", "default")
CLICKHOUSE_PASSWORD = os.environ.get("CLICKHOUSE_PASSWORD", "")
CLICKHOUSE_SECURE = os.environ.get("CLICKHOUSE_SECURE", "False").lower() == "true"

client = Client(
    host=CLICKHOUSE_HOST,
    port=CLICKHOUSE_PORT,
    user=CLICKHOUSE_USER,
    password=CLICKHOUSE_PASSWORD,
    database=CLICKHOUSE_DATABASE,
    secure=CLICKHOUSE_SECURE,
)


def get_database_structure():
    result = ""
    tables = client.execute("SHOW TABLES")
    for table in tables:
        table_name = table[0]
        columns = client.execute(f"DESCRIBE TABLE {table_name}")
        result += f"{table_name} (\n"
        for column in columns:
            result += f"  {column[0]} {column[1]}, \n"
        result += ")\n"
    return result

def run_query(query):
    result = client.execute(query)
    return result