
# %% IMPORTS
from sys import maxsize

# %% INITIALIZE
blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]

# %% REQUIREMENTS
reqs = ['gym','store','school']

# %% LOGIC
distances=[]
distance_dict={}
min_distance=maxsize
best_block = -1
for index, block in enumerate(blocks):
    # Search current block
    for req in reqs:
        if req in block.keys():
            if block[req]:
                distance_dict[req+'dist'] = 0
            else:
                distance_dict[req+'dist'] = 100
                
    #Traverse Previous blocks
    for previous_block in range(0, index):
        for req in reqs:
            if req in blocks[previous_block].keys():
                if blocks[previous_block][req]:
                    if req+'dist' in distance_dict.keys():
                        if distance_dict[req+'dist'] == 0: 
                            distance = 0
                        elif distance_dict[req+'dist'] == 100:
                            distance = previous_block-index
                        else:
                            distance = max(distance_dict[req+'dist'], previous_block-index)

                        distance_dict[req+'dist'] = distance
    
    #Traverse Next blocks
    for next_block in range(index+1, len(blocks)):
        for req in reqs:
            if req in blocks[next_block].keys():
                if blocks[next_block][req]:
                    if req+'dist' in distance_dict.keys():
                        if distance_dict[req+'dist'] == 0: 
                            distance = 0
                        elif distance_dict[req+'dist'] == 100:
                            distance = index-next_block
                        else:
                            distance = min(distance_dict[req+'dist'], previous_block-index)

                        distance_dict[req+'dist'] = distance

    distances.append(distance_dict.copy())
    
print(distances)
  