# OUTPUT FORMAT

# print('{}'.format('Merhaba'))
# print('{}'.format(10))

# print("merhaba {} dünyası".format('python'))

# print("merhaba {} {}".format('python','dünyası'))

# strVal = "python"
# print("merhaba {} dünyası".format(strVal))

# strVal1 = "merhaba"
# strVal2 = "python"
# strVal3 = "dünyası"
# print("{} {} {}".format(strVal1,strVal2,strVal3))
# print("{0} {1} {2}".format(strVal1,strVal2,strVal3))
# print("{2} {1} {0} {0}".format(strVal1,strVal2,strVal3))

# print('{:.15}'.format("merhaba python dünyası")) # ilk 15 karakteri yazdırır.

# print('{:^40}'.format("PYTHON"))    # 40 karakterlik yazı oluşturup ^ ile python yazısını ortaya yazdırır.
# print('{:*^40}'.format("PYTHON"))   # boşluklara * yazdırılır.

# print('{:<40}'.format("PYTHON"))    # 40 karakterlik yazı oluşturup ^ ile python yazısını sola yazdırır..
# print('{:*<40}'.format("PYTHON"))   # boşluklara * yazdırılır.

# print('{:>40}'.format("PYTHON"))    # 40 karakterlik yazı oluşturup ^ ile python yazısını sağa yazdırır.
# print('{:*>40}'.format("PYTHON"))   # boşluklara * yazdırılır.

# print('{:d}'.format(10))    # numerik ifadeler yazdırılır.
# print('{:+d}'.format(10))   # başına + yazdırılır.
# print('{:20d}'.format(10))  # soluna boşluk ile 20 karakter yazdırıldı.

# intVal = 123456
# print('{:20d}'.format(intVal))  # soluna boşluk ile 20 karakter yazdırıldı.
# print('{:020d}'.format(intVal)) # boşluklar "0" ile değiştirildi.

# print('{:,d}'.format(intVal))   # basamakları üçer üçer ayırır.
# print('{:_d}'.format(intVal))  # basamakları "-" ile üçer üçer ayırır.

# floatVal= 123.456
# print('{:f}'.format(floatVal))
# print('{:.2f}'.format(floatVal))    # virgülden sonra 2 basamağını yazdırır.
# print('{:10.2f}'.format(floatVal))  # soluna boşluk ile 10 karakter yazdırıldı.
# print('{:010.2f}'.format(floatVal)) # boşluklar "0" ile değiştirildi.