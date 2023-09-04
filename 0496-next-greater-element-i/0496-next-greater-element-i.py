class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = [-1] * len(nums1)
        nums1index = { n:i for i, n in enumerate(nums1)}
        
        for i in range(len(nums2)):
            if nums2[i] not in nums1index:
                continue
                
            for j in range(i + 1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = nums1index[nums2[i]]
                    res[index] = nums2[j]
                    break
                    
        return res
        
        