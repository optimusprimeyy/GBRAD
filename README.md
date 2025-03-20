# GBRAD
Sihan Wang, **Zhong Yuan***, Shitong Cheng, Hongmei Chen, and Dezhong Peng, [Granular-ball computing-based Random Walk for anomaly detection](Paper/2025-GBRAD.pdf), Pattern Recognition, 7 March 2023). (Code)

## Abstract
Anomaly detection is a key task in data mining, which has been successfully employed in many practical scenarios. However, most existing methods usually analyze the anomalous characteristics of samples at a 
single and finest granularity, which leads to high computational cost and low efficiency. As one of the significant mathematical models in the theory of granular computing, granular-ball computing can portray the 
distributional characteristics of data from a multi-granularity perspective. For this reason, this paper proposes an unsupervised anomaly detection method based on granular-ball computing. Firstly, the samples are covered 
by generating adaptive granular-balls, and the multi-granularity information represented by granular-balls with different sizes can reflect the data distribution characteristics of the corresponding region. Secondly, the 
granular-balls are used to fit the samples for constructing a state transfer matrix in Random walk. Then, the steady-state distribution is generated using iterative computation and is normalized as the degree of anomaly 
for each granular-ball. Finally, the anomaly score for each sample is computed by relating the anomaly degree of each granular-ball to the samples it covers. Comparative experiments show that the proposed anomaly 
detection method performs well on multiple datasets, demonstrating its feasibility and superiority in practical applications. The code is publicly available online at [https://github.com/optimusprimeyy/GBRAD](https://github.com/optimusprimeyy/GBRAD).
## Usage
You can run FREAD.py:
```
if __name__ == "__main__":
    load_data = loadmat('FREAD_Example.mat')
    trandata = load_data['trandata']

    scaler = MinMaxScaler()
    trandata[:, 1:] = scaler.fit_transform(trandata[:, 1:])

    delta = 0.5
    out_scores = FREAD(trandata, delta)

    print(out_scores)
```
You can get outputs as follows:
```
out_scores =
    0.8621
    0.9448
    0.8373
    0.8630
    0.8090
    0.8945
```

## Citation
If you find FREAD useful in your research, please consider citing:
```
@article{WANG2023109087,
    title = {Exploiting fuzzy rough entropy to detect anomalies},
    author = {Wang, Si Han and Yuan, Zhong and Luo,Chuan and Chen, Hong Mei and Peng, De Zhong},
    journal = {International Journal of Approximate Reasoning},
    pages = {109087},
    year = {2023},
    doi = {10.1016/j.ijar.2023.109087},
    publisher={Elsevier}
}
```
## Contact
If you have any questions, please contact wangsihan0713@foxmail.com or yuanzhong@scu.edu.cn.

