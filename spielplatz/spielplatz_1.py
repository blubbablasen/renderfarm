class TestClass:
    def __init__(self):
        self.__attr = True

    def get_attr(self):
        return self.__attr

    def set_attr(self, boolean):
        if isinstance(boolean, bool):
            self.__attr = boolean
            return True
        return False


obj = TestClass()


def testfunction(_obj_):
    _obj_(False)
    return


testfunction(obj.set_attr)
print(obj.get_attr())
