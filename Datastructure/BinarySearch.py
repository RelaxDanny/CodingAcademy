def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence)-1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2 # begin index +rest of items in the sequence // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint_value - 1

        # elif item > midpoint_value:
        else:
            begin_index = midpoint + 1
    return None

sequence_a = [2,4,5,6,7,8,9,12] #must be already sorted
item_a = 12

print(binary_search(sequence_a, item_a),"th position")

