class Abc:
    def xyz(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])

        return longest


def main():

    s = input("Enter a string containing only '(' and ')': ").strip()

    obj = Abc()
    ans = obj.xyz(s)

    print(f"The longest Valid Parentheses Length is {ans}")


if __name__ == "__main__":
    main()
