weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

left = max(weights)
right = sum(weights)
answer = right

while left <= right:
    mid = left + (right - left) // 2

    required_days = 1
    current_weight = 0

    for weight in weights:
        if current_weight + weight <= mid:
            current_weight += weight
        else:
            required_days += 1
            current_weight = weight

    if required_days <= days:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)