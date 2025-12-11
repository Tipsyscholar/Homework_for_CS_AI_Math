import numpy as np

baseT=10000.0
def pos_encoding(position: int, d_model: int):
	# Your code here
	if position==0:
		return 0
	if d_model<=0:
		return -1
	
	assert d_model%2==0
	pos=np.array(range(position)).reshape(-1,1)

	feature=np.array(range(d_model//2)).reshape(1,-1)
	feature=pow(baseT,-feature*2/d_model)
	base=np.matmul(pos,feature).reshape(-1,1)
	Sin=np.sin(base)
	Cos=np.cos(base)
	pos_encoding=np.concatenate((Sin,Cos),axis=-1).reshape(1,-1,d_model)

	pos_encoding = np.float16(pos_encoding)
	return pos_encoding

	#更好的是原地实现(分配内存越少越好)


print(pos_encoding(2, 8))
print(pos_encoding(5, 16))  