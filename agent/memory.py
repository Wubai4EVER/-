from qdrant_client import QdrantClient
from neo4j import GraphDatabase
import timescaleclient

class MemoryStore:
    def __init__(self, qdrant_url, neo4j_uri, tsdb_params):
        self.qdrant = QdrantClient(url=qdrant_url)
        self.graph = GraphDatabase.driver(neo4j_uri, auth=("neo4j", "password"))
        self.tsdb = timescaleclient.connect(**tsdb_params)

    def store_embedding(self, tag, vector):
        self.qdrant.upsert(
            collection_name="embeddings",
            points=[{"id": tag, "vector": vector}]
        )

    def add_relationship(self, from_tag, to_tag, weight=1.0):
        with self.graph.session() as session:
            session.run(
                "MERGE (a:Emotion {name:$a}) "
                "MERGE (b:Emotion {name:$b}) "
                "MERGE (a)-[r:RELATED {weight:$w}]->(b)",
                a=from_tag, b=to_tag, w=weight
            )

    def log_time_series(self, tag, timestamp, value):
        cursor = self.tsdb.cursor()
        cursor.execute(
            "INSERT INTO emotion_timeseries (tag, ts, val) VALUES (%s, %s, %s)",
            (tag, timestamp, value)
        )
        self.tsdb.commit()
