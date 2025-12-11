import numpy as np
def learn_decision_tree(examples: list[dict], attributes: list[str], target_attr: str) -> dict:

    def mutual_information(A,B,joint_prob) -> float:
        return entropy(A)+entropy(B)-entropy(joint_prob)
    
    def entropy(input:list):
        count={i: input.count(i) for i in input}
        count=count.values()
        pro=np.array([i/sum(count) for i in count])

        def cal(p:np.array):
            p=np.maximum(p,1e-15)
            return np.sum(p*(-np.log(p)))
        return cal(pro)

    res=[j[target_attr] for j in examples]
    if attributes == [] or examples==[]:
        if res.count('Yes')>res.count('No'):
            return 'Yes'
        else:
            return 'No'
    dis={i: [j[i] for j in examples] for i in attributes}
    if all(l=='Yes' for l in res) :
        return 'Yes'
    if all(l=='No' for l in res) :
        return 'No'	
    mutual=[]
    for i in attributes:
        joint=list(zip(dis[i],res))
        mutual.append(mutual_information(dis[i],res,joint))
    k=mutual.index(max(mutual))
    select=attributes[k]
    remaining_attributes = attributes.copy()#
    remaining_attributes.remove(select)
    branch=list(set(dis[select]))
    return {select:{i:learn_decision_tree(list(filter(lambda x: x[select]==i, examples)),remaining_attributes,target_attr) for i in branch}}

print(learn_decision_tree([ {'Outlook': 'Sunny', 'Wind': 'Weak', 'PlayTennis': 'No'},
                            {'Outlook': 'Overcast', 'Wind': 'Strong', 'PlayTennis': 'Yes'}, 
                            {'Outlook': 'Rain', 'Wind': 'Weak', 'PlayTennis': 'Yes'}, 
                            {'Outlook': 'Sunny', 'Wind': 'Strong', 'PlayTennis': 'No'}, 
                            {'Outlook': 'Sunny', 'Wind': 'Weak', 'PlayTennis': 'Yes'}, 
                            {'Outlook': 'Overcast', 'Wind': 'Weak', 'PlayTennis': 'Yes'}, 
                            {'Outlook': 'Rain', 'Wind': 'Strong', 'PlayTennis': 'No'}, 
                            {'Outlook': 'Rain', 'Wind': 'Weak', 'PlayTennis': 'Yes'} ],
                              ['Outlook', 'Wind'], 'PlayTennis'))

{'Outlook': {'Sunny': {'Wind': {'Weak': 'No', 'Strong': 'No'}}, 
             'Rain': {'Wind': {'Weak': 'Yes', 'Strong': 'No'}}, 
             'Overcast': 'Yes'}}