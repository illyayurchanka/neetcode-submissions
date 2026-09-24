class TimeMap:
    def __init__(self):
        self.ds = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.ds[key]
        if len(values) == 0:
            return ""
        l, r = 0, len(values) - 1
        mid = 0
        while l <= r:
            mid = l + (r - l) // 2
            if values[mid][0] == timestamp:
                break
            elif mid < len(values) - 1 and values[mid][0] < timestamp and values[mid + 1][0] > timestamp:
                break
            elif values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return values[mid][1] if values[mid][0] <= timestamp else ""
        
