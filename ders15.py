# ENUMERATE VE ZIP

# enumerate: değişkende objeye index tanımlayıp listelerde değişiklik yapmayı sağlar.
# meyvelerList = ['elma', 'armut', 'kavun', 'karpuz']
# for meyve in enumerate(meyvelerList):
#     print(meyve)
#     print(type(meyve))

# for sira, meyve in enumerate(meyvelerList):
#     sira += 1
#     print('{}. sıradaki meyve: {}'.format(sira,meyve)) # 1 eklemeyi "sira+1" yazarakta yapabilirdik.

# zip: iki değişkeni birleştirip aynı anda işlem yapmayı sağlar.
# meyvelerList = ['elma', 'armut', 'kavun', 'karpuz']
# siraList = [1,2,3,4]

# for val in zip(meyvelerList,siraList):
#     print(val)