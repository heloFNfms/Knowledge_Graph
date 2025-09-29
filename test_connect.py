from py2neo import Graph

# 连接到Neo4j数据库
# 使用你设置的新密码替换'your_password'
graph = Graph("bolt://localhost:7687", auth=("neo4j", "WZY216814wzy"))

# 测试连接
result = graph.run("MATCH (n:Person) RETURN n.name as name LIMIT 5")
for record in result:
    print(record["name"])