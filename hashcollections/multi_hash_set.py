class MultiHashSet:

    INITIAL_BUCKETS_SIZE = 4
    INCREASE_FACTOR = 2

    def __init__(self, payload_factor = 0.75):
        self.buckets = [[] for _ in range(self.INITIAL_BUCKETS_SIZE)]
        self.payload_factor = 0.75
        self.length = 0

    def add(self, new_entry):
        if self.length / len(self.buckets) >= self.payload_factor:
            self._inc_bucket_count()
        mod = hash(new_entry) % len(self.buckets)
        self.buckets[mod].append(new_entry)
        self.length += 1

    def contains(self, item):
        # for bucket in self.buckets:
        #     for element in bucket:
        #         if item == element:
        #             return True

        mod = hash(item) % len(self.buckets)
        return item in self.buckets[mod]

    def _inc_bucket_count(self):
        new_buckets = [[] for _ in range(self.INCREASE_FACTOR * len(self.buckets))]
        for old_bucket in self.buckets:
            for element in old_bucket:
                mod = hash(element) % len(new_buckets)
                new_buckets[mod].append(element)
        self.buckets = new_buckets

    def __contains__(self, item):
        return self.contains(item)



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