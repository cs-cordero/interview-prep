import math
from typing import Iterable, List, Tuple


class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        running_sum = 0
        running_count = 0
        minimum = 1 << 31
        maximum = -1 << 31
        mode = -1
        highest_seen = -1 << 31

        def counts(count: List[int]) -> Iterable[Tuple[int, int]]:
            for i, sample_count in enumerate(count):
                if sample_count > 0:
                    yield i, sample_count

        for i, sample_count in counts(count):
            minimum = min(minimum, i)
            maximum = max(maximum, i)
            running_sum += i * sample_count
            running_count += sample_count
            if highest_seen < sample_count:
                highest_seen = sample_count
                mode = i

        mean = running_sum / running_count

        median = 0
        median_counter = math.ceil(running_count / 2)
        median_requires_midpoint = running_count % 2 == 0

        generator = counts(count)
        while median_counter > 0:
            i, sample_count = next(generator)
            median_counter -= sample_count
        median = i
        if median_requires_midpoint and median_counter == 0:
            j, _ = next(generator)
            median = (i + j) / 2

        return float(minimum), float(maximum), float(mean), float(median), float(mode)
