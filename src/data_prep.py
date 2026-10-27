import pandas as pd
import numpy as np

def clean_missing_and_types(df: pd.DataFrame) -> pd.DataFrame:
    
    df_clean = df.copy()
    
    if 'customerID' in df_clean.columns:
        df_clean.drop(columns=['customerID'], inplace=True)
        
    
    if 'TotalCharges' in df_clean.columns:
        df_clean['TotalCharges'] = pd.to_numeric(df_clean['TotalCharges'], errors='coerce')
        # Bos kalan yerleri medyan (ortanca) deger ile doldurma
        median_total = df_clean['TotalCharges'].median()
        df_clean['TotalCharges'] = df_clean['TotalCharges'].fillna(median_total)
        

    replace_cols = ['MultipleLines', 'OnlineSecurity', 'OnlineBackup', 
                    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    for col in replace_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].replace({'No internet service': 'No', 'No phone service': 'No'})
            
    return df_clean


def handle_outliers(df: pd.DataFrame, cols=['MonthlyCharges', 'TotalCharges']) -> pd.DataFrame:
    
    df_out = df.copy()
    for col in cols:
        if col in df_out.columns:
            Q1 = df_out[col].quantile(0.25)
            Q3 = df_out[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Aykiri degerleri alt ve ust sinirlara baskila
            df_out[col] = np.where(df_out[col] < lower_bound, lower_bound, df_out[col])
            df_out[col] = np.where(df_out[col] > upper_bound, upper_bound, df_out[col])
            
    return df_out


def encode_target(df: pd.DataFrame) -> pd.DataFrame:
   
    df_encoded = df.copy()
    if 'Churn' in df_encoded.columns:
        df_encoded['Churn'] = df_encoded['Churn'].map({'Yes': 1, 'No': 0})
    return df_encoded


def load_and_clean_data(file_path: str) -> pd.DataFrame:
   
   
    df = pd.read_csv(file_path)
    
    
    df = clean_missing_and_types(df)
    
  
    df = handle_outliers(df)
    

    df = encode_target(df)
    
    return df