from queue import Queue


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find mid point of combined arrays

        args:
        nums1: List 1
        nums2: List 2

        return:
        res: Float value of the median
        """
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            res = self.findMedian(nums1, nums2, (total_length // 2), False)
        else:
            res = self.findMedian(nums1, nums2, total_length // 2, True)
        return float(res)

    def findMedian(self, list1, list2, center, odd) -> float:
        """
        Read numbers from two lists into a queue until reaching center point. 
        Queue is of length 1 if odd, 2 if even
        If odd, return the center value
        If even, return the mean of the values in the queue
        
        args:
        list1: List 1
        list2: List 2
        center: Number of elements to read in order
        odd: boolean variable to indicate if the sum of the lengths of the lists is odd or even
        
        return:
        res: float
        """
        if odd:
            max_len = 1
        else:
            max_len = 2
        res_q = Queue(max_len)
        i = 0
        idx1, idx2 = 0, 0
        res = 0
        while i <= center:
            if idx1 < len(list1) and idx2 < len(list2):
                if list1[idx1] < list2[idx2]:
                    if res_q.full():
                        res_q.get()
                    res_q.put(list1[idx1])
                    idx1 += 1
                else:
                    if res_q.full():
                        res_q.get()
                    res_q.put(list2[idx2])
                    idx2 += 1
            elif idx1 == len(list1):
                if res_q.full():
                    res_q.get()
                res_q.put(list2[idx2])
                idx2 += 1
            else:
                if res_q.full():
                    res_q.get()
                res_q.put(list1[idx1])
                idx1 += 1
            i += 1
        for _ in range(max_len):
            res += res_q.get()
        return res / max_len

