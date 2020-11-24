def print_sorted(alg, a):
    print(f"Printing {alg} Sorted Element List...")
    for i in a:
        print(i)


# Counting Sort:
#
# It is a sorting technique based on the keys i.e. objects are collected according to keys which are small integers.
# Counting sort calculates the number of occurrence of objects and stores its key values. New array is formed by adding
# previous key elements and assigning to objects.
#
# Complexity
#
#   Time Complexity: O(n+k) is worst case where n is the number of element and k is the range of input.
#   Space Complexity: O(k) k is the range of input.
#
# Limitation of Counting Sort
#
#     It is effective when range is not greater than number of object.
#     It is not comparison based complexity.
#     It is also used as sub-algorithm for different algorithm.
#     It uses partial hashing technique to count the occurrence.
#     It is also used for negative inputs.
#
# Algorithm
#
#     STEP 1 START
#     STEP 2 Store the input array
#     STEP 3 Count the key values by number of occurrence of object
#     STEP 4 Update the array by adding previous key elements and assigning to objects
#     STEP 5 Sort by replacing the object into new array and key= key-1
#     STEP 6 STOP
# Python program for counting sort

# The main function that sort the given string arr[] in
# alphabetical order
def execute_sort_count(myList):
    maxValue = 0
    for i in range(len(myList)):
        if myList[i] > maxValue:
            maxValue = myList[i]

    buckets = [0] * (maxValue + 1)

    for i in myList:
        buckets[i] += 1

    i = 0
    for j in range(maxValue + 1):
         for a in range(buckets[j]):
             myList[i] = j
             i += 1

    return myList


