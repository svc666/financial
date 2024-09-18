import streamlit as st

# Function to calculate financial assistance and provide suggestions
def calculate_assistance(income, expenses, savings_goal):
    available_funds = income - expenses
    
    # Initialize advice message
    advice = ""
    
    # Determine financial status
    if available_funds > 0:
        advice = "You have surplus funds. Consider the following options:\n"
        advice += "- Increase your savings by at least 20% of your available funds.\n"
        advice += "- Consider investing in low-cost index funds or a high-yield savings account.\n"
    elif available_funds < 0:
        advice = "You have a deficit. Consider these actions:\n"
        advice += "- Review your expenses and identify areas to cut back.\n"
        advice += "- Look for additional income sources (e.g., freelance work, part-time jobs).\n"
    else:
        advice = "Your income and expenses are balanced. Good job!\n"
    
    # Check if savings goal is achievable
    if available_funds > savings_goal:
        advice += "You can meet your savings goal this month!\n"
        advice += "- Allocate any surplus towards a retirement account or emergency fund.\n"
    else:
        advice += "You may need to adjust your budget to meet your savings goal.\n"
        advice += "- Consider setting a smaller goal or increasing your income.\n"
    
    return advice

# Streamlit user interface
st.title("Financial Assistance Tool")

# User input
income = st.number_input("Enter your income:", min_value=0.0)
expenses = st.number_input("Enter your expenses:", min_value=0.0)
savings_goal = st.number_input("Enter your savings goal:", min_value=0.0)

if st.button("Get Financial Advice"):
    result = calculate_assistance(income, expenses, savings_goal)
    st.text_area("Advice:", result, height=200)
