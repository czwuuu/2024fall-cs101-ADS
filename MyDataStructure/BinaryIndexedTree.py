# binary_indexed_tree
class BIT:
    # initialization
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            index = i + 1
            value = self.arr[i]
            while index < self.n + 1:
                self.bit[index] += value
                index += index & (-index)

    # change arr[index] to value, change self.bit at the same time
    def update(self, index, value):
        index += 1
        while index < self.n + 1:
            self.bit[index] += value - self.arr[index - 1]
            index += index & (-index)
        self.arr[index - 1] = value

    # work out the prefix sum from 1 to length, both edge covered
    def prefix_sum(self, length):
        result = 0
        while length > 0:
            result += self.bit[length]
            length -= length & (-length)
        return result

    # from start to end, both edge covered
    def range_sum(self, start, end):
        return self.prefix_sum(end) - self.prefix_sum(start - 1)

if __name__ == '__main__':
    my_bit = BIT([1, 3, 5, 7, 9, 11])
    print(my_bit.prefix_sum(3))
    print(my_bit.range_sum(3, 5))