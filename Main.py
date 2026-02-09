from Pandas_ETL import process_messy_data
import Load_BQ
if __name__ == '__main__':
    # 1. Defining the messy file
    local_file_path = r'C:\Users\same1\PycharmProjects\Python+Gcp_Customerbehaviour\vodafone_raw_data.csv'

    csv_filename = 'messy_sales.csv'

    # 2. Running the Cleaning & Uploading Process
    process_messy_data(local_file_path)

    try:
        Load_BQ.load_data_from_gcs(bucket_file_name)
    except Exception as e:
        print(f"Skipping Raw Load (File might not be in bucket): {e}")

    print("--- PIPELINE FINISHED ---")