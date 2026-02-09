# Automated Data Pipeline: Python + Google Cloud + Power BI

## Project Overview
This project is an automated **ETL (Extract, Transform, Load)** pipeline that ingests raw business data, cleans it using Python, and loads it into a **Google BigQuery** data warehouse for analysis.

The pipeline is designed to be **serverless and scalable**, utilizing Google Cloud Platform (GCP) services to handle data storage and warehousing, while **Power BI** is connected for real-time reporting.

## Architecture
**Flow:** `Local CSV` -> `Python (Pandas)` -> `Google Cloud Storage` -> `BigQuery` -> `Power BI`

* **Extraction:** Python scripts ingest raw CSV files (`messy_sales.csv`).
* **Transformation:** **Pandas** performs data cleaning (handling nulls, deduplication, type casting).
* **Loading:** Cleaned data is pushed to **BigQuery** (`customer_data` table).
* **Orchestration:** `Main.py` acts as the controller to trigger the full workflow.

##  Tech Stack
* **Language:** Python 3.9+
* **Libraries:** `pandas`, `pandas-gbq`, `google-cloud-bigquery`, `google-cloud-storage`
* **Cloud:** Google Cloud Platform (GCS, BigQuery, IAM)
* **Visualization:** Microsoft Power BI

##  Project Structure
```text
 Main.py            # The entry point 
 Pandas_ETL.py      # Data cleaning & Upload logic 
 Load_BQ.py         # Raw data loader 
 var.py             # Configuration settings (Project ID, Table Names)
 messy_sales.csv    # Sample dataset (500 rows)
 README.md          # Documentation
