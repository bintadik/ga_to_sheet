# GA4 to Google Sheet Reporter

## Description
This Python script automates the extraction of data from Google Analytics 4 (GA4) properties and updates a Google Sheet. It leverages the GA4 Data API to fetch report data, handles pagination for large datasets, processes the data into a Pandas DataFrame, and integrates with Google Sheets for streamlined data storage and reporting.

## Technologies Used
*   Python
*   `google-analytics-data` (for Google Analytics Data API interaction)
*   `pandas` (for data manipulation)
*   `datetime` (for date handling)
*   `numpy` (for numerical operations)
*   `google-oauth2-service-account` (for Google Cloud authentication)
*   `gspread` (for Google Sheets API interaction)

## File Structure

```
.
└── ga_to_gsheet_next.py
```

## How to Run

1.  **Prerequisites**:
    *   Python 3.x installed.
    *   A Google Cloud Project with the Google Analytics Data API and Google Sheets API enabled.
    *   A Service Account with appropriate permissions for GA4 data access and Google Sheet editing. Ensure you have the JSON key file for this service account.

2.  **Installation**:
    Install the required Python packages using pip:
    ```bash
    pip install google-analytics-data pandas gspread google-auth-oauthlib numpy
    ```

3.  **Configuration**:
    *   Within the `ga_to_gsheet_next.py` script, you will need to:
        *   Specify your GA4 `property_id`.
        *   Define the `date_range`, `dimensions_name`, `metrics_name`, and `dim_filter` for your GA4 report.
        *   Provide the path to your Service Account JSON key file for the `credentials` parameter in GA4 functions and `serv_account` parameter in `gspread` functions.
        *   Specify the `sheet_name` and `worksheet_name` for your Google Sheet operations.

4.  **Execution**:
    Run the Python script from your terminal:
    ```bash
    python ga_to_gsheet_next.py
    ```
    *Note: The provided script snippet contains function definitions. You will need to add a main execution block or integrate these functions into your application logic to define and call specific GA4 reports and Google Sheet operations.*

## Flow

```mermaid
graph TD
    A[Start] --> B(Load Google Service Account Credentials);

    subgraph GA4 Data Extraction
        B --> C{Call GA4 Report Function (e.g., ga4_report)};
        C --> D(Define Property ID, Date Range, Dimensions, Metrics);
        D --> E(Apply Optional Dimension Filters);
        E --> F[Execute GA4 Data API Request];
        F --> G{Handle Pagination for Large Reports};
        G --> H[Receive GA4 API Response];
        H --> I[Convert Response to Pandas DataFrame];
    end

    subgraph Google Sheets Operations
        I --> J{Call GSheets Utility Function (e.g., update_report)};
        J --> K(Specify Google Sheet Name and Worksheet Name);
        K --> L[Choose Operation: Clear or Update];
        L -- Clear --> M(Clear Sheet Range via clear_report / clear_report_range);
        L -- Update --> N(Update Sheet with DataFrame Content via update_report);
    end

    M --> O[End];
    N --> O;
```