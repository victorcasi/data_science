# 📋 Instructions

This example analyzes an undirected network representing the project groups of an XPTO company. The connections between nodes indicate collaboration or reporting relationships between individuals. The network comprises six main projects:

## 📂 Project Overview

- **Department 1 (D1)**: Snopp, Gukrishnan, Leon, Kabutz.  
  Snopp reports to Chapman.

- **Department 2 (D2)**: Oliver, Gotti, Patrick, Zhuo.  
  Oliver reports to Chapman.

- **Department 3 (D3)**: Gotti, Leon, Kabutz.  
  Gotti reports to Chapman.

- **Department 4 (D4)**: Yu reports to Chapman on this project.

- **Department 4a (D4a)**: Polark, Chang, Weng, Angel.  
  Polark reports to Yu.

- **Department 4b (D4B)**: Christoph, Nardo, Gotti, Zhuo.  
  Christoph reports to Yu.

- **Department 4c (D4C)**: Graffe, Zhuo, Hund.  
  Graffe reports to Yu.

### 🎯 Objective

The objective is to conduct a comprehensive analysis of the network metrics and detail insights that may be of interest to the HR director. The director is particularly concerned about Gotti and Chang, as their performance is under market scrutiny.

---

# 🛠️ Solution: Key Metrics Summary

The main metrics obtained are summarized in the table "table_results":

- **Average Connections**: Employees have an average of **3.899 connections**.

- **Weighted Degree**: Chapman has the highest weighted degree, justified by his position as director.

- **Network Diameter**: The largest number of steps (diameter) required to travel between any two points in the network is **5**.

- **Minimum Steps**: The minimum number of steps needed between any two points is **3**.

- **Average Steps**: On average, individuals take **2.5 steps** to connect with others in the network.

- **Closeness of Gotti**: Gotti exhibits high closeness, holding a strategic position that enables quick access to other individuals in the network. He also lies on the paths of several other network members.

- **Position of Chang**: Chang's closeness centrality (CC) is **1**, indicating that his departure from the network would have no significant impact. He is not a strategic employee, similar to Angel and Weng.

- **Role of Yu**: Although not a director, Yu possesses high closeness, allowing him to reach out quickly to others. His betweenness is also high, marking him as a strategic connector. Polark also plays a significant role as an articulation point in the network.

---

🔍 **Software Used**: This analysis was conducted using **Gephi**, a powerful tool for visualizing and analyzing networks.

Feel free to reach out for any questions or additional insights regarding this analysis!
