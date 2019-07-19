class MultiHashSet:

    INITIAL_BUCKETS_SIZE = 4
    INCREASE_FACTOR = 2

    def __init__(self, payload_factor=0.75):
        self.buckets = [[] for _ in range(self.INITIAL_BUCKETS_SIZE)]
        self.payload_factor = payload_factor
        self.length = 0

    def add(self, new_entry):
        if self.length / len(self.buckets) >= self.payload_factor:
            self._inc_bucket_count(len(self.buckets)*self.INCREASE_FACTOR)
        mod = hash(new_entry) % len(self.buckets)
        self.buckets[mod].append(new_entry)
        self.length += 1

    def add_all(self, elements):
        size_after_insertion = self.length + len(elements)
        self._inc_bucket_count(int(size_after_insertion / self.payload_factor) + 1)
        for element in elements:
            self.add(element)

    def clear(self):
        for bucket in self.buckets:
            bucket.clear()
        self.length = 0

    def contains(self, item):
        # for bucket in self.buckets:
        #     for element in bucket:
        #         if item == element:
        #             return True

        mod = hash(item) % len(self.buckets)
        return item in self.buckets[mod]

    def _inc_bucket_count(self, target_bucket_size):
        new_buckets = [[] for _ in range(target_bucket_size)]
        for old_bucket in self.buckets:
            for element in old_bucket:
                mod = hash(element) % len(new_buckets)
                new_buckets[mod].append(element)
        self.buckets = new_buckets

    def __contains__(self, item):
        return self.contains(item)

    def __len__(self):
        return self.length

    def __str__(self):
        result = "{"
        for bucket in self.buckets:
            result += "{"
            for element in bucket:
                result += str(element)
                result += ", "
            if result[-2:-1] == ',':
                result = result[:-2]
            result += "}"
        result += "}"
        return result

    def __hash__(self):
        pass

    def __eq__(self, other):
        this = self._group_elements(self)
        that = self._group_elements(other)

        return this == that

    def _group_elements(self,mhs):
        elements = []
        for bucket in mhs.buckets:
            for element in bucket:
                elements.append(element)
        elements_grouped_by = dict()
        for element in elements:
            if element not in elements_grouped_by:
                elements_grouped_by[element] = 0
            elements_grouped_by[element] += 1
        return elements_grouped_by


if __name__ == '__main__':
    s = MultiHashSet()
    s.add('aaa1')
    s.add('aaa2')
    s.add('aaa3')
    s.add('aaa4')
    s.add('aaa5')
    s.add('aaa6')
    s.add('aaa7')
    s.add('aaa8')
    s.add('aaa9')

    print(s)
    print(s.contains('aaa'))
    print(s.contains('abc'))

    print('bbb' in s)
