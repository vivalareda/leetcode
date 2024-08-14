class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = n + m - 1

        while (i >= 0 or j >= 0):
            if (nums1[i] > nums2[j]):
                nums1[k] = nums1[i]
                i-=1
            elif (nums1[j] > nums2[i]):
                nums1[k] = nums2[j]
                j-=1
            k-=1
