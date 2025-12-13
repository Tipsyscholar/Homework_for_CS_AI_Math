
|标题| 来源|分类|核心idea|(消融)实验与发现|
| :--- | :--- |:--- |:--- |:--- |
|No One-Size-Fits-All Neurons: Task-based  Neurons for Artificial Neural Networks|arxiv|网络架构|使用遗传算法或者张量分解来找多项式，找出最适合的阶数作为动力信息传到网络，保留激活函数，训练微调，可以并行加速，并且泛化友好||
|MULTILINEAR OPERATOR NETWORKS|ICLR 2024|网络架构|除去了非线性激活层，从而可以显式写出来拟合表达式,采用全秩+低秩信息混合:Y = C[(AX) * (BDX) + AX];|ImageNet C测鲁棒性，发现低归纳偏置（处理比较通用，一般是ViT,CNN是高归纳偏置），小数据一般不佳，但是monet也效果好 说明捕捉发现规律的效率很快，捕食者模型ODE推的效果非常好。<br><br>消融实验:（金字塔结构（有效果，节省计算），宽和深，（深更好）空间位移错位交叉（不重要），低秩压缩，（可以压得很大但不影响准确率）|
|Hyper-Compression: Model Compression via Hyperfunction|arxiv|模型压缩|用非有理缠绕让一条线遍历二维单位正方形，用kd树最近邻搜索来记录参数值，这样参数的浮点数就变成了整数，能减少存储比特;<br><br>把参数按照K=2分组，选定a使得尽量密铺，并且分成M组来缩放，可以并行加速|
|An AI-Aided Algorithm for Multivariate Polynomial Reconstruction on Cartesian Grids and the PLG Finite Difference Method|SIAM JSC 2024|高级数据结构与算法|三角格和主格之间用D阶置换群来通信，用部分置换的想法来把问题分解成为顺序操作，从而可以用回溯法来生成一个适定的三角格，以便于对边界进行多项式Lagrange插值，其中回溯的顺序用到了部分置换群;|最小二乘的条件数随膨胀先小后急剧升高|
|A Practical Diffusion Path for Sampling|ICML 2024|生成模型高效采样|使用Dirac分布作为Proposal分布进行卷积路径Annealed Langevin动力学采样，此时$$\nabla \log \mu _{t}(x) = \frac{1}{\sqrt{\lambda _{t}}}\nabla \log \pi\left(\frac{x}{\sqrt{\lambda _{t}}}\right)$$分数可以显式计算(只需对神经网络已拟合得到的score场线性变换即可)，核心优势在于mode覆盖速度很快，分布差异(KL(scipy库KDE拟合),KSD,OT(otto库Sinkorn算法),MMD)降速快|初始分布比较重要，从原点出发初始化，ULA的mode最先坍塌到"1"数字，因其分布与原点的欧氏距离最接近;<br><br>但是其自适应步长会导致分布偏移|
|ADAPTIVE STEPSIZE ALGORITHMS FOR LANGEVIN DYNAMICS|SIAM JSC 2024|生成模型高效采样|||
|Posterior Sampling by Combining Diffusion Models with Annealed Langevin Dynamics|NeurIPS 2025|生成模型高效采样|||
|Adjoint Matching: Fine-tuning Flow and Diffusion Generative Models with Memoryless Stochastic Optimal Control|||||
|DPM-solver: A fast ODE solver for diffusion probabilistic model sampling in around 10 steps|NeurIPS 2022|生成模型高效采样|||
|DPM-solver++: Fast solver for guided sampling of diffusion probabilistic models|arxiv|生成模型高效采样|||
