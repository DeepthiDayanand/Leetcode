class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([frequency * c for c, frequency in Counter(s).most_common()])
