from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        mat_list = [(idx, row.count(1)) for idx, row in enumerate(mat)]
        mat_list = sorted(mat_list, key=lambda x: x[1])

        return [mat_list[i][0] for i in range(k)]
