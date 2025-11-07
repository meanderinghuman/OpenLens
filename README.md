<p align="center">
  <img src="https://github.com/meanderinghuman/OpenLens/blob/main/OpenLens_logo.png" alt="OpenLens Logo" width="350"/>
</p>

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Framework](https://img.shields.io/badge/Framework-TensorFlow%20%7C%20PyTorch-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-ff69b4)
![Status](https://img.shields.io/badge/Status-Active-blueviolet)

> **OpenLens** is an open-source framework that replicates and benchmarks the functionality of **Google Lens** — enabling image-based product retrieval using deep learning and metric-learning models.

---

## 🌐 Overview
OpenLens provides a unified, extensible environment for **evaluating**, **comparing**, and **deploying** visual similarity models such as:
- 🧠 ResNet | EfficientNet | CLIP  
- ⚙️ Siamese | Triplet | Autoencoder  
- ⚡ LSH | FAISS | Hybrid ensembles  

It measures **precision, recall, F1, and inference latency** across models to identify the optimal trade-off between accuracy and efficiency.

---

## 🧭 Features
- 🔍 **Comprehensive Model Benchmarking**
- ⚙️ **Unified Feature Extraction & Search Pipeline**
- ⚡ **FAISS / LSH for Large-Scale Retrieval**
- 📊 **Detailed Metrics & Comparison Reports**
- 🖼️ **Interactive Jupyter Notebook (search.ipynb)**
- 🧩 **Easy Model & Dataset Extension**

---

## 🏗️ Repository Structure
```
├── app.py                              # Main application entry point
├── search.ipynb                        # Interactive notebook for retrieval
├── sample_dataset_creation_kaggle_script.py
├── detailed_metrics_[timestamp].csv    # Per-model detailed metrics
├── model_comparison_results_[timestamp].csv
├── query_results_[timestamp].csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation
```bash
git clone https://github.com/meanderinghuman/OpenLens.git
cd OpenLens
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Usage

### 🖥️ Run the Application
```bash
python app.py
```

### 🧪 Use the Jupyter Notebook
```bash
jupyter notebook
```
Open `search.ipynb` to visualize embeddings and retrieve top-K matches.

---

## 📊 Results Summary
| Model | Precision | Recall | F1 | Latency | Notes |
|:------|:----------:|:------:|:--:|:-------:|:------|
| **ResNet** | ⭐ High | Good | ✅ Balanced | Moderate | Reliable baseline |
| **CLIP** | High | High | ✅ Best Cross-Modal | ⚡ Fastest | Text + Image capable |
| **Triplet/Siamese** | Medium | Good | ✅ Low Latency | ⚡ Fast | Ideal for real-time |
| **Hybrid** | Highest | High | ✅ Top F1 | 🧩 Heavy | Best production reranker |
| **LSH** | Medium | Medium | ⚙️ Scalable | ⚡ Very Fast | Suitable for large datasets |

---

## 🧰 Deployment Recommendations
- **Production / High Traffic** → Hybrid (LSH + ResNet reranking) + caching  
- **Edge / Low-Power** → Quantized EfficientNet or Siamese  
- **Real-Time** → Pre-compute embeddings + Triplet + HNSW index  

---

## 📦 Dataset Format
```
image_id,product_id,category
img_001.jpg,1234,shoes
img_002.jpg,5678,bags
```
- Query → `/data/query/`  
- Gallery → `/data/gallery/`

---

## 🧩 Roadmap
- [ ] Domain fine-tuning for CLIP  
- [ ] Semantic reranking (Vision-Language)  
- [ ] Web Dashboard (Streamlit/Gradio)  
- [ ] Multi-modal Retrieval (Image + Text)  
- [ ] FAISS-HNSW Hybrid Index  

---

## 🧾 License
This project is licensed under the **MIT License** © 2025 Siddharth Pal

---

## 📬 Contact
**Maintainer:** Siddharth Pal  
📧 Email: siddharthpal@live.com  
🔗 LinkedIn: [https://linkedin.com/in/siddharthpal](https://linkedin.com/in/siddharthpal)

---

> “**OpenLens** brings transparency, replicability, and open access to visual search — empowering developers and researchers to build the next generation of intelligent retrieval systems.”
