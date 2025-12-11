import numpy as np

def compute_qkv(X,W_q,W_k,W_v):
    return np.matmul(X,W_q),np.matmul(X,W_k),np.matmul(X,W_v)

def self_attention(Q, K, V):
    def softmax(x:np.array):
        x=x-np.max(x,axis=-1,keepdims=True)
        ex=np.exp(x)
        sum=np.sum(ex,axis=-1,keepdims=True)
        return ex/sum
    Qk=np.matmul(Q,K.transpose(0,2,1))
    d=Q.shape[-1]    
    attention_output=np.matmul(softmax(Qk/np.sqrt(d)),V)
    return attention_output

def multi_head_attention(Q, K, V, n_heads):
    m,n=Q.shape
    assert n%n_heads==0
    head_dim=n//n_heads#注意直接/是浮点数
    
    # for 循环访问切片比较低效，这类切片访问一般都可以先升维再降维
    # for i in range(n_heads):
    #     atttntion=self_attention(Q[...,i*head_dim:(i+1)*head_dim],K[...,i*head_dim:(i+1)*head_dim],V[...,i*head_dim:(i+1)*head_dim])
    #     if i==0:
    #         result=atttntion
    #     else:
    #         result=np.concatenate((result,atttntion),axis=-1)

    #并且注意用transpose()调控，pytorch里对应permute()
    Q=Q.reshape(m,n_heads,head_dim).transpose(1,0,2)
    K=K.reshape(m,n_heads,head_dim).transpose(1,0,2)
    V=V.reshape(m,n_heads,head_dim).transpose(1,0,2)

    result=self_attention(Q,K,V)
    result=result.transpose(1,0,2).reshape(m,n)
    return result
    

m, n = 4, 4 
n_heads = 2 
np.random.seed(42) 
X = np.arange(m*n).reshape(m,n) 
X = np.random.permutation(X.flatten()).reshape(m, n) 
W_q = np.random.randint(0,4,size=(n,n)) 
W_k = np.random.randint(0,5,size=(n,n)) 
W_v = np.random.randint(0,6,size=(n,n)) 
Q, K, V = compute_qkv(X, W_q, W_k, W_v) 
print(multi_head_attention(Q, K, V, n_heads))


