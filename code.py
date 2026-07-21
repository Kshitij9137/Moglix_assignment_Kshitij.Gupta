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
    answer = obj.xyz(s)

    print(f"\nThe longest Valid Parentheses Length is {answer}")


if __name__ == "__main__":
    main()
