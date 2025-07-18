import gradio as gr
from utils.data_processor import load_and_process_csv
from visualizations.charts import generate_spending_chart
from rag.rag_engine import get_financial_advice
from agent.spending_monitor import check_overspending
import pandas as pd


def upload_file(file):
    try:
        df = load_and_process_csv(file)
        return df  # ✅ Directly return DataFrame to Gradio Dataframe component
    except Exception as e:
        # ✅ Return empty DataFrame with column headers on error
        return pd.DataFrame(columns=["transaction_id", "category", "amount", "date", "description"])

def visualize_spending(file):
    df = load_and_process_csv(file)
    chart_path = generate_spending_chart(df)
    return chart_path

def query_advice(query):
    return get_financial_advice(query)

def detect_overspending(file, category):
    df = load_and_process_csv(file)
    return check_overspending(df, category)

# Custom CSS: Gradient Background + Button Styling
custom_css = """
body {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}

.gr-button {
    background: linear-gradient(to right, #4f46e5, #3b82f6);
    color: white;
    border-radius: 8px;
    font-weight: bold;
}

.gr-textbox, .gr-dropdown {
    border-radius: 10px;
}

.gr-image {
    border: 3px solid white;
    border-radius: 15px;
}
"""

# Gradio App Layout
with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("# 💸 **SmartWallet AI**")
    gr.Markdown("An AI-powered budgeting assistant to visualize your spending, detect overspending, and get personalized financial advice.")

    with gr.Row():
        with gr.Column(scale=1):
            file_input = gr.File(label="📁 Upload Spending Data (CSV)")

            category_input = gr.Dropdown(
                choices=["Food", "Transport", "Entertainment", "Shopping"],
                label="Select Category to Monitor"
            )

            btn_chart = gr.Button("📊 Show Spending Chart")
            chart_output = gr.Image()

            btn_chart.click(visualize_spending, inputs=file_input, outputs=chart_output)

            btn_alert = gr.Button("🚨 Check Overspending")
            alert_output = gr.Textbox(label="Overspending Alert", lines=2)

            btn_alert.click(detect_overspending, inputs=[file_input, category_input], outputs=alert_output)

        with gr.Column(scale=1):
            gr.Markdown("### 💬 Ask for Personalized Financial Advice")
            query_input = gr.Textbox(label="Enter Your Question", placeholder="E.g. How can I save on food expenses?")
            btn_advice = gr.Button("💡 Get Advice")
            advice_output = gr.Textbox(label="AI Advice", lines=4)

            btn_advice.click(query_advice, inputs=query_input, outputs=advice_output)

    gr.Markdown("---")
    gr.Markdown("🔍 View your uploaded transactions below.")

    data_table = gr.Dataframe(
    headers=["transaction_id", "category", "amount", "date", "description"],
    label="Transaction Table"
)


    # ✅ CSV Upload connects directly to Table Display:
    file_input.change(upload_file, inputs=file_input, outputs=data_table)

demo.launch()
