import pandas as pd
import pandas_gbq
import var

def process_messy_data(filename):
    print(f"\n--- 1. READING MESSY DATA: {filename} ---")

    df=pd.read_csv(filename)
    print(df)

    initial_rows = len(df)
    df = df.dropna(subset=['monthly_bill_eur'])
    dropped_rows = initial_rows - len(df)
    print(dropped_rows)

    negative_usage_count = df[df['data_usage_gb'] < 0].shape[0]
    df['data_usage_gb'] = df['data_usage_gb'].abs()
    print(negative_usage_count)

    duplicates_count = df.duplicated().sum()
    df = df.drop_duplicates()

    print(df)
    print('uploading to bigquery')
    destination_table = f"{var.dataset_name}.{var.table_name}"
    pandas_gbq.to_gbq(
        df,
        destination_table,
        project_id=var.project_id,
        if_exists='replace',
    )
    print("Upload Complete")