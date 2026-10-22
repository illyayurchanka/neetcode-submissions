class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthSmallest(A: list[int], B: list[int], k) -> int:
            la = len(A)
            lb = len(B)

            if la > lb:
                A, B, la, lb = B, A, lb, la
            
            if la == 0:
                return B[k-1]
            
            if k == 1:
                return min(A[0], B[0])
            
            i = min(la, k//2)
            j = min(lb, k//2)

            if B[j - 1] >= A[i - 1]:
                return getKthSmallest(A[i:], B, k - i)
            elif B[j - 1] < A[i - 1]:
                return getKthSmallest(A, B[j:], k - j)

        la = len(nums1)
        lb = len(nums2)

        left = (la + lb + 1) // 2
        right = (la + lb + 2) // 2
        return (getKthSmallest(nums1, nums2, left) + getKthSmallest(nums1, nums2, right)) / 2.0 