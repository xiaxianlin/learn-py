class StreamHasher:
    """哈希摘要生成器"""

    def __init__(self, alg="md5", size=4096):
        self.size = size
        alg = alg.lower()
        self.hasher = getattr(__import__("hashlib"), alg.lower())()

    def __call__(self, stream):
        return self.to_digest(stream)

    def to_digest(self, stream):
        """生成十六进制形式的摘要"""
        for buf in iter(lambda: stream.read(self.size), b""):
            self.hasher.update(buf)
        return self.hasher.hexdigest()


def calc_avg():
    """流式计算平均值"""
    total, counter = 0, 0
    avg_value = None
    while True:
        value = yield avg_value
        total, counter = total + value, counter + 1
        avg_value = total / counter


gen = calc_avg()
next(gen)
print(gen.send(10))
print(gen.send(20))
print(gen.send(30))
