def intersection(nums1,nums2):
    lista = {}
    lesta =[]
    for i in nums1:
        lista[i] = i
    for j in nums2:
        if j in lista and j not in lesta:
            lesta.append(j)
    
    print(lesta)

intersection([4,9,5],[9,4,9,8,4])