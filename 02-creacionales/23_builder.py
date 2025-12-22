class QueryBuilder:
    def __init__(self):
        self.query = ""

    def select(self, table):
        self.query += f"SELECT * FROM {table} "
        return self

    def where(self, condition):
        self.query += f"WHERE {condition} "
        return self

    def order_by(self, field):
        self.query += f"ORDER BY {field} "
        return self

    def build(self):
        return self.query.strip()


# Uso
query = (
    QueryBuilder()
    .select("users")
    .where("age > 18")
    .order_by("name")
    .build()
)

print(query)  
# → SELECT * FROM users WHERE age > 18 ORDER BY name
