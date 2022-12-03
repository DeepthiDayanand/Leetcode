class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(sorted(s, key=lambda c, freq=Counter(s): (-freq[c],c)))
