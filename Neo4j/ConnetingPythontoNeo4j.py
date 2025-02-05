from neo4j import GraphDatabase

uri = "bolt://localhost:7687"

user = "neo4j"
password = "password"

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result
    
person1 = "CREATE (p:Person {name: 'Alice', age: 30})"
person2 = "CREATE (p:Person {name: 'Bob', age: 25})"
person3 = "CREATE (p:Person {name: 'Charlie', age: 35})"

run_query(person1)
run_query(person2)
run_query(person3)
print("la personne :", person1)##test pour savoir si les données ont bien étaient inserer

##Creer une relation 
relationship1 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) CREATE (a)-[:FRIEND]->(b)"
relationship2 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"
relationship3 = "MATCH (a:Person {name: 'Bob'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"

run_query(relationship1)
run_query(relationship2)
run_query(relationship3)
##print ("La relation 1", relationship1 )
with driver.session() as session:
    query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"
    results = session.run(query_all_persons)
    
    for record in results:
        print(f"Name: {record['p.name']}, Age: {record['p.age']}")


with driver.session() as session:
    def get_friends(tx, name):
        query = """
        MATCH (p:Person {name: $name})-[:FRIEND]->(friend) 
        RETURN friend.name, friend.age
        """
        result = tx.run(query, name=name)
        return list(result)  # Convertir le résultat en liste

    name = "Alice"
    friends = session.execute_read(lambda tx: get_friends(tx, name))

    print(f"Friends of {name}:")
    for record in friends:
        print(f"Name: {record['friend.name']}, Age: {record['friend.age']}")

driver.close()


delete_nodes_and_relationships = "MATCH (n) DETACH DELETE n"
run_query(delete_nodes_and_relationships)