import pandas as pd

def load_and_process_csv(file_input):
    # Step 1: Read raw CSV correctly
    if hasattr(file_input, 'read'):
        df = pd.read_csv(file_input)
    else:
        df = pd.read_csv(str(file_input))

    # Step 2: Clean column headers
    df.columns = [col.strip() for col in df.columns]

    # Step 3: If only one column detected, treat as corrupted CSV
    if len(df.columns) == 1:
        # Split the single-column values into actual columns
        df = df.iloc[:, 0].str.split(',', expand=True)
        df.columns = ['transaction_id', 'category', 'amount', 'date', 'description']

    # Step 4: Ensure 'amount' is numeric
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # Step 5: Debug print
    print("✅ Final columns:", df.columns.tolist())
    print(df.head())

    return df
