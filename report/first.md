# AS network 网络性质研究——以 EasyGraph为工具：开题报告
## 1.选题的目的和意义
AS商业关系的准确知识对于互联网的域间结构的技术和经济方面都非常重要。首先，AS关系确定了路由策略，引入了一组非平凡的约束条件，限制了互联网流量可能流过的路径。这对网络的稳健性、流量工程、宏观拓扑测量策略以及其他研究和运营考虑具有重要意义。其次，AS关系的宏观分析不仅可以深入了解当前互联网业务现实的经济基础，还为基于经济模型的互联网拓扑演化提供了一个坚实的验证框架。事实上，互联网AS级别的拓扑结构及其演化动态是互联网参与者做出的业务决策的结果。因此，推断AS关系的能力是了解和建模驱动互联网拓扑结构和层次结构演化的经济力量的有前途的工具。

准确的AS商业关系数据对于许多关注全球互联网性能、稳健性和演化的研究工作至关重要。一些不能忽略AS关系的研究和操作任务包括：

* 实际路径扩张效应建模的真实仿真，此类仿真需要考虑路由策略的影响。
* 理解互联网中的数据包如何路由以及如何通过分析现有的不足来优化互联网路径。
* 开发更可扩展的域间路由协议和架构，如HLP，以考虑AS关系结构来优化其性能。
* 评估AS关系如何影响互联网基础设施的演化，构建基于经济模型的全球互联网增长模型。
* 分析BGP配置场景的各种情况，以开发更具表现力的路由协议和配置语言。
* 推断互联网中的AS路径。
* 建模路由表的结构，并开发合成路由表以进行路由表查找算法的仿真。
* 开发考虑AS关系拓扑特征的更好的拓扑生成器。
* 通过测量现有服务器的流量来源和评估候选数据中心的连接性和AS关系来选择服务器副本的数据中心。
* 基于候选ISP的连通性和AS关系来选择对等点或上游提供商。

## 2.国内外相关研究状况综述（列出相应的参考文献）；

[AS Relationships: Inference and Validation](https://catalog.caida.org/paper/2007_as_relationships_inference/)  
[Inferring AS Relationships: Dead End or Lively Beginning?](https://catalog.caida.org/paper/2005_asrelationships/)  
[Inferring Multilateral Peering](https://catalog.caida.org/paper/2013_inferring_multilateral_peering/)  
[AS Relationships, Customer Cones, and Validation](https://catalog.caida.org/paper/2013_asrank/)  
[Inferring Complex AS Relationships](https://catalog.caida.org/paper/2014_inferring_complex_as_relationships/)  
[IPv6 AS Relationships, Cliques, and Congruence](https://catalog.caida.org/paper/2015_ipv6_as_relationships/)  
[Are We Ready for Metaverse? A Measurement Study of Social Virtual Reality Platforms](https://dl.acm.org/doi/abs/10.1145/3517745.3561417)  



## 3.主要研究内容与基本思路，详细技术路线，并分析可行性、难点和创新点；
### 3.1 研究内容
我的研究将使用CAIDA AS关系网络数据集进行社交网络分析。我将在不同的时间段运行各种社交检测算法，如结构洞检测、社区检测、中心性等。我将跟踪AS关系的趋势，了解某些AS的发展情况，并编写EasyGraph的一些算法。总的来说是以下两点:  
* 使用 EasyGraph 图分析工具，构建基于 CAIDA 给出的 AS-relationships 数据集的关系网络，计算各项社交网络指标，寻找数据规律，深入挖掘并得到有现实意义的洞见。
* 对于 EasyGraph 给出客观评估，并对缺省 / 需要功能进行开发。
### 3.2 难点
* CAIDA 数据集较大，社交网络算法复杂度较高，对机器硬件有要求。
* AS relationship 作为研究内容相关研究较少，可借鉴内容不多。
### 3.3 创新点
* 没人做过 AS relationship 社交网络研究。
* 使用 EasyGraph 进行图分析的研究不多。

## 4.预期成果及形式。
这项研究的预期成果包括：

1. 为AS关系的演化提供全面的了解，包括网络中不同AS之间的联系、其关系的稳定性和演变趋势等，为互联网未来的规划和发展提供基础数据支持。
2. 发掘网络中不同AS之间的潜在合作机会，为商业合作提供新的思路和契机。
3. 通过对社交网络分析的研究，进一步提升EasyGraph的性能和功能，为互联网研究提供更加便捷的工具。

结果分为代码和分析文件。代码含 EasyGraph 开发代码以及数据网络搭建和计算。分析文件为社交网络算法的运算结果，包括图表等。



