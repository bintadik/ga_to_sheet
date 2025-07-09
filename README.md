# GA4 to Google Sheet Data Connector

This project provides Python scripts to extract data from Google Analytics 4 (GA4) using its Data API and load it into Google Sheets. It includes utility functions for data retrieval, processing, and Google Sheet interactions.

## Directory Structure

```
.
└── ga_to_gsheet/
    ├── ga_to_gsheet.py
    ├── ga_to_gsheet_next.py
    └── .git/
```

## How It Works

The core functionality involves fetching report data from Google Analytics 4 and pushing it into a specified Google Sheet. The `ga_to_gsheet_next.py` version introduces pagination handling for larger datasets.

```mermaid
graph TD
    A[Start Script Execution] --> B(Load Configuration & Credentials);
    B --> C{Authenticate with Google APIs};
    C -- Credentials --> D[Google Analytics Data API (GA4)];
    C -- Credentials --> E[Google Sheets API];
    D -- Query Parameters --> F[Request GA4 Report Data];
    F -- Raw Response --> G{Process GA4 Response
    (response_to_dataframe)};
    G -- Pandas DataFrame --> H[Prepare Data for GSheet];
    H --> I[Clear Existing GSheet Data
    (clear_report/clear_report_range)];
    I --> J[Update GSheet Worksheet
    (update_report)];
    J --> K(Script Completion);
```

## File Breakdown

### `ga_to_gsheet.py`

This script contains the initial set of functions for interacting with GA4 and Google Sheets. The `ga4_report` function in this version does *not* handle pagination, meaning it might retrieve only a partial dataset if the report size exceeds a single API response limit.

**Functions:**

*   `response_to_dataframe(response)`: Converts a raw GA4 API report response object into a pandas DataFrame, extracting dimension and metric values.
*   `ga4_report(date_range, property_id, dimensions_name, metrics_name, dim_filter, credentials)`: Fetches data from the Google Analytics Data API (GA4) for a specified property, dimensions, metrics, and date range.
*   `clear_report(serv_account, sheet_name, worksheet_name)`: Clears all content from a specific worksheet within a Google Sheet.
*   `update_report(serv_account, sheet_name, worksheet_name, item, pos)`: Updates a cell or range in a Google Sheet worksheet with provided data.
*   `clear_report_range(serv_account, sheet_name, worksheet_name, range)`: Clears content from a specified cell range within a Google Sheet worksheet.

### `ga_to_gsheet_next.py`

This version is an enhancement of `ga_to_gsheet.py`, primarily by introducing pagination logic to the `ga4_report` function, enabling it to retrieve complete datasets that span multiple API responses. It also includes an additional `ga4_report2` function for direct response retrieval without pagination.

**Functions:**

*   `response_to_dataframe(response)`: Converts a raw GA4 API report response object into a pandas DataFrame. (Identical to `ga_to_gsheet.py`)
*   `ga4_report(date_range, property_id, dimensions_name, metrics_name, dim_filter, credentials)`: **Improved** version of `ga4_report` that includes pagination logic to fetch all available data pages from the GA4 API.
*   `ga4_report2(date_range, property_id, dimensions_name, metrics_name, dim_filter, credentials)`: Fetches data from the GA4 API for a specified range without pagination, returning the raw API response object.
*   `clear_report(serv_account, sheet_name, worksheet_name)`: Clears all content from a specific worksheet within a Google Sheet. (Identical to `ga_to_gsheet.py`)
*   `update_report(serv_account, sheet_name, worksheet_name, item, pos)`: Updates a cell or range in a Google Sheet worksheet with provided data. (Identical to `ga_to_gsheet.py`)
*   `clear_report_range(serv_account, sheet_name, worksheet_name, range)`: Clears content from a specified cell range within a Google Sheet worksheet. (Identical to `ga_to_gsheet.py`)