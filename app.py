import streamlit as st

# Import your existing logic
from chatbot.data_loader import load_data
from chatbot.intent_router import detect_intent
from chatbot.holdings_engine import count_holdings, performance_by_fund
from chatbot.trades_engine import count_trades
from chatbot.combined_engine import trade_vs_performance
from chatbot.response_generator import generate_response


# -----------------------
# Load data ONCE
# -----------------------
@st.cache_data
def init_data():
    return load_data()

holdings, trades = init_data()


# -----------------------
# Chatbot function
# -----------------------
def chatbot(question: str):
    intent = detect_intent(question)

    if intent == "COUNT_HOLDINGS":
        fund = question.split("for")[-1].strip().lower()
        result = count_holdings(holdings, fund)

        if result <= 0:
            return "Sorry can not find the answer"

        context = f"Total number of holdings for fund '{fund}': {result}"
        return generate_response(context, question)

    if intent == "FUND_PERFORMANCE":
        perf = performance_by_fund(holdings)
        positive_perf = perf[perf > 0]

        if positive_perf.empty:
            return "Sorry can not find the answer"

        context = (
            "Funds ranked by yearly Profit and Loss (PL_YTD):\n\n"
            + positive_perf.to_string()
        )
        return generate_response(context, question)

    if intent == "COUNT_TRADES":
        fund = question.split("for")[-1].strip().lower()
        result = count_trades(trades, fund)

        if result <= 0:
            return "Sorry can not find the answer"

        context = f"Total number of trades for fund '{fund}': {result}"
        return generate_response(context, question)

    if intent == "TRADE_VS_PERFORMANCE":
        table = trade_vs_performance(trades, holdings)

        if table.empty:
            return "Sorry can not find the answer"

        context = (
            "Comparison of trade activity and yearly performance by fund:\n\n"
            + table.to_string()
        )
        return generate_response(context, question)

    return "Sorry can not find the answer"


# -----------------------
# Streamlit UI
# -----------------------
st.set_page_config(page_title="Fund Data Chatbot", layout="centered")

st.title("Fund Analytics Chatbot")
st.write(
    "Ask questions **only related to the provided holdings and trades data**.\n\n"
    "If an answer does not exist, the bot will say:\n"
    "**“Sorry can not find the answer”**"
)

# Example questions
with st.expander("Example questions"):
    st.markdown("""
- Total number of holdings for Garfield  
- Which funds performed better depending on the yearly Profit and Loss of that fund  
- Total number of trades for HoldCo 1  
- Compare trade activity and performance across funds
""")

# Input box
user_question = st.text_input(
    "Enter your question:",
    placeholder="e.g. Which funds performed better depending on the yearly Profit and Loss of that fund"
)

# Submit button
if st.button("Ask"):
    if user_question.strip():
        with st.spinner("Analyzing data..."):
            answer = chatbot(user_question)
        st.subheader("Answer")
        st.text(answer)
    else:
        st.warning("Please enter a question.")
