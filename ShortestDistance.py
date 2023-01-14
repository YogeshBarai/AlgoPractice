
# %% IMPORTS
from sys import maxsize

blocks = [{'gym': False, 'school': True, 'store': False},
          {'gym': True, 'school': False, 'store': False},
          {'gym': True, 'school': True, 'store': False},
          {'gym': False, 'school': True, 'store': False},
          {'gym': False, 'school': True, 'store': True}]

reqs = ['gym', 'school', 'store']

total_blocks = len(blocks)

min_distance = maxsize
best_block = -1

for current_block_index in range(total_blocks-1):
    for next_block_index in range(current_block_index+1, total_blocks):
        next_block = blocks[next_block_index]
        current_block = blocks[current_block_index]

        dist = 0
        for req in reqs:
            if next_block[req] == current_block[req]:
                dist += 0
            else:
                dist += abs(next_block_index-current_block_index)

        if dist < min_distance:
            min_distance = dist
            best_block = next_block_index

        print(f"\t({current_block_index}, {next_block_index}):\t{dist}")
        print(f"\t({best_block}):\t{min_distance}")

print(f"Best block index: {best_block}")
# %%
