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
    
if __name__ == '__main__':
    arr1 = sys.argv[1]
    n = int(sys.argv[2])
    arr2 = sys.argv[3]
    m = int(sys.argv[4])
    
    arr1 = [int(data) for data in arr1 if data.isdigit()]
    arr2 = [int(data) for data in arr2 if data.isdigit()]
    
    print(main(arr1, n, arr2, m))