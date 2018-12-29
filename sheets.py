from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from xlrd import open_workbook
from oauth2client import file, client, tools
import datetime

now = datetime.datetime.now()
flags = tools.argparser.parse_args(args=[])

alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

SAMPLE_SPREADSHEET_ID = '1Xhio1rUviGS_2PvxvrM-UCjkcz2KPFRUd9gaSDkiKto' 
SAMPLE_RANGE_NAME = 'Sheet1!A1:E5'
store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, flags)

SPREADSHEET_ID = '1Xhio1rUviGS_2PvxvrM-UCjkcz2KPFRUd9gaSDkiKto'

class SpreadsheetSnippets(object):
    def __init__(self, service):
        self.service = service

    def create(self, title):
        service = self.service
        spreadsheet = {
            'properties': {
                'title': title
            }
        }
        spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()
        print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
        return spreadsheet.get('spreadsheetId')

    def batch_update(self, spreadsheet_id, title, find, replacement):
        service = self.service
        requests = []
        requests.append({
            'updateSpreadsheetProperties': {
                'properties': {
                    'title': title
                },
                'fields': 'title'
            }
        })
        requests.append({
            'findReplace': {
                'find': find,
                'replacement': replacement,
                'allSheets': True
            }
        })

        body = {
            'requests': requests
        }
        response = service.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=body).execute()
        find_replace_response = response.get('replies')[1].get('findReplace')
        print('{0} replacements made.'.format(
            find_replace_response.get('occurrencesChanged')))
        return response

    def get_values(self, spreadsheet_id, range_name):
        service = self.service
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        numRows = result.get('values') if result.get('values')is not None else 0
        #print('{0} rows retrieved.'.format(numRows))
        return result,numRows

    def batch_get_values(self, spreadsheet_id, _range_names):
        service = self.service
        range_names = [
            # Range names ...
        ]
        range_names = _range_names
        result = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id, ranges=range_names).execute()
        #print('{0} ranges retrieved.'.format(result.get('valueRanges')))
        numRows = result.get('valueRanges')
        return result, numRows

    def update_values(self, spreadsheet_id, range_name, value_input_option,_values):
        service = self.service
        # [START sheets_update_values]
