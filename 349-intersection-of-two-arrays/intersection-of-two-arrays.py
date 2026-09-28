class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)

        result = []
        i = 0
        j = 0

        while i < n and j < m:

            if nums1[i] == nums2[j]:
                if len(result) == 0 or result[-1] != nums1[i]:
                    result.append(nums1[i])

                i += 1
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return result