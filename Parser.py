import xmltodict
import yaml
import time
t1 = time.time()
output_data = open("ya.yml", "w", encoding="utf-8")
with open("x.xml", encoding="utf-8") as input_data:
    doc = xmltodict.parse(input_data.read())
    line = yaml.dump(doc, allow_unicode=True)
    output_data.write(line)
output_data.close()
print((time.time()-t1)*10)
