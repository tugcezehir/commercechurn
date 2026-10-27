import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    
    df_model = df.copy()
    
   
    cat_cols = df_model.select_dtypes(include=['object', 'category']).columns
    df_model = pd.get_dummies(df_model, columns=cat_cols, drop_first=True)
    
    return df_model

def train_churn_model(df: pd.DataFrame):
   
   
    df_processed = prepare_features(df)
    
    
    X = df_processed.drop('Churn', axis=1)
    y = df_processed['Churn']
    
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
   
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight='balanced', 
        max_depth=10              
    )
    model.fit(X_train, y_train)
    
   
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]
    
   
    print("        MODEL PERFORMANS RAPORU           ")
  
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC Skoru: {roc_auc_score(y_test, y_proba):.4f}")
    
    return model