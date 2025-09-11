# import fun8
#
# fun8.all_params(1, 2, 3)
# # 1, 2
# # 3, 256

import pakiet

# impotrtuje tylko dozolone rzeczy
# AttributeError: module 'pakiet' has no attribute 'powitanie'
# po dodaniu w __init__.py metoda jest widoczna
pakiet.powitanie()

# można plik z pakietu bezpośrednio zaimportować
from pakiet import fun

fun.powitanie()
# Jestem pakietem

# import jako alias
import pakiet.fun as pk

pk.powitanie()
# Jestem pakietem

# info() nie jet w __init_.py - nie jest widoczna przy podstawowym imporcie
# pakiet.info()
pk.info()
fun.info()
