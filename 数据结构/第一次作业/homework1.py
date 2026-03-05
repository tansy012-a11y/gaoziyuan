#=========================作业1-删除元素==================================
from typing import Iterable, Any

class DeleteItem:
    """
    从列表中删除指定索引位置的元素
    核心逻辑：将目标索引后的元素逐个向前移动，最后移除末尾多余位置
    """
    def __init__(self, iterable: Iterable[Any]):
        """
        :param iterable: 可迭代对象，要从中删除元素的列表/可迭代对象
        """
        self.iterable = list(iterable)  # 转换为列表存储，统一操作

    def delete(self, index_to_delete: int) -> list[Any]:
        """
        删除指定索引位置的元素
        
        :param index_to_delete: 要删除的元素的索引
        :return: 删除元素后的新列表
        :raises IndexError: 如果索引超出有效范围，抛出索引异常
        """
        # 先校验索引合法性
        list_length = len(self.iterable)
        if index_to_delete < 0 or index_to_delete >= list_length:
            raise IndexError("删除的索引超出列表有效范围！")
        
        # 核心逻辑：从删除索引的下一位开始，逐个向前移动元素
        # 遍历范围：从删除索引+1 到 列表最后一位，正序遍历
        for i in range(index_to_delete + 1, list_length):
            self.iterable[i - 1] = self.iterable[i]
        
        # 移除末尾多余的最后一个元素（因为前面的元素都前移了，末尾重复了）
        self.iterable.pop()
        
        return self.iterable

# ------------------- 使用示例 -------------------
if __name__ == "__main__":
    # 示例1：删除中间位置的元素（索引2）
    deleter1 = DeleteItem([1, 2, 3, 4, 5])
    result1 = deleter1.delete(2)
    print("示例1 - 删除中间元素：", result1)  # 输出：[1, 2, 4, 5]

    # 示例2：删除开头位置的元素（索引0）
    deleter2 = DeleteItem(["a", "b", "c"])
    result2 = deleter2.delete(0)
    print("示例2 - 删除开头元素：", result2)  # 输出：['b', 'c']

    # 示例3：删除末尾位置的元素（索引3）
    deleter3 = DeleteItem([10, 20, 30, 40])
    result3 = deleter3.delete(3)
    print("示例3 - 删除末尾元素：", result3)  # 输出：[10, 20, 30]



#====课上回顾：插入元素====
from typing import Iterable, Any

class InsertItem:
    """
    向列表中插入元素
    """
    def __init__(self, iterable: Iterable[Any]):
        """
        :param iterable: 可迭代对象，向其内部插入元素
        """
        self.iterable = list(iterable)  # 将输入的可迭代对象转换为列表存储

    def insert(self, element: Any, index_to_insert: int) -> list[Any]:
        """
        向列表中插入元素

        :param element: 要插入的元素
        :param index_to_insert: 插入的索引
        """
        length_of_iterable: int = len(self.iterable)
        # 提前在末尾留一个空位
        self.iterable.append("")
        # 从后往前移动元素
        # 注意，不能颠倒顺序，否则会覆盖原来的元素
        for i in range(length_of_iterable, index_to_insert, -1):
            self.iterable[i] = self.iterable[i - 1]

        self.iterable[index_to_insert] = element
        return self.iterable

# ------------------- 核心使用示例 -------------------
# 1. 创建 InsertItem 实例（传入要操作的列表/可迭代对象）
original_list = [1, 2, 3, 4]
inserter = InsertItem(original_list)  # 实例化，把列表传入类中

# 2. 调用 insert 方法插入元素（参数1：要插入的元素，参数2：插入索引）
# 示例1：在索引2的位置插入99
result1 = inserter.insert(99, 2)
print("示例1 - 中间插入：", result1)  # 输出：[1, 2, 99, 3, 4]

# 示例2：重新创建实例，在开头插入元素（索引0）
inserter2 = InsertItem(["a", "b", "c"])
result2 = inserter2.insert("start", 0)
print("示例2 - 开头插入：", result2)  # 输出：['start', 'a', 'b', 'c']

# 示例3：重新创建实例，在末尾插入元素（索引等于列表长度）
inserter3 = InsertItem([10, 20])
result3 = inserter3.insert(30, 2)
print("示例3 - 末尾插入：", result3)  # 输出：[10, 20, 30]
