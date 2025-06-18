from translator import select_language, translate_text
from doc_generator import generate_bank_form
from fraud_checker import check_fraud_number, add_fraud_entry
import os

# Create directories if missing
os.makedirs('../data', exist_ok=True)
os.makedirs('../generated_docs', exist_ok=True)

def financial_literacy_quiz(lang):
    """Interactive financial literacy quiz"""
    questions = [
        {
            'question': 'What does EMI stand for?',
            'options': ['Easy Monthly Investment', 'Equated Monthly Installment', 'Electronic Money Transfer'],
            'answer': 1
        },
        {
            'question': 'What is the minimum balance in Jan Dhan account?',
            'options': ['₹1000', '₹500', 'Zero balance'],
            'answer': 2
        }
    ]
    
    score = 0
    for i, q in enumerate(questions):
        # Translate question and options
        question = translate_text(q['question'], lang) if lang != 'en' else q['question']
        options = [translate_text(opt, lang) if lang != 'en' else opt for opt in q['options']]
        
        print(f"\nQ{i+1}: {question}")
        for idx, opt in enumerate(options):
            print(f"{idx+1}. {opt}")
            
        while True:
            try:
                choice = int(input("Your answer: ")) - 1
                if 0 <= choice < len(options):
                    break
                print("Invalid choice!")
            except ValueError:
                print("Enter a number")
        
        if choice == q['answer']:
            score += 1
            print(translate_text("✅ Correct!", lang))
        else:
            correct = options[q['answer']]
            print(translate_text(f"❌ Wrong! Correct answer: {correct}", lang))
    
    print(translate_text(f"\nYour score: {score}/{len(questions)}", lang))
    return score

def main():
    print("="*60)
    print(translate_text("वित्त सहायता - वर्नाक्युलर बैंकिंग सहायक", 'hi'))
    print("="*60)
    
    lang = select_language()
    
    while True:
        print("\n" + "="*50)
        print(translate_text("MAIN MENU", lang))
        print("1. " + translate_text("Generate Bank Form", lang))
        print("2. " + translate_text("Check Fraud Number", lang))
        print("3. " + translate_text("Report Fraud Number", lang))
        print("4. " + translate_text("Financial Literacy Quiz", lang))
        print("5. " + translate_text("Exit", lang))
        
        choice = input(translate_text("Enter choice: ", lang))
        
        if choice == '1':
            # Document generation
            print("\n" + translate_text("Available Schemes:", lang))
            print("1. PM Jan Dhan Yojana")
            print("2. Mudra Loan")
            print("3. Kisan Credit Card")
            
            scheme_choice = input(translate_text("Select scheme: ", lang))
            schemes = {'1': 'pmjdy', '2': 'mudra', '3': 'kcc'}
            scheme = schemes.get(scheme_choice)
            
            if scheme:
                user_data = {}
                print(translate_text("\nEnter your details:", lang))
                user_data['Name'] = input(translate_text("Full Name: ", lang))
                user_data['Aadhaar Number'] = input(translate_text("Aadhaar Number: ", lang))
                user_data['Mobile Number'] = input(translate_text("Mobile Number: ", lang))
                
                result = generate_bank_form(scheme, user_data, lang)
                print(translate_text(result, lang))
            else:
                print(translate_text("Invalid scheme choice", lang))
                
        elif choice == '2':
            # Fraud check
            number = input(translate_text("\nEnter phone number to check: +91", lang))
            result = check_fraud_number(f"+91{number}", lang)
            print(result)
            
        elif choice == '3':
            # Report fraud
            number = input(translate_text("\nEnter fraud phone number: +91", lang))
            fraud_type = input(translate_text("Fraud type (UPI Scam/Fake Loan/Impersonation): ", lang))
            result = add_fraud_entry(f"+91{number}", fraud_type)
            print(translate_text(result, lang))
            
        elif choice == '4':
            # Financial quiz
            financial_literacy_quiz(lang)
            
        elif choice == '5':
            print(translate_text("\nधन्यवाद! आपका दिन शुभ हो!", lang))
            break
            
        else:
            print(translate_text("Invalid choice! Please try again.", lang))

if __name__ == "__main__":
    main()