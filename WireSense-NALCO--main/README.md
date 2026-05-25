# WireSense – Automated Parameter Tuning for Consistent Wire Grade Production at NALCO

**WireSense** is a comprehensive steel-mill toolkit designed to automate and optimize process parameters to ensure consistent wire-grade production at NALCO’s facilities. Developed as part of the Smart India Hackathon challenge, it leverages machine learning and generative modeling to monitor live operations and predict key material properties.

---

## 🚀 Key Features

* **Live Monitor**
  Real-time sliding-window visualization of incoming process data and on-the-fly prediction of Ultimate Tensile Strength (UTS), Conductivity, and Elongation using pre-trained XGBoost models. 

* **Reverse Predictor**
  Inverse parameter estimation that maps user-defined product specifications back to 16 critical upstream process levers via a PyTorch-based Cycle-GAN generator. 

---

## 🎥 Demonstration & Documentation

## 🎥 Demonstration & Documentation

* 📊 **Project Presentation (PPT/PDF)**: [WireSense%20PPT.pdf`](./WireSense PPT.pdf) – Contains project overview, methodology, implementation, results, and future scope.

* 📄 **Wire Rod Specifications**: [`WIRE_ROD_Specification.pdf`](./WIRE_ROD_Specification.pdf) – Provides industry-standard parameters.

---

## 💻 Getting Started

### Prerequisites

* Python 3.8 or higher
* Git

### Installation

```bash
git clone https://github.com/muskan1712/WireSense--NALCO.git
cd WireSense--NALCO
pip install -r requirements.txt
```

### Launching the Dashboard

```bash
streamlit run main.py
```

Use the **Live Monitor**, **Reverse Predictor**, or **Target Feature Recommender** buttons on the home page to navigate between modules. 

---

## 📂 Repository Structure

```
WireSense-NALCO-/
├── DATA/                         # Raw plant data exports
├── DataSets/                     # Cleaned & training datasets
│   ├── Real_final_Data_With_anomaly.csv
│   └── Training_Dataset.csv
├── Models/                       # Pre-trained model artifacts
│   ├── xgboost_model_output_*.pkl
│   ├── gen_input.pth.tar
│   └── gen_output.pth.tar
├── Properties Predictor/         # Jupyter notebooks for forward-model development
├── Reverse Prediction/           # Notebooks for inverse modeling (Cycle-GAN)
├── Suggestion Optimise Inputs/   # Notebooks for optimization workflows
├── pages/                        # Streamlit app pages
│   ├── 01_Live_Monitor.py
│   ├── 02_Intial_Parameter_Prediction.py
│   └── 03_Target_Feature_Recommender.py
├── main.py                       # Streamlit app entrypoint :contentReference[oaicite:8]{index=8}
├── requirements.txt              # Python dependencies
└── WIRE_ROD_Specification.pdf    # Industry specs
└── WireSense PPT.pdf             # Project presentation
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for enhancements, bug fixes, or new features.

---

## 📄 License

This project currently does not specify a license. Please contact the maintainer for licensing inquiries.

---
<!-- 
**Author**: Shivansh Singhal ([@shivanshsinghal-22](https://github.com/shivanshsinghal-22))

[1]: https://github.com/shivanshsinghal-22/WireSense-NALCO-/tree/main "GitHub - shivanshsinghal-22/WireSense-NALCO-: Automated parameter tuning for consistent wire grade production at NALCO" -->
<!-- [2]: https://raw.githubusercontent.com/shivanshsinghal-22/WireSense-NALCO-/main/pages/01_Live_Monitor.py "raw.githubusercontent.com"
[3]: https://raw.githubusercontent.com/shivanshsinghal-22/WireSense-NALCO-/main/pages/02_Intial_Parameter_Prediction.py "raw.githubusercontent.com"
[4]: https://raw.githubusercontent.com/shivanshsinghal-22/WireSense-NALCO-/main/pages/03_Target_Feature_Recommender.py "raw.githubusercontent.com"
[5]: https://raw.githubusercontent.com/shivanshsinghal-22/WireSense-NALCO-/main/main.py "raw.githubusercontent.com" -->
