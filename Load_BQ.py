from google.cloud import bigquery
from google.oauth2 import service_account
import var

def load_data_from_gcs(filename):
    print(f"--- Starting Load Job for {filename} ---")

    # 1. Settingup Authentication using the key file
    credentials = service_account.Credentials.from_service_account_file(var.key_path)
    client = bigquery.Client(credentials=credentials, project=var.project_id)

    # 2. Defining where the file is (The URI)
    uri = f"gs://{var.bucket_name}/{filename}"

    # 3. Configuring the Job (Auto-detect columns, skip header)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE # Overwrite table if exists
    )

    # 4. Defining the Destination Table
    table_ref = f"{var.project_id}.{var.dataset_name}.{var.table_name}"

    # 5. Running the Job
    try:
        load_job = client.load_table_from_uri(
            uri,
            table_ref,
            job_config=job_config
        )
        print(f"Job triggered. Loading data from {uri}...")

        load_job.result()  # here Waits for the job to complete

        print(f"Success! Data loaded into table: {var.table_name}")

    except Exception as e:
        print(f"Error occurred: {e}")