def flipAndinvertImage(image):
    arr = []
    for i in image:
        arr.append(list(reversed(i)))
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                arr[i][j] = 1
            elif arr[i][j] == 1:
                arr[i][j] = 0
    return arr