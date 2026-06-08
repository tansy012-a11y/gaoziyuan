import heapq

class MedianFinder:
    def __init__(self):
        # left: 大顶堆(存负数)，存小的一半；right:小顶堆，存大的一半
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # 第一步：选择放入哪个堆
        if not self.left:
            heapq.heappush(self.left, -num)
        else:
            if num <= -self.left[0]:
                heapq.heappush(self.left, -num)
            else:
                heapq.heappush(self.right, num)
        
        # 第二步：平衡两个堆的长度
        len_l = len(self.left)
        len_r = len(self.right)
        # 左边多2个，移一个顶到右边
        if len_l - len_r > 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        # 右边比左边多，移一个顶到左边（保证左边>=右边）
        elif len_r > len_l:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self) -> float:
        len_l = len(self.left)
        len_r = len(self.right)
        # 总数奇数，取左堆顶
        if len_l > len_r:
            return -self.left[0]
        # 偶数取平均
        else:
            return (-self.left[0] + self.right[0]) / 2
mf = MedianFinder()
mf.addNum(3)
print(mf.findMedian())  # 3.0
mf.addNum(1)
print(mf.findMedian())  # 2.0
mf.addNum(4)
print(mf.findMedian())  # 3.0
mf.addNum(1)
print(mf.findMedian())  # 2.0
mf.addNum(5)
print(mf.findMedian())  # 3.0
'''
时间复杂度分析
addNum(num)
堆插入、弹出操作复杂度均为 O(logn)，每次最多两次堆操作：
单次添加时间：O(logn)
findMedian()
只读取两个堆顶元素，无堆调整：O(1)
整体：插入批量操作总复杂度 O(nlogn)，查询常数级。
'''
