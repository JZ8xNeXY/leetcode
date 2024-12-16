class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is None:
            self.data = []  # 空のリストとして初期化
        else:
            self.data = value  # 単一の整数として初期化

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.data, int)  # dataが整数ならTrue

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if not self.isInteger():
            self.data.append(elem)  # リストとして動作し、要素を追加
        else:
            # 現在整数を保持している場合、リストに変換して要素を追加
            self.data = [NestedInteger(self.data)]
            self.data.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.data = value  # 単一の整数としてデータを設定

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.data  # 整数を返す
        return None  # リストを保持している場合はNoneを返す

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if not self.isInteger():
            return self.data  # リストを返す
        return None  # 整数を保持している場合はNoneを返す

     # 追加: __str__ メソッド
    def __str__(self):
        if self.isInteger():
            return str(self.data)
        else:
            return f"[{', '.join(map(str, self.data))}]"


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """

        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = ''

        for char in s:
            if char == '[':
                stack.append(NestedInteger())  # 空のリストを作成 スタックに追加
            elif char == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))  # 現在のnum を  に追加
                    num = ''  # num をリセット
                if len(stack) > 1:
                    top = stack.pop()  # スタックの後ろの要素を取り出す
                    stack[-1].add(top)  # スタックの後ろの要素に追加する
            elif char == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))  # スタックの一番後ろに数字を追加
                    num = ''  # numをリセット
            else:
                num += char  # 数字を蓄積

        return stack[0]


s = "[123,[456,[789]]]"
solution = Solution()
print(solution.deserialize(s))
