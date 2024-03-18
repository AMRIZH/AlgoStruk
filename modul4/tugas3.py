

def binSe(kumpulan, target):
    # Perform binary search to find the first occurrence of the target
    low = 0
    high = len(kumpulan) - 1

    while low <= high:
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            break
        elif target < kumpulan[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        return []  # Target not found

    # Find all consecutive occurrences of the target
    indices = []
    left = mid
    right = mid

    while left >= 0 and kumpulan[left] == target:
        indices.append(left)
        left -= 1

    while right < len(kumpulan) and kumpulan[right] == target:
        indices.append(right)
        right += 1

    return sorted(indices)
  
kumpulan = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
target = 6
indices = binSe(kumpulan, target)
print(indices)  # Output: [3, 4, 5]


#========================================================

def solveTebakAngka(jumlah, jawaban, kesempatan) :
    low = 0 
    high = jumlah
    while kesempatan > 0 :
        mid = (high+low) // 2
        if mid == jawaban :
            return 1
        elif mid < jawaban :
            high = mid
        else :
            low = mid
    return -1


        