import google.generativeai as genai

# Set your API key here
genai.configure(api_key="YOUR APU KEY")

model = genai.GenerativeModel("models/gemini-1.5-flash")

print("📚 Student Finance Chatbot (Finance Only) — type 'exit' to quit")

finance_keywords = [
    "money", "finance", "financial", "investment", "invest", "stock", "stocks", "share",
    "bond", "bonds", "loan", "loans", "bank", "banking", "credit","currency", "debit", "budget",
    "tax", "taxes", "saving", "savings", "interest", "inflation", "account", "accounts",
    "insurance", "mortgage", "debt", "income", "expense", "expenses", "rent", "emi",
    "mutual fund", "mutual funds", "sip", "pension", "retirement", "cryptocurrency",
    "crypto", "bitcoin", "ethereum", "wallet", "payment", "payments", "salary", "wage",
    "earning", "spending", "finance management", "personal finance", "net worth", "assets",
    "liabilities", "revenue", "profit", "loss", "balance sheet", "cash flow", "upstox",
    "zerodha", "nifty", "sensex", "dividend", "broker", "demat", "portfolio", "roth ira",
    "401k", "fd", "fixed deposit", "rd", "recurring deposit", "equity", "trading", "forex",
    "exchange rate", "atm", "withdraw", "transfer", "upi", "gst", "billing", "invoice",
    "tax return", "auditing", "subsidy", "finance tips", "student loan", "education loan",
    "scholarship", "fee", "university fee", "loan repayment", "credit score", "cibil"
]

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    # Check if question is related to finance
    if not any(keyword in query.lower() for keyword in finance_keywords):
        print("\nBot: Sorry, I can only provide assistance on financial topics!")
        continue

    prompt = f"""
    You are a helpful financial chatbot for students.
    Explain this in simple terms:

    {query}
    """

    try:
        response = model.generate_content(prompt)
        print("\nBot:", response.text)
    except Exception as e:
        print("Error:", e)
