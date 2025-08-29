import csv
import pandas as pd
from translator import translate_text

def load_fraud_database():
    #Load fraud database from CSV
    try:
        return pd.read_csv('../data/fraud_database.csv')
    except:
        # Create dummy data if file missing
        data = {
            'phone': ['+919876543210', '+911234567890'],
            'type': ['UPI Scam', 'Fake Loan Offer'],
            'reports': [5, 12]
        }
        return pd.DataFrame(data)

def check_fraud_number(number, lang='en'):
    """Check if number exists in fraud database"""
    df = load_fraud_database()
    result = df[df['phone'] == number]
    
    if not result.empty:
        fraud_type = result.iloc[0]['type']
        reports = result.iloc[0]['reports']
        warning = f"⚠️ HIGH RISK! {reports} fraud reports - {fraud_type}"
        return translate_text(warning, lang) if lang != 'en' else warning
    
    safe_msg = "✅ Number not found in fraud database"
    return translate_text(safe_msg, lang) if lang != 'en' else safe_msg

def add_fraud_entry(number, fraud_type):
    """Add new entry to fraud database"""
    df = load_fraud_database()
    if number in df['phone'].values:
        return "Number already exists in database"
    
    new_entry = pd.DataFrame([{
        'phone': number,
        'type': fraud_type,
        'reports': 1
    }])
    
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv('../data/fraud_database.csv', index=False)
    return "Fraud entry added successfully"
