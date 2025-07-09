print(f"""
                            ##########################
                            #     IMPORT LIBRARY     #
                            ##########################
""")
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import DateRange
from google.analytics.data_v1beta.types import Dimension
from google.analytics.data_v1beta.types import Metric
from google.analytics.data_v1beta.types import RunReportRequest
from google.analytics.data_v1beta.types import Filter
from google.analytics.data_v1beta.types import FilterExpression
from google.analytics.data_v1beta.types import FilterExpressionList

import os
from collections import defaultdict

import pandas as pd
from datetime import datetime
from datetime import date,timedelta
import numpy as np

from google.oauth2 import service_account
from pandas.io import gbq
import gspread

import warnings
warnings.filterwarnings("ignore")

print(f"""
                            ########################
                            #     DEF FUNCTION     #
                            ########################
""")
def response_to_dataframe(response):
    # Extracting dimension headers
    dimension_headers = [header.name for header in response.dimension_headers]
    
    # Extracting metric headers
    metric_headers = [header.name for header in response.metric_headers]
    
    # Extracting rows
    rows = []
    for row in response.rows:
        dimension_values = [value.value for value in row.dimension_values]
        metric_values = [value.value for value in row.metric_values]
        rows.append(dimension_values + metric_values)
    
    # Constructing DataFrame
    column_names = dimension_headers + metric_headers
    df = pd.DataFrame(rows, columns=column_names)
    return df
def ga4_report(date_range = [], property_id = "", dimensions_name =[],metrics_name  = [],dim_filter = None, credentials = ""):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials
    print(date_range)
    client = BetaAnalyticsDataClient()
    request = RunReportRequest(
        property=f"properties/{property_id}",
        dimensions = [Dimension(name = d_name) for d_name in dimensions_name],
        metrics=[Metric(name = m_name) for m_name in metrics_name],
        date_ranges=[DateRange(start_date=str(date_range[0]), end_date=str(date_range[1]))],
        dimension_filter=dim_filter

    )
    response = client.run_report(request)
    df = response_to_dataframe(response)
    print(df)
    return df
def clear_report(serv_account,sheet_name,worksheet_name):
    sa = gspread.service_account(filename=serv_account)
    sh = sa.open(sheet_name)
    wks = sh.worksheet(worksheet_name)
    wks.clear()

def update_report(serv_account,sheet_name,worksheet_name,item,pos):
    sa = gspread.service_account(filename=serv_account)
    sh = sa.open(sheet_name)
    wks = sh.worksheet(worksheet_name)
    wks.update(pos,item, value_input_option = "USER_ENTERED")

def clear_report_range(serv_account,sheet_name,worksheet_name,range):
    sa = gspread.service_account(filename=serv_account)
    sh = sa.open(sheet_name)
    wks = sh.worksheet(worksheet_name)
    wks.batch_clear(range)