def execute_sort_count_char(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i - 1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


array_test = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print_sorted("Counting", execute_sort_count(array_test))

########################################################################################################################
# Bubble Sort:
#
# In Bubble sort, Each element of the array is compared with its adjacent element. The algorithm processes
# the list in passes. A list with n elements requires n-1 passes for sorting. Consider an array A of n elements
# whose elements are to be sorted by using Bubble sort. The algorithm processes like following.
#
#     In Pass 1, A[0] is compared with A[1], A[1] is compared with A[2], A[2] is compared with A[3] and so on.
#           At the end of pass 1, the largest element of the list is placed at the highest index of the list.
#     In Pass 2, A[0] is compared with A[1], A[1] is compared with A[2] and so on.
#           At the end of Pass 2 the second largest element of the list is placed at the second highest index of the list.
#     In pass n-1, A[0] is compared with A[1], A[1] is compared with A[2] and so on. At the end of this pass.
#           The smallest element of the list is placed at the first index of the list.
#
# Algorithm :
#
#     Step 1: Repeat Step 2 For i = 0 to N-1
#     Step 2: Repeat For J = i + 1 to N - I
#     Step 3: IF A[J] > A[i]
#     SWAP A[J] and A[i]
#     [END OF INNER LOOP]
#     [END OF OUTER LOOP
#     Step 4: EXIT
#
# Complexity
# Scenario 	Complexity
# Space 	O(1)
# Worst case running time 	O(n2)
# Average case running time 	O(n)
# Best case running time 	O(n2)
def execute_sort_bubble_simple(a):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp


def execute_sort_bubble_best(array):
    n = len(array)

    for i in range(n):

        # Create a flag that will allow the function to

        # terminate early if there's nothing left to sort

        already_sorted = True

        # Start looking at each item of the list one by one,

        # comparing it with its adjacent value. With each

        # iteration, the portion of the array that you look at

        # shrinks because the remaining items have already been

        # sorted.

        for j in range(n - i - 1):

            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its

                # adjacent value, then swap them

                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,

                # set the `already_sorted` flag to `False` so the

                # algorithm doesn't finish prematurely

                already_sorted = False

        # If there were no swaps during the last iteration,

        # the array is already sorted, and you can terminate

        if already_sorted:
            break

    return array


array_test = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
execute_sort_bubble_simple(array_test)
print_sorted("Bubble Simple", array_test)
array_test = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print_sorted("Bubble Best", execute_sort_bubble_best(array_test))


# Printing Sorted Element List . . .
# 7
# 9
# 10
# 12
# 23
# 34
# 34
# 44
# 78
# 101

########################################################################################################################
# Merge sort
#
# Merge sort is the algorithm which follows divide and conquer approach. Consider an array A of n number of elements.
# The algorithm processes the elements in 3 steps.
#
#     If A Contains 0 or 1 elements then it is already sorted, otherwise, Divide A into two sub-array of equal number of elements.
#     Conquer means sort the two sub-arrays recursively using the merge sort.
#     Combine the sub-arrays to form a single final sorted array maintaining the ordering of the array.
#
# The main idea behind merge sort is that, the short list takes less time to be sorted.
# Complexity
# Complexity 	Best case 	Average Case 	Worst Case
# Time Complexity 	O(n log n) 	O(n log n) 	O(n log n)
# Space Complexity 			O(n)
# Example :
#
# Consider the following array of 7 elements. Sort the array by using merge sort.
#
#     A = {10, 5, 2, 23, 45, 21, 7}
#
#
# Merge sort
# Algorithm
#
#     Step 1: [INITIALIZE] SET I = BEG, J = MID + 1, INDEX = 0
#     Step 2: Repeat while (I <= MID) AND (J<=END)
#     IF ARR[I] < ARR[J]
#     SET TEMP[INDEX] = ARR[I]
#     SET I = I + 1
#     ELSE
#     SET TEMP[INDEX] = ARR[J]
#     SET J = J + 1
#     [END OF IF]
#     SET INDEX = INDEX + 1
#     [END OF LOOP]
#     Step 3: [Copy the remaining
#     elements of right sub-array, if
#     any]
#     IF I > MID
#     Repeat while J <= END
#     SET TEMP[INDEX] = ARR[J]
#     SET INDEX = INDEX + 1, SET J = J + 1
#     [END OF LOOP]
#     [Copy the remaining elements of
#     left sub-array, if any]
#     ELSE
#     Repeat while I <= MID
#     SET TEMP[INDEX] = ARR[I]
#     SET INDEX = INDEX + 1, SET I = I + 1
#     [END OF LOOP]
#     [END OF IF]
#     Step 4: [Copy the contents of TEMP back to ARR] SET K = 0
#     Step 5: Repeat while K < INDEX
#     SET ARR[K] = TEMP[K]
#     SET K = K + 1
#     [END OF LOOP]
#     Step 6: Exit
#
# MERGE_SORT(ARR, BEG, END)
#
#     Step 1: IF BEG < END
#     SET MID = (BEG + END)/2
#     CALL MERGE_SORT (ARR, BEG, MID)
#     CALL MERGE_SORT (ARR, MID + 1, END)
#     MERGE (ARR, BEG, MID, END)
#     [END OF IF]
#     Step 2: END
def execute_sort_merge_impl(left, right):
    # If the first array is empty, then nothing needs

    # to be merged, and you can return the second array as the result

    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs

    # to be merged, and you can return the first array as the result

    if len(right) == 0:
        return left

    result = []

    index_left = index_right = 0

    # Now go through both arrays until all the elements

    # make it into the resultant array

    while len(result) < len(left) + len(right):

        # The elements need to be sorted to add them to the

        # resultant array, so you need to decide whether to get

        # the next element from the first or the second array

        if left[index_left] <= right[index_right]:

            result.append(left[index_left])

            index_left += 1

        else:

            result.append(right[index_right])

            index_right += 1

        # If you reach the end of either array, then you can

        # add the remaining elements from the other array to

        # the result and break the loop

        if index_right == len(right):
            result += left[index_left:]

            break

        if index_left == len(left):
            result += right[index_right:]

            break

    return result


def execute_sort_merge(array):
    # If the input array contains fewer than two elements,

    # then return it as the result of the function

    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input

    # into two equal halves, sorting each half and merging them

    # together into the final result

    return execute_sort_merge_impl(

        left=execute_sort_merge(array[:midpoint]),

        right=execute_sort_merge(array[midpoint:]))


array_test = [10, 9, 7, 101, 23, 44, 12, 78, 34, 23]
print_sorted("Merge", execute_sort_merge(array_test))


def most_balanced_partition(parent, files_size):

    def calcWeight(node, adj, files_size):
        q = [node]
        weight = 0
        while q:
            idx = q.pop()
            weight += files_size[idx]
            if idx in adj:
                q.extend(adj[idx])
        return weight

    adj = {}
    edges = []
    for idx, p in enumerate(parent):
        edges.append((p, idx))
        if p in adj:
            adj[p].append(idx)
        else:
            adj[p] = [idx]

    print(adj, edges)
    weight_tot = sum(files_size)
    diff_min = sum(files_size)
    for e in edges:
        p, c = e
        adj[p].remove(c)
        w1 = calcWeight(c, adj, files_size)
        diff_min = min(diff_min, abs(weight_tot - 2 * w1))
        adj[p].append(c)

    return diff_min


parent = [ -1, 0, 1, 2, 1, 0, 5, 2, 0, 0 ]
files_size = [ 8475, 6038, 8072, 7298, 5363, 9732, 3786, 5521, 8295, 6186 ]
print(most_balanced_partition(parent, files_size))
# Sample Output
# 4182
parent = [ -1, 0, 0, 0, 0, 3, 4, 6, 0, 3 ]
files_size = [ 298, 2187, 5054, 266, 1989, 6499, 5450, 2205, 5893, 8095 ]
print(most_balanced_partition(parent, files_size))
# Sample Output
# 8216

def hamilton(G, size, pt, path=[]):
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))
    # loop or dead end, None is implicitly returned


def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    minCnt = 0
    for idx in range(len(job_id)):
        minCnt += abs(crew_id[idx]-job_id[idx])
    return minCnt

crews = [3, 1, 4, 6, 5]
jobs = [9, 8, 3, 15, 1]
print(getMinCost(crews, jobs))
