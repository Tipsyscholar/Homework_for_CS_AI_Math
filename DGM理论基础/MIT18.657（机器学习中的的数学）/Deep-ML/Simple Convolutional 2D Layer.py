import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    padheight=input_height+2*padding
    padweight=input_width+2*padding
    pad=np.zeros((padheight,padweight))
    pad[padding:padding+input_height,padding:padding+input_width]=input_matrix
    output_matrix=np.zeros(((padheight-kernel_height)//stride+1,(padweight-kernel_width)//stride+1))
    for i in range(output_matrix.shape[0]):
        for j in range(output_matrix.shape[1]):
            output_matrix[i,j]=np.sum(kernel*pad[i*stride:i*stride+kernel_height,j*stride:j*stride+kernel_width])



    return output_matrix


input_matrix = np.array([ [1., 2., 3., 4., 5.], [6., 7., 8., 9., 10.], [11., 12., 13., 14., 15.], [16., 17., 18., 19., 20.], [21., 22., 23., 24., 25.], ]) 
kernel = np.array([ [1., 2.], [3., -1.], ]) 
padding, stride = 0, 1 
expected = np.array([ [ 16., 21., 26., 31.], [ 41., 46., 51., 56.], [ 66., 71., 76., 81.], [ 91., 96., 101., 106.], ]) 
output = simple_conv2d(input_matrix, kernel, padding, stride) 
print(output)