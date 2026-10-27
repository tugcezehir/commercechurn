import sys
import os



CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(CURRENT_DIR, 'src')

if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from data_prep import load_and_clean_data
from churn_model import train_churn_model

def main():
    data_path = os.path.join(CURRENT_DIR, "data", "WA_Fn-UseC_-Telco-Customer-Churn.csv")
    
    if not os.path.exists(data_path):
        print(f"\nHATA: Dosya bulunamadı -> {data_path}")
        print("Lütfen CSV dosyasını 'data' klasörü içine eklediğinizden emin olun.")
        return

    df_cleaned = load_and_clean_data(data_path)
    print(" Veri seti başarıyla yüklendi ve işlendi.")
    print(f"İşlenmiş Veri Boyutu: {df_cleaned.shape[0]} Satır, {df_cleaned.shape[1]} Sütun\n")
    

    model = train_churn_model(df_cleaned)
    
   
if __name__ == "__main__":
    main()
