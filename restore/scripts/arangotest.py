from arango import Arango
from arango.exceptions import DatabaseDeleteError

a = Arango(host="platypi.dev", port=8529)

retrodb_name = "retrospective_test"
iteration_graph_name = "iteration_graph"
iteration_vertex_collection_name = "iteration_vertex"
iteration_edge_collection_name = "iteration_edge"

try:
    a.delete_database(retrodb_name)
except DatabaseDeleteError:
    pass

retrodb = a.create_database(retrodb_name)
iteration_graph = retrodb.create_graph(iteration_graph_name)

iteration_collection = retrodb.create_collection(iteration_vertex_collection_name)
iteration_vertex_collection = iteration_graph.create_vertex_collection(iteration_vertex_collection_name)
iteration_edge_collection = retrodb.create_collection(iteration_edge_collection_name, is_edge=True)
iteration_graph.create_edge_definition(
    edge_collection=iteration_edge_collection_name,
    from_vertex_collections=[iteration_vertex_collection_name],
    to_vertex_collections=[iteration_vertex_collection_name],
)

iteration_ids = [
    "4f5c04c7-793a-443b-9035-9514aa301ef6",
    "6c79a2d7-16cd-4907-88bf-120c89293169",
    "f4207bf3-3afb-46f4-adae-d573deff8e48"
]

iterations = [
    {
        "_key": iteration_ids[0],
        "number": 1,
        "begins": 1459123200,
        "ends": 1459728000
    },
    {
        "_key": iteration_ids[1],
        "number": 2,
        "begins": 1459728000,
        "ends": 1460332800
    },
    {
        "_key": iteration_ids[2],
        "number": 3,
        "begins": 1460332800,
        "ends": 1460937600
    }
]

iteration_edge_ids = [
    "64514b41-abd7-4cf3-9365-2b628593141b",
    "80ad8080-2779-4513-8c9c-76cae28eb424"
]

iteration_edges = [
    {
        "_key": iteration_edge_ids[0],
        "_from": iteration_vertex_collection_name+"/"+iteration_ids[0],
        "_to": iteration_vertex_collection_name+"/"+iteration_ids[1]
    },
    {
        "_key": iteration_edge_ids[1],
        "_from": iteration_vertex_collection_name+"/"+iteration_ids[1],
        "_to": iteration_vertex_collection_name+"/"+iteration_ids[2]
    }
]

def build_batch_operation(operation, collection_name, value):
    return (
        operation,
        [collection_name, value],
        {"wait_for_sync": True}
    )

iteration_vertex_operations = list(map(lambda iteration: build_batch_operation(iteration_graph.create_vertex, iteration_vertex_collection_name, iteration), iterations))

iteration_edge_operations = list(map(lambda edge: build_batch_operation(iteration_graph.create_edge, iteration_edge_collection_name, edge), iteration_edges))

retrodb.execute_batch(iteration_vertex_operations)
retrodb.execute_batch(iteration_edge_operations)
