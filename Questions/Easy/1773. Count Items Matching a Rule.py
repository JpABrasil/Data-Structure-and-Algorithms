def countItems(items,ruleKey,ruleValue):
    count = 0
    if ruleKey == 'type':
        for i in items:
            if i[0] == ruleValue:
                count +=1
    if ruleKey == 'color':
        for i in items:
            if i[1] == ruleValue:
                count +=1
    if ruleKey == 'name':
        for i in items:
            if i[2] == ruleValue:
                count +=1    
    return count