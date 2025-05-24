def LIS(arr):
    n = len(arr)
    table = [[arr[i], 1, -1] for i in range(n)]
    max_len = 0

    # 테이블 업데이트 (길이와 이전 인덱스)
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and table[i][1] < table[j][1] + 1:
                table[i][1] = table[j][1] + 1
                table[i][2] = j
        max_len = max(max_len, table[i][1])

    # LIS를 끝내는 모든 인덱스 찾기
    candidates = [i for i in range(n) if table[i][1] == max_len]

    # DFS를 이용하여 모든 LIS 구성
    def dfs(index, path):
        if index == -1:
            results.append(path[::-1])
            return
        prev_index = table[index][2]
        dfs(prev_index, path + [arr[index]])

    results = []
    for i in candidates:
        dfs(i, [])

    return results

# 테스트
input = [10, 22, 9, 33, 21, 50, 41, 60]
output = LIS(input)
print("모든 LIS:")
for seq in output:
    print(seq)
print("길이:", len(output[0]))
