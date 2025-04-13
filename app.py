import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBZ4FcsOLlvnJDKyU3pS6UU7WeoyqvooY8")
model = genai.GenerativeModel("models/gemini-1.5-flash")

finance_keywords = [
    "money", "finance", "financial", "investment", "invest", "stock", "stocks", "share",
    "bond", "bonds", "loan", "loans", "bank", "banking","cash","commerce" ,"credit","currency", "debit", "budget",
    "tax", "taxes","economics", "saving", "savings", "interest", "inflation", "account", "accounts",
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

st.set_page_config(page_title="Student Finance Chatbot")

st.title("📚 Student Finance Chatbot")
st.caption("Finance queries only. Ask anything finance-related!")

query = st.text_input("Ask a question")

if query:
    if not any(keyword in query.lower() for keyword in finance_keywords):
        st.warning("Sorry, I can only provide assistance on financial topics!")
    else:
        prompt = f"""
        You are a helpful financial chatbot for students.
        Explain this in simple terms:

        {query}
        """
        try:
            response = model.generate_content(prompt)
            st.success(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
