"""
    - public
    - protected
    - private
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.__cpu = cpu  # private
        self._memory = memory  # protected
        self.hdd = hdd  # public


obj = Computer(2300, 16000, 250000)
print(dir(obj))
print(obj._Computer__cpu)
print(obj._memory)
print(obj.hdd)
