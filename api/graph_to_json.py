import pickle
import json

with open('./nfl_graph_4.pkl', 'rb') as f:
    g = pickle.load(f)

id_to_name = {}
name_to_id = {}

for vert_id in g.vert_objs:
    name = g.vert_objs[vert_id].search_name
    id_to_name[vert_id] = name
    if name in name_to_id:
        print("Name: ", name)
        print("Current ID: ", name_to_id[name])
        print("New ID: ", vert_id)
        print("=" * 20)
    name_to_id[name] = vert_id


print(len(id_to_name))
print(len(name_to_id))

with open('./id_to_name.json', 'w') as i2n_f:
    json.dump(id_to_name, i2n_f, indent=2)

with open('./name_to_id.json', 'w') as n2i_f:
    json.dump(name_to_id, n2i_f, indent=2)

# with open('./graph.json', 'w') as graph_f:
#     json.dump(g.vertices, graph_f, indent=2)
#     pass
