# sparting the numbers charcters and spactial sysmbol using re
import re
s="uday1234$&@$12310uday"
res=re.findall('[a-z]',s)
res1= re.findall('[0-9]',s)
res2=re.findall('[$@&]',s)
print(res1)
print(res)
print(res2)
