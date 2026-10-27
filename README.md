# 🛒 E-Commerce Customer Churn Analysis

Python ve makine öğrenmesi kullanarak e-ticaret platformlarındaki müşteri kaybını (churn) tahminleyen veri bilimi projesi.

---

## 📊 Model Performans Raporu

* **İşlenen Veri Boyutu:** 7,043 Satır, 20 Sütun
* **Genel Doğruluk (Accuracy):** `%76` (0.76)
* **ROC-AUC Skoru:** `0.8399`

### Sınıflandırma Metrikleri (Classification Report)

| Sınıf / Metrik | Precision (Kesinlik) | Recall (Duyarlılık) | F1-Score | Support (Destek) |
| :--- | :---: | :---: | :---: | :---: |
| **Sınıf 0** (Aktif Müşteri) | 0.90 | 0.75 | 0.82 | 1035 |
| **Sınıf 1** (Churn / Ayrılan) | 0.53 | 0.76 | 0.62 | 374 |
| **Macro Average** | 0.71 | 0.76 | 0.72 | 1409 |
| **Weighted Average** | 0.80 | 0.76 | 0.77 | 1409 |