##        values = [
##            [
##                #cell values
##            ],
##            # Additional rows ...
##        ]

        values = _values

        body = {
            'values': values
        }
        
        result = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_name,valueInputOption=value_input_option, body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))
        # [END sheets_update_values]
        return result

    def batch_update_values(self, spreadsheet_id, range_name,
                            value_input_option, _values):
        service = self.service
        values = [
            [
                # Cell values ...
            ],
            # Additional rows
        ]
        values = _values
        data = [
            {
                'range': range_name,
                'values': values
            },
            # Additional ranges to update ...
        ]
        body = {
            'valueInputOption': value_input_option,
            'data': data
        }
        result = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        print('{0} cells updated.'.format(result.get('updatedCells')))
        return result

    def append_values(self, spreadsheet_id, range_name, value_input_option,_values):
        service = self.service
        values = [
            [
                # Cell values ...
            ],
            # Additional rows ...
        ]
        values = _values
        body = {
            'values': values
        }
        result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name,valueInputOption=value_input_option, body=body).execute()
        return result

    def pivot_tables(self, spreadsheet_id):
        service = self.service
        # Create two sheets for our pivot table.
        body = {
            'requests': [{
                'addSheet': {}
            }, {
                'addSheet': {}
            }]
        }
        batch_update_response = service.spreadsheets() \
            .batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        source_sheet_id = batch_update_response.get('replies')[0] \
            .get('addSheet').get('properties').get('sheetId')
        target_sheet_id = batch_update_response.get('replies')[1] \
            .get('addSheet').get('properties').get('sheetId')
        requests = []
        requests.append({
            'updateCells': {
                'rows': {
                    'values': [
                        {
                            'pivotTable': {
                                'source': {
                                    'sheetId': source_sheet_id,
                                    'startRowIndex': 0,
                                    'startColumnIndex': 0,
                                    'endRowIndex': 101,
                                    'endColumnIndex': 8
                                },
                                'rows': [
                                    {
                                        'sourceColumnOffset': 6,
                                        'showTotals': True,
                                        'sortOrder': 'ASCENDING',

                                    },

                                ],
                                'columns': [
                                    {
                                        'sourceColumnOffset': 3,
                                        'sortOrder': 'ASCENDING',
                                        'showTotals': True,

                                    }
                                ],
                                'values': [
                                    {
                                        'summarizeFunction': 'COUNTA',
                                        'sourceColumnOffset': 3
                                    }
                                ],
                                'valueLayout': 'HORIZONTAL'
                            }
                        }
                    ]
                },
                'start': {
                    'sheetId': target_sheet_id,
                    'rowIndex': 0,
                    'columnIndex': 0
                },
                'fields': 'pivotTable'
            }
        })
        body = {
            'requests': requests
        }
        response = service.spreadsheets() \
            .batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        # [END sheets_pivot_tables]
        return response

    def conditional_formatting(self, spreadsheet_id):
        service = self.service

        # [START sheets_conditional_formatting]
        my_range = {
            'sheetId': 0,
            'startRowIndex': 1,
            'endRowIndex': 11,
            'startColumnIndex': 0,
            'endColumnIndex': 4,
        }
        requests = [{
            'addConditionalFormatRule': {
                'rule': {
                    'ranges': [my_range],
                    'booleanRule': {
                        'condition': {
                            'type': 'CUSTOM_FORMULA',
                            'values': [{
                                'userEnteredValue':
                                    '=GT($D2,median($D$2:$D$11))'
                            }]
                        },
                        'format': {
                            'textFormat': {
                                'foregroundColor': {'red': 0.8}
                            }
                        }
                    }
                },
                'index': 0
            }
        }, {
            'addConditionalFormatRule': {
                'rule': {
                    'ranges': [my_range],
                    'booleanRule': {
                        'condition': {
                            'type': 'CUSTOM_FORMULA',
                            'values': [{
                                'userEnteredValue':
                                    '=LT($D2,median($D$2:$D$11))'
                            }]
                        },
                        'format': {
                            'backgroundColor': {
                                'red': 1,
                                'green': 0.4,
                                'blue': 0.4
                            }
                        }
                    }
                },
                'index': 0
            }
        }]
        body = {
            'requests': requests
        }
        response = ""
##        response = service.spreadsheets() \.batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
        return response

def main(name, ID):
    count = 0
    year = now.year
    month = now.month
    day = now.day
    
    date = str(day)+"/"+str(month)+"/"+str(year)
    
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    sp = SpreadsheetSnippets(service)

    value_input_option = 'RAW'
    values = [[date]]
    range_name = 'Sheet1!A1:Z1'
    options = ['a', 'p']
    result, data = sp.get_values(SPREADSHEET_ID, range_name)
##    for doc in data:
##        for d in doc:
##            if d is not None:
##                count+=1
##                range_name = 'Sheet1!'+alpha[count]+'1'
##                sp.update_values(SPREADSHEET_ID, range_name, value_input_option, values)
##                print(range_name)
    range_name = 'Sheet1!A2:A4'
    values = [['p']]
    result, data= sp.get_values(SPREADSHEET_ID, range_name)
    for doc in data:
        for d in doc:
            if d == name:
                range_name = 'Sheet1!B2'
                sp.update_values(SPREADSHEET_ID, range_name, value_input_option, values)


def getdata():
    service = build('sheets', 'v4', http=creds.authorize(Http()))
    sp = SpreadsheetSnippets(service)
    value_input_option = 'RAW'
    range_name = 'Sheet1!A1:Z163'
    result, data = sp.batch_get_values(SPREADSHEET_ID, range_name)
    return data
    
