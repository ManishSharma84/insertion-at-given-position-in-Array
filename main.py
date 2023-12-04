# insertion at given position
def printar(ary, n):
    for i in range(0, n):
        print(ary[i], end=' ')
    print("\n")


def ins(ary, size, key, pos):
    for i in range(size - 1, pos - 1, -1):
        ary[i + 1] = ary[i]

    ary[pos - 1] = key


def insertE(arr, n, x, pos):
    for i in range(n - 1, pos - 1, -1):
        arr[i + 1] = arr[i]

    arr[pos] = x


# here -1 is for empty space
arr = [1, 2, 3, 4, 5, 6, -1, -1, -1, -1]
k = 9
p = 3
n = 6  # given size of array

print("Before insertion: ")
printar(arr, n)

insertE(arr, n, k, p)

print("After insertion")
n += 1
for i in range(0, n):
    print(arr[i], end=' ')
