from typing import List, NamedTuple


class Cost(NamedTuple):
    cost: int
    source: str
    target: str


class Solution:
    def minCostToSupplyWater(
        self, n: int, wells: List[int], pipes: List[List[int]]
    ) -> int:
        well_map = {str(well): well for well, _ in enumerate(wells)}
        well_map["WATER"] = len(well_map)
        well_map_inverse = {i: well for well, i in well_map.items()}

        parents = list(range(len(well_map)))
        ranks = [0] * len(parents)

        def find(well: str) -> str:
            well_index = well_map[well]
            if parents[well_index] != well_index:
                parents[well_index] = find(well_map_inverse[parents[well_index]])
            return parents[well_index]

        def union(source: str, target: str) -> bool:
            parent_source = find(source)
            parent_target = find(target)
            if parent_source == parent_target:
                return False

            rank_source = ranks[parent_source]
            rank_target = ranks[parent_target]
            if rank_source > rank_target:
                parents[parent_target] = parent_source
            elif rank_source < rank_target:
                parents[parent_source] = parent_target
            else:
                parents[parent_source] = parent_target
                ranks[parent_target] += 1
            return True

        costs_to_dig_well = [
            Cost(cost, str(well), "WATER") for well, cost in enumerate(wells)
        ]
        costs_to_dig_pipe = [
            Cost(cost, str(house1 - 1), str(house2 - 1))
            for house1, house2, cost in pipes
        ]
        costs = costs_to_dig_well + costs_to_dig_pipe
        costs.sort()

        total_expenditure = 0
        for cost, source, target in costs:
            if union(str(source), str(target)):
                total_expenditure += cost
        return total_expenditure


print(Solution().minCostToSupplyWater(3, wells=[1, 2, 2], pipes=[[1, 2, 1], [2, 3, 1]]))
