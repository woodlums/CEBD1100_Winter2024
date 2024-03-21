my_dataset = [{'id':0,'name':'The Title' }, {'id':1,'name':' Title2'}]


print(list(filter(lambda i: i["id"] == 1, my_dataset)))

