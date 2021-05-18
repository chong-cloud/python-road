class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xors = [0]
        count = 0
        for it in arr:
            xors.append(xors[-1] ^ it)
        for i in range(len(arr)-1):
            for k in range(i+1, len(arr)):
                for j in range(i+1, k+1):
                    a = xors[i] ^ xors[j]
                    b = xors[j] ^ xors[k + 1]
                    if a == b:
                        count += 1
        return count




