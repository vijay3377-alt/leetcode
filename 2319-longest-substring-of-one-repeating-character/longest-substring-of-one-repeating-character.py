class Solution(object):

    def longestRepeating(self, s, queryCharacters, queryIndices):

        n = len(s)
        s = list(s)

        size = 4 * n

        left = [0] * size
        right = [0] * size
        best = [0] * size
        first = [''] * size
        last = [''] * size

        def build(node, l, r):

            if l == r:
                left[node] = right[node] = best[node] = 1
                first[node] = last[node] = s[l]
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, l, r, mid)

        def merge(node, l, r, mid):

            a = node * 2
            b = a + 1

            first[node] = first[a]
            last[node] = last[b]

            length1 = mid - l + 1
            length2 = r - mid

            left[node] = left[a]

            if left[a] == length1 and last[a] == first[b]:
                left[node] += left[b]

            right[node] = right[b]

            if right[b] == length2 and last[a] == first[b]:
                right[node] += right[a]

            best[node] = max(best[a], best[b])

            if last[a] == first[b]:
                best[node] = max(
                    best[node],
                    right[a] + left[b]
                )

        def update(node, l, r, idx):

            if l == r:

                left[node] = right[node] = best[node] = 1
                first[node] = last[node] = s[l]

                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx)
            else:
                update(node * 2 + 1, mid + 1, r, idx)

            merge(node, l, r, mid)

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):

            s[idx] = ch

            update(1, 0, n - 1, idx)

            ans.append(best[1])

        return ans