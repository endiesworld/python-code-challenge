import sys

def main(nums1, m, nums2 , n, *args, **kwargs):
    m_pointer = 0
    n_pointer = 0
    container = []

    while((m_pointer < m ) and (n_pointer < n )):
        if nums1[m_pointer] <= nums2[n_pointer]:
            container.append(nums1[m_pointer])
            m_pointer += 1
        else:
            container.append(nums2[n_pointer])
            n_pointer += 1

    if (m_pointer < m ):
        for index in range(m - m_pointer):
            container.append(nums1[m_pointer + index])
    else:
        for index in range(n - n_pointer):
            container.append(nums2[n_pointer + index])
            
    return container


def mergeTwoLists(list1, list2):
        result = []
        counter = 0
        len_1 = len(list1)
        len_2 = len(list2)
        pos_1 = 0
        pos_2 = 0

        for i in range(len_1 + len_2):
            if list1[pos_1] < list2[pos_2]:
                result.append(list1[pos_1])
                pos_1 += 1
            else:
                result.append(list2[pos_2])
                pos_2 += 1
            if (pos_1 == len_1 ):
                while pos_2 < len_2:
                    result.append(list2[pos_2])
                    pos_2 += 1
                break
            if (pos_2 == len_2 ):
                while pos_1 < len_1:
                    result.append(list1[pos_1])
                    pos_1 += 1
                break

        return result

print(mergeTwoLists([1,2,4,5,9,10,11], [1,3,4,7,8,20]))

    
# if __name__ == '__main__':
#     arr1 = sys.argv[1]
#     n = int(sys.argv[2])
#     arr2 = sys.argv[3]
#     m = int(sys.argv[4])
    
#     arr1 = [int(data) for data in arr1 if data.isdigit()]
#     arr2 = [int(data) for data in arr2 if data.isdigit()]
    
#     print(main(arr1, n, arr2, m))