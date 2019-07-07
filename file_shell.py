#xls,xlsx
import csv

#user xlrd ,xlsxwriter
import xlsxwriter
import json
import collections

def check_row_clo(x,y,format):
    format=format['map']
    print(format)
    for row in format.keys():
        if __check_cell__(x,row) and __check_cell__(y,format[row]):
            return True
    return False

def __check_cell__(x,string):
    x=str(x)
    if string=='*':
        return True
    else:
        strs=string.split(',')
        if x in strs:
            return True
        else :
            for area in [ar for ar in strs if ':' in ar]:
                a0=area.split(':')[0].upper()
                a1=area.split(':')[1].upper()
                if a0<=x.upper() and a1>=x.upper() and len(a0)<=len(x) and len(a1)>=len(x):
                    return True
    return False

class format_class():
    def __init__(format_dict):
        __self__.format=format_dict['format']
        __self__.map=collections.Counter()
        for rows in format_dict['map']:
            pass
            

def writer_csv(filename,data,modem='w',headers=None):
    with open(filename,modem,newline='') as f:
        csv_write=csv.writer(f)
        if headers:
            csv_write.writerow(headers)
        csv_write.writerows(data)

def read_csv(path):
    with open(path) as f:
        return list(csv.reader(f))
def write_excel_simple(worksheet,data):
    for row in range(len(data)):
        for col in range(len(data[0])):
            data[row][col]=try_cast_number(data[row][col])
            worksheet.write(row, col,  data[row][col])


def read_excel_from_json(workbooh,json_path):
    # Format=collections.namedtuple({'format':{'format':'mat','map':'index'}})
    # Format()

    with open(json_path,'r+' ,encoding='utf-8')as f:
        js=json.load(f)
        js_keys=js.keys()
        if 'sheet_name' in js_keys:
            sheet=workbooh.add_worksheet(js['sheet_name'])
            
        else:
            sheet=workbooh.add_worksheet()
        if 'data' in js_keys:
            data=read_csv(js['data'])
        else:
            data=None
        if 'format' in js_keys:
            formats=js['format']
        else:
            formats=None
        writer_cxcel_from_json(sheet,data,formats,workbooh)
def writer_cxcel_from_json(worksheet,data,formats,workbook):
    # for the_format in  formats.keys():
    #     formats[the_format]['format']=workbook.add_format(formats[the_format]['format'])
    for row in range(len(data)):
        for col in range(len(data[0])):
            dict_add={}
            for the_format in  formats.keys():
                if check_row_clo(row,col, formats[the_format]):
                    print({**formats[the_format]['format'],**dict_add})
                    dict_add={**formats[the_format]['format'],**dict_add}
            
            data[row][col]=try_cast_number(data[row][col])
            worksheet.write(row, col,  data[row][col],workbook.add_format(dict_add))
workbooh=xlsxwriter.Workbook('headers_footers.xlsx')
read_excel_from_json(workbooh,'test.json')
workbooh.close()
        



def map_row_to_int(raw_string):
    if type(try_cast_number[ raw_string]) in [int,float]:
        return  try_cast_number(raw_string)
    else:
        k=0
        num_raw=0
        len(raw_string)
        for i in raw_string:
            n=(''.join([chr(i)  for i in range(ord('a'),ord('z')+1)]).find(i.lower())+1)
            num_raw =n+k*num_raw*26
            k=k+1
            if n==0:
                raise ValueError('raw_error in json or other')
        return num_raw
def int_to_map_row(raw_int):
    w_str=[chr(i)  for i in range(ord('a'),ord('z')+1)]
    w_str_up=[chr(i)  for i in range(ord('A'),ord('Z')+1)]
    if isinstance( raw_int,str):
        if set(raw_int.lower())<set(w_str+w_str_up):
            return raw_int.upper()
        else:
            raise TypeError('row error a-z/A-Z')
    else:
        re_str=[]
        
        while raw_int!=1:
            re_str.append(raw_int%26)
            raw_int=int(raw_int/26)+1
        print(re_str)
        re_str.reverse()
        for i in range(len(re_str)):
            if re_str[i]==0:
                re_str[i]=w_str_up[ -1]
            else:
                re_str[i]=w_str_up[ re_str[i]-1]
        return ''.join(re_str)



import configparser
conf=configparser.ConfigParser()
conf.read('Expenses01.ini')
Workbook_name=conf['main']['name']
data_name=conf['main']['data']
print(Workbook_name)
print(conf.sections())
def main():
    workbook = xlsxwriter.Workbook(Workbook_name)
    if len(conf.sections())==1:
        worksheet = workbook.add_worksheet()
        write_excel_simple(worksheet,read_csv(data_name))
    else:
        pass
    workbook.close()


def try_cast_number(string):
    if isinstance(string,int):
        return int(str)
    elif isinstance(string,float):
        return float
    else:
        try:
            int(string)
        except BaseException as e:
            try:
                float(string)
            except BaseException as e:
                return string
            else:
                return float(string)
        else:
            return(int(string))

float('2.4')
expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
    ['Total','=SUM(B1:B4)']
)
import os
writer_csv('Expenses01.csv',expenses)

def openxls(xls_path, sheet=None):
    work_book=xlsxwriter.Workbook(xls_path)

    worksheet = work_book.add_worksheet()
    if sheet:
        if type(sheet) is int:
            for _ in range(sheet-1):
                worksheet = work_book.add_worksheet()
            worksheet = work_book.add_worksheet()
        else:
            worksheet = work_book.add_worksheet(sheet)
    else:
        worksheet=work_book.sh











def test1():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()

    # Some data we want to write to the worksheet.
    expenses = (
        ['Rent', 1000],
        ['Gas',   100],
        ['Food',  300],
        ['Gym',    50],
    )

    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0

    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
        worksheet.write(row, col,     item)
        worksheet.write(row, col + 1, cost)
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')

    workbook.close()
def test2():
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Expenses02.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Add a number format for cells with money.
    money = workbook.add_format({'num_format': '$#,##0'})

    # Write some data headers.
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)

    # Some data we want to write to the worksheet.
    expenses = (
        ['Rent', 1000],
        ['Gas',   100],
        ['Food',  300],
        ['Gym',    50],
    )

    # Start from the first cell below the headers.
    row = 1
    col = 0

    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
        worksheet.write(row, col,     item)
        worksheet.write(row, col + 1, cost, money)
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total',       bold)
    worksheet.write(row, 1, '=SUM(B2:B5)', money)

    workbook.close()




from datetime import datetime

def test3():
    # Create a workbook and add a worksheet.
    # write_string()
    # write_number()
    # write_blank()
    # write_formula()
    # write_datetime()
    # write_boolean()
    # write_url()
    workbook = xlsxwriter.Workbook('Expenses03.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # Add a number format for cells with money.
    money_format = workbook.add_format({'num_format': '$#,##0'})

    # Add an Excel date format.
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})

    # Adjust the column width.
    worksheet.set_column(1, 1, 15)

    # Write some data headers.
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Date', bold)
    worksheet.write('C1', 'Cost', bold)

    # Some data we want to write to the worksheet.
    expenses = (
        ['Rent', '2013-01-13', 1000],
        ['Gas',  '2013-01-14',  100],
        ['Food', '2013-01-16',  300],
        ['Gym',  '2013-01-20',   50],
    )

    # Start from the first cell below the headers.
    row = 1
    col = 0

    for item, date_str, cost in (expenses):
        # Convert the date string into a datetime object.
        date = datetime.strptime(date_str, "%Y-%m-%d")

        worksheet.write_string  (row, col,     item              )
        worksheet.write_datetime(row, col + 1, date, date_format )
        worksheet.write_number  (row, col + 2, cost, money_format)
        row += 1

    # Write a total using a formula.
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 2, '=SUM(C2:C5)', money_format)

    workbook.close()

# constant_memory: Reduces the amount of data stored in memory so that large files can be written efficiently:
# workbook = xlsxwriter.Workbook(filename, {'constant_memory': True})
# Note, in this mode a row of data is written and then discarded when a cell in a new row is added via one of the worksheet write_() methods. Therefore, once this mode is active, data should be written in sequential row order. For this reason the add_table() and merge_range() Worksheet methods don’t work in this mode.
# See Working with Memory and Performance for more details.
# tmpdir: XlsxWriter stores workbook data in temporary files prior to assembling the final XLSX file. The temporary files are created in the system’s temp directory. If the default temporary directory isn’t accessible to your application, or doesn’t contain enough space, you can specify an alternative location using the tmpdir option:
# workbook = xlsxwriter.Workbook(filename, {'tmpdir': '/home/user/tmp'})
# The temporary directory must exist and will not be created.
# in_memory: To avoid the use of temporary files in the assembly of the final XLSX file, for example on servers that don’t allow temp files such as the Google APP Engine, set the in_memory constructor option to True:
# workbook = xlsxwriter.Workbook(filename, {'in_memory': True})
# This option overrides the constant_memory option.
# strings_to_numbers: Enable the worksheet.write() method to convert strings to numbers, where possible, using float() in order to avoid an Excel warning about “Numbers Stored as Text”. The default is False. To enable this option use:
# workbook = xlsxwriter.Workbook(filename, {'strings_to_numbers': True})
# strings_to_formulas: Enable the worksheet.write() method to convert strings to formulas. The default is True. To disable this option use:
# workbook = xlsxwriter.Workbook(filename, {'strings_to_formulas': False})
# strings_to_urls: Enable the worksheet.write() method to convert strings to urls. The default is True. To disable this option use:
# workbook = xlsxwriter.Workbook(filename, {'strings_to_urls': False})
# nan_inf_to_errors: Enable the worksheet.write() and write_number() methods to convert nan, inf and -inf to Excel errors. Excel doesn’t handle NAN/INF as numbers so as a workaround they are mapped to formulas that yield the error codes #NUM! and #DIV/0!. The default is False. To enable this option use:
# workbook = xlsxwriter.Workbook(filename, {'nan_inf_to_errors': True})
# default_date_format: This option is used to specify a default date format string for use with the worksheet.write_datetime() method when an explicit format isn’t given. See Working with Dates and Time for more details:
# xlsxwriter.Workbook(filename, {'default_date_format': 'dd/mm/yy'})
# remove_timezone: Excel doesn’t support timezones in datetimes/times so there isn’t any fail-safe way that XlsxWriter can map a Python timezone aware datetime into an Excel datetime in functions such as write_datetime(). As such the user should convert and remove the timezones in some way that makes sense according to their requirements. Alternatively the remove_timezone option can be used to strip the timezone from datetime values. The default is False. To enable this option use:
# workbook = xlsxwriter.Workbook(filename, {'remove_timezone': True})
# See also Timezone Handling in XlsxWriter.
# date_1904: Excel for Windows uses a default epoch of 1900 and Excel for Mac uses an epoch of 1904. However, Excel on either platform will convert automatically between one system and the other. XlsxWriter stores dates in the 1900 format by default. If you wish to change this you can use the date_1904 workbook option. This option is mainly for enhanced compatibility with Excel and in general isn’t required very often:
# workbook = xlsxwriter.Workbook(filename, {'date_1904': True})

# add_worksheet([name])
# Add a new worksheet to a workbook.


# Parameters:
# name (string) – Optional worksheet name, defaults to Sheet1, etc.
# Return type:
# A worksheet object.
# Raises:
# DuplicateWorksheetName – if a duplicate worksheet name is used.
# InvalidWorksheetName – if an invalid worksheet name is used.
# ReservedWorksheetName – if a reserved worksheet name is used.

# The name parameter is optional. If it is not specified, or blank, the default Excel convention will be followed, i.e. Sheet1, Sheet2, etc.:

# The worksheet name must be a valid Excel worksheet name:
# It must be less than 32 characters. This error will raise a InvalidWorksheetName exception.
# It cannot contain any of the characters: [ ] : * ? / \. This error will raise a InvalidWorksheetName exception.
# It cannot begin or end with an apostrophe. This error will raise a InvalidWorksheetName exception.
# You cannot use the same, case insensitive, name for more than one worksheet. This error will raise a DuplicateWorksheetName exception.
# You cannot use the Excel reserved name “History”, or case insensitive variants. This error will raise a ReservedWorksheetName exception.
# The rules for worksheet names in Excel are explained in the Microsoft Office documentation on how to Rename a worksheet.
# Category
# Description
# Property
# Method Name
# Font
# Font type
# 'font_name'
# set_font_name()
 
# Font size
# 'font_size'
# set_font_size()
 
# Font color
# 'font_color'
# set_font_color()
 
# Bold
# 'bold'
# set_bold()
 
# Italic
# 'italic'
# set_italic()
 
# Underline
# 'underline'
# set_underline()
 
# Strikeout
# 'font_strikeout'
# set_font_strikeout()
 
# Super/Subscript
# 'font_script'
# set_font_script()
# Number
# Numeric format
# 'num_format'
# set_num_format()
# Protection
# Lock cells
# 'locked'
# set_locked()
 
# Hide formulas
# 'hidden'
# set_hidden()
# Alignment
# Horizontal align
# 'align'
# set_align()
 
# Vertical align
# 'valign'
# set_align()
 
# Rotation
# 'rotation'
# set_rotation()
 
# Text wrap
# 'text_wrap'
# set_text_wrap()
 
# Reading order
# 'reading_order'
# set_reading_order()
 
# Justify last
# 'text_justlast'
# set_text_justlast()
 
# Center across
# 'center_across'
# set_center_across()
 
# Indentation
# 'indent'
# set_indent()
 
# Shrink to fit
# 'shrink'
# set_shrink()
# Pattern
# Cell pattern
# 'pattern'
# set_pattern()
 
# Background color
# 'bg_color'
# set_bg_color()
 
# Foreground color
# 'fg_color'
# set_fg_color()
# Border
# Cell border
# 'border'
# set_border()
 
# Bottom border
# 'bottom'
# set_bottom()
 
# Top border
# 'top'
# set_top()
 
# Left border
# 'left'
# set_left()
 
# Right border
# 'right'
# set_right()
 
# Border color
# 'border_color'
# set_border_color()
 
# Bottom color
# 'bottom_color'
# set_bottom_color()
 
# Top color
# 'top_color'
# set_top_color()
 
# Left color
# 'left_color'
# set_left_color()
 
# Right color
# 'right_color'
# set_right_color()
import xlsxwriter
def test4():
    workbook = xlsxwriter.Workbook('chart.xlsx')
    worksheet = workbook.add_worksheet()

    # Create a new Chart object.
    chart = workbook.add_chart({'type': 'column'})

    # Write some data to add to plot on the chart.
    data = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
    ]

    worksheet.write_column('A1', data[0])
    worksheet.write_column('B1', data[1])
    worksheet.write_column('C1', data[2])

    # Configure the chart. In simplest case we add one or more data series.
    chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
    chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
    chart.add_series({'values': '=Sheet1!$C$1:$C$5'})

    # Insert the chart into the worksheet.
    worksheet.insert_chart('A7', chart)

    workbook.close()
#     area: Creates an Area (filled line) style chart.
# bar: Creates a Bar style (transposed histogram) chart.
# column: Creates a column style (histogram) chart.
# line: Creates a Line style chart.
# pie: Creates a Pie style chart.
# doughnut: Creates a Doughnut style chart.
# scatter: Creates a Scatter style chart.
# stock: Creates a Stock style chart.
# radar: Creates a Radar style chart.
def test5():
    #######################################################################
    #
    # An example of creating an Excel chart in a chartsheet with Python
    # and XlsxWriter.
    #
    # Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
    #


    workbook = xlsxwriter.Workbook('chartsheet.xlsx')

    # Add a worksheet to hold the data.
    worksheet = workbook.add_worksheet()

    # Add a chartsheet. A worksheet that only holds a chart.
    chartsheet = workbook.add_chartsheet()

    # Add a format for the headings.
    bold = workbook.add_format({'bold': 1})

    # Add the worksheet data that the charts will refer to.
    headings = ['Number', 'Batch 1', 'Batch 2']
    data = [
        [2, 3, 4, 5, 6, 7],
        [10, 40, 50, 20, 10, 50],
        [30, 60, 70, 50, 40, 30],
    ]

    worksheet.write_row('A1', headings, bold)
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])


    # Create a new bar chart.
    chart1 = workbook.add_chart({'type': 'bar'})

    # Configure the first series.
    chart1.add_series({
        'name':       '=Sheet1!$B$1',
        'categories': '=Sheet1!$A$2:$A$7',
        'values':     '=Sheet1!$B$2:$B$7',
    })

    # Configure a second series. Note use of alternative syntax to define ranges.
    chart1.add_series({
        'name':       ['Sheet1', 0, 2],
        'categories': ['Sheet1', 1, 0, 6, 0],
        'values':     ['Sheet1', 1, 2, 6, 2],
    })

    # Add a chart title and some axis labels.
    chart1.set_title ({'name': 'Results of sample analysis'})
    chart1.set_x_axis({'name': 'Test number'})
    chart1.set_y_axis({'name': 'Sample length (mm)'})

    # Set an Excel chart style.
    chart1.set_style(11)

    # Add the chart to the chartsheet.
    chartsheet.set_chart(chart1)

    # Display the chartsheet as the active sheet when the workbook is opened.
    chartsheet.activate()

    workbook.close()

def test_table():
    ###############################################################################
#
# Example of how to add tables to an XlsxWriter worksheet.
#
# Tables in Excel are used to group rows and columns of data into a single
# structure that can be referenced in a formula or formatted collectively.
#
# Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
#


    workbook = xlsxwriter.Workbook('tables.xlsx')
    worksheet1 = workbook.add_worksheet()
    worksheet2 = workbook.add_worksheet()
    worksheet3 = workbook.add_worksheet()
    worksheet4 = workbook.add_worksheet()
    worksheet5 = workbook.add_worksheet()
    worksheet6 = workbook.add_worksheet()
    worksheet7 = workbook.add_worksheet()
    worksheet8 = workbook.add_worksheet()
    worksheet9 = workbook.add_worksheet()
    worksheet10 = workbook.add_worksheet()
    worksheet11 = workbook.add_worksheet()
    worksheet12 = workbook.add_worksheet()

    currency_format = workbook.add_format({'num_format': '$#,##0'})

    # Some sample data for the table.
    data = [
        ['Apples', 10000, 5000, 8000, 6000],
        ['Pears', 2000, 3000, 4000, 5000],
        ['Bananas', 6000, 6000, 6500, 6000],
        ['Oranges', 500, 300, 200, 700],

    ]


    ###############################################################################
    #
    # Example 1.
    #
    caption = 'Default table with no data.'

    # Set the columns widths.
    worksheet1.set_column('B:G', 12)

    # Write the caption.
    worksheet1.write('B1', caption)

    # Add a table to the worksheet.
    worksheet1.add_table('B3:F7')


    ###############################################################################
    #
    # Example 2.
    #
    caption = 'Default table with data.'

    # Set the columns widths.
    worksheet2.set_column('B:G', 12)

    # Write the caption.
    worksheet2.write('B1', caption)

    # Add a table to the worksheet.
    worksheet2.add_table('B3:F7', {'data': data})


    ###############################################################################
    #
    # Example 3.
    #
    caption = 'Table without default autofilter.'

    # Set the columns widths.
    worksheet3.set_column('B:G', 12)

    # Write the caption.
    worksheet3.write('B1', caption)

    # Add a table to the worksheet.
    worksheet3.add_table('B3:F7', {'autofilter': 0})

    # Table data can also be written separately, as an array or individual cells.
    worksheet3.write_row('B4', data[0])
    worksheet3.write_row('B5', data[1])
    worksheet3.write_row('B6', data[2])
    worksheet3.write_row('B7', data[3])


    ###############################################################################
    #
    # Example 4.
    #
    caption = 'Table without default header row.'

    # Set the columns widths.
    worksheet4.set_column('B:G', 12)

    # Write the caption.
    worksheet4.write('B1', caption)

    # Add a table to the worksheet.
    worksheet4.add_table('B4:F7', {'header_row': 0})

    # Table data can also be written separately, as an array or individual cells.
    worksheet4.write_row('B4', data[0])
    worksheet4.write_row('B5', data[1])
    worksheet4.write_row('B6', data[2])
    worksheet4.write_row('B7', data[3])


    ###############################################################################
    #
    # Example 5.
    #
    caption = 'Default table with "First Column" and "Last Column" options.'

    # Set the columns widths.
    worksheet5.set_column('B:G', 12)

    # Write the caption.
    worksheet5.write('B1', caption)

    # Add a table to the worksheet.
    worksheet5.add_table('B3:F7', {'first_column': 1, 'last_column': 1})

    # Table data can also be written separately, as an array or individual cells.
    worksheet5.write_row('B4', data[0])
    worksheet5.write_row('B5', data[1])
    worksheet5.write_row('B6', data[2])
    worksheet5.write_row('B7', data[3])


    ###############################################################################
    #
    # Example 6.
    #
    caption = 'Table with banded columns but without default banded rows.'

    # Set the columns widths.
    worksheet6.set_column('B:G', 12)

    # Write the caption.
    worksheet6.write('B1', caption)

    # Add a table to the worksheet.
    worksheet6.add_table('B3:F7', {'banded_rows': 0, 'banded_columns': 1})

    # Table data can also be written separately, as an array or individual cells.
    worksheet6.write_row('B4', data[0])
    worksheet6.write_row('B5', data[1])
    worksheet6.write_row('B6', data[2])
    worksheet6.write_row('B7', data[3])


    ###############################################################################
    #
    # Example 7.
    #
    caption = 'Table with user defined column headers'

    # Set the columns widths.
    worksheet7.set_column('B:G', 12)

    # Write the caption.
    worksheet7.write('B1', caption)

    # Add a table to the worksheet.
    worksheet7.add_table('B3:F7', {'data': data,
                                'columns': [{'header': 'Product'},
                                            {'header': 'Quarter 1'},
                                            {'header': 'Quarter 2'},
                                            {'header': 'Quarter 3'},
                                            {'header': 'Quarter 4'},
                                            ]})


    ###############################################################################
    #
    # Example 8.
    #
    caption = 'Table with user defined column headers'

    # Set the columns widths.
    worksheet8.set_column('B:G', 12)

    # Write the caption.
    worksheet8.write('B1', caption)

    # Formula to use in the table.
    formula = '=SUM(Table8[@[Quarter 1]:[Quarter 4]])'

    # Add a table to the worksheet.
    worksheet8.add_table('B3:G7', {'data': data,
                                'columns': [{'header': 'Product'},
                                            {'header': 'Quarter 1'},
                                            {'header': 'Quarter 2'},
                                            {'header': 'Quarter 3'},
                                            {'header': 'Quarter 4'},
                                            {'header': 'Year',
                                                'formula': formula},
                                            ]})


    ###############################################################################
    #
    # Example 9.
    #
    caption = 'Table with totals row (but no caption or totals).'

    # Set the columns widths.
    worksheet9.set_column('B:G', 12)

    # Write the caption.
    worksheet9.write('B1', caption)

    # Formula to use in the table.
    formula = '=SUM(Table9[@[Quarter 1]:[Quarter 4]])'

    # Add a table to the worksheet.
    worksheet9.add_table('B3:G8', {'data': data,
                                'total_row': 1,
                                'columns': [{'header': 'Product'},
                                            {'header': 'Quarter 1'},
                                            {'header': 'Quarter 2'},
                                            {'header': 'Quarter 3'},
                                            {'header': 'Quarter 4'},
                                            {'header': 'Year',
                                                'formula': formula
                                                },
                                            ]})


    ###############################################################################
    #
    # Example 10.
    #
    caption = 'Table with totals row with user captions and functions.'

    # Set the columns widths.
    worksheet10.set_column('B:G', 12)

    # Write the caption.
    worksheet10.write('B1', caption)

    # Options to use in the table.
    options = {'data': data,
            'total_row': 1,
            'columns': [{'header': 'Product', 'total_string': 'Totals'},
                        {'header': 'Quarter 1', 'total_function': 'sum'},
                        {'header': 'Quarter 2', 'total_function': 'sum'},
                        {'header': 'Quarter 3', 'total_function': 'sum'},
                        {'header': 'Quarter 4', 'total_function': 'sum'},
                        {'header': 'Year',
                            'formula': '=SUM(Table10[@[Quarter 1]:[Quarter 4]])',
                            'total_function': 'sum'
                            },
                        ]}

    # Add a table to the worksheet.
    worksheet10.add_table('B3:G8', options)


    ###############################################################################
    #
    # Example 11.
    #
    caption = 'Table with alternative Excel style.'

    # Set the columns widths.
    worksheet11.set_column('B:G', 12)

    # Write the caption.
    worksheet11.write('B1', caption)

    # Options to use in the table.
    options = {'data': data,
            'style': 'Table Style Light 11',
            'total_row': 1,
            'columns': [{'header': 'Product', 'total_string': 'Totals'},
                        {'header': 'Quarter 1', 'total_function': 'sum'},
                        {'header': 'Quarter 2', 'total_function': 'sum'},
                        {'header': 'Quarter 3', 'total_function': 'sum'},
                        {'header': 'Quarter 4', 'total_function': 'sum'},
                        {'header': 'Year',
                            'formula': '=SUM(Table11[@[Quarter 1]:[Quarter 4]])',
                            'total_function': 'sum'
                            },
                        ]}


    # Add a table to the worksheet.
    worksheet11.add_table('B3:G8', options)


    ###############################################################################
    #
    # Example 12.
    #
    caption = 'Table with column formats.'

    # Set the columns widths.
    worksheet12.set_column('B:G', 12)

    # Write the caption.
    worksheet12.write('B1', caption)

    # Options to use in the table.
    options = {'data': data,
            'total_row': 1,
            'columns': [{'header': 'Product', 'total_string': 'Totals'},
                        {'header': 'Quarter 1',
                            'total_function': 'sum',
                            'format': currency_format,
                            },
                        {'header': 'Quarter 2',
                            'total_function': 'sum',
                            'format': currency_format,
                            },
                        {'header': 'Quarter 3',
                            'total_function': 'sum',
                            'format': currency_format,
                            },
                        {'header': 'Quarter 4',
                            'total_function': 'sum',
                            'format': currency_format,
                            },
                        {'header': 'Year',
                            'formula': '=SUM(Table12[@[Quarter 1]:[Quarter 4]])',
                            'total_function': 'sum',
                            'format': currency_format,
                            },
                        ]}

    # Add a table to the worksheet.
    worksheet12.add_table('B3:G8', options)
    workbook.close()
def test_pane():
    #######################################################################
    #
    # Example of using Python and the XlsxWriter module to create
    # worksheet panes.
    #
    # Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
    #

    workbook = xlsxwriter.Workbook('panes.xlsx')

    worksheet1 = workbook.add_worksheet('Panes 1')
    worksheet2 = workbook.add_worksheet('Panes 2')
    worksheet3 = workbook.add_worksheet('Panes 3')
    worksheet4 = workbook.add_worksheet('Panes 4')

    #######################################################################
    #
    # Set up some formatting and text to highlight the panes.
    #
    header_format = workbook.add_format({'bold': True,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'fg_color': '#D7E4BC',
                                        'border': 1})

    center_format = workbook.add_format({'align': 'center'})


    #######################################################################
    #
    # Example 1. Freeze pane on the top row.
    #
    worksheet1.freeze_panes(1, 0)

    # Other sheet formatting.
    worksheet1.set_column('A:I', 16)
    worksheet1.set_row(0, 20)
    worksheet1.set_selection('C3')


    # Some text to demonstrate scrolling.
    for col in range(0, 9):
        worksheet1.write(0, col, 'Scroll down', header_format)

    for row in range(1, 100):
        for col in range(0, 9):
            worksheet1.write(row, col, row + 1, center_format)


    #######################################################################
    #
    # Example 2. Freeze pane on the left column.
    #
    worksheet2.freeze_panes(0, 1)

    # Other sheet formatting.
    worksheet2.set_column('A:A', 16)
    worksheet2.set_selection('C3')

    # Some text to demonstrate scrolling.
    for row in range(0, 50):
        worksheet2.write(row, 0, 'Scroll right', header_format)
        for col in range(1, 26):
            worksheet2.write(row, col, col, center_format)
def test_pane():
    #######################################################################
    #
    # Example of using Python and the XlsxWriter module to create
    # worksheet panes.
    #
    # Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
    #
    import xlsxwriter

    workbook = xlsxwriter.Workbook('panes.xlsx')

    worksheet1 = workbook.add_worksheet('Panes 1')
    worksheet2 = workbook.add_worksheet('Panes 2')
    worksheet3 = workbook.add_worksheet('Panes 3')
    worksheet4 = workbook.add_worksheet('Panes 4')

    #######################################################################
    #
    # Set up some formatting and text to highlight the panes.
    #
    header_format = workbook.add_format({'bold': True,
                                        'align': 'center',
                                        'valign': 'vcenter',
                                        'fg_color': '#D7E4BC',
                                        'border': 1})

    center_format = workbook.add_format({'align': 'center'})


    #######################################################################
    #
    # Example 1. Freeze pane on the top row.
    #
    worksheet1.freeze_panes(1, 0)

    # Other sheet formatting.
    worksheet1.set_column('A:I', 16)
    worksheet1.set_row(0, 20)
    worksheet1.set_selection('C3')


    # Some text to demonstrate scrolling.
    for col in range(0, 9):
        worksheet1.write(0, col, 'Scroll down', header_format)

    for row in range(1, 100):
        for col in range(0, 9):
            worksheet1.write(row, col, row + 1, center_format)


    #######################################################################
    #
    # Example 2. Freeze pane on the left column.
    #
    worksheet2.freeze_panes(0, 1)

    # Other sheet formatting.
    worksheet2.set_column('A:A', 16)
    worksheet2.set_selection('C3')

    # Some text to demonstrate scrolling.
    for row in range(0, 50):
        worksheet2.write(row, 0, 'Scroll right', header_format)
        for col in range(1, 26):
            worksheet2.write(row, col, col, center_format)


    #######################################################################
    #
    # Example 3. Freeze pane on the top row and left column.
    #
    worksheet3.freeze_panes(1, 1)

    # Other sheet formatting.
    worksheet3.set_column('A:Z', 16)
    worksheet3.set_row(0, 20)
    worksheet3.set_selection('C3')
    worksheet3.write(0, 0, '', header_format)

    # Some text to demonstrate scrolling.
    for col in range(1, 26):
        worksheet3.write(0, col, 'Scroll down', header_format)

    for row in range(1, 50):
        worksheet3.write(row, 0, 'Scroll right', header_format)
        for col in range(1, 26):
            worksheet3.write(row, col, col, center_format)


    #######################################################################
    #
    # Example 4. Split pane on the top row and left column.
    #
    # The divisions must be specified in terms of row and column dimensions.
    # The default row height is 15 and the default column width is 8.43
    #
    worksheet4.split_panes(15, 8.43)

    # Other sheet formatting.
    worksheet4.set_selection('C3')

    # Some text to demonstrate scrolling.
    for col in range(1, 26):
        worksheet4.write(0, col, 'Scroll', center_format)

    for row in range(1, 50):
        worksheet4.write(row, 0, 'Scroll', center_format)
        for col in range(1, 26):
            worksheet4.write(row, col, col, center_format)

    workbook.close()


def test_img():
        ######################################################################
    #
    # This program shows several examples of how to set up headers and
    # footers with XlsxWriter.
    #
    # The control characters used in the header/footer strings are:
    #
    #     Control             Category            Description
    #     =======             ========            ===========
    #     &L                  Justification       Left
    #     &C                                      Center
    #     &R                                      Right
    #
    #     &P                  Information         Page number
    #     &N                                      Total number of pages
    #     &D                                      Date
    #     &T                                      Time
    #     &F                                      File name
    #     &A                                      Worksheet name
    #
    #     &fontsize           Font                Font size
    #     &"font,style"                           Font name and style
    #     &U                                      Single underline
    #     &E                                      Double underline
    #     &S                                      Strikethrough
    #     &X                                      Superscript
    #     &Y                                      Subscript
    #
    #     &[Picture]          Images              Image placeholder
    #     &G                                      Same as &[Picture]
    #
    #     &&                  Miscellaneous       Literal ampersand &
    #
    # See the main XlsxWriter documentation for more information.
    #
    # Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
    #

    workbook = xlsxwriter.Workbook('headers_footers.xlsx')
    preview = 'Select Print Preview to see the header and footer'

    ######################################################################
    #
    # A simple example to start
    #
    worksheet1 = workbook.add_worksheet('Simple')
    header1 = '&CHere is some centered text.'
    footer1 = '&LHere is some left aligned text.'

    worksheet1.set_header(header1)
    worksheet1.set_footer(footer1)

    worksheet1.set_column('A:A', 50)
    worksheet1.write('A1', preview)


    ######################################################################
    #
    # Insert a header image.
    #
    worksheet2 = workbook.add_worksheet('Image')
    header2 = '&L&G'

    # Adjust the page top margin to allow space for the header image.
    worksheet2.set_margins(top=1.3)

    worksheet2.set_header(header2, {'image_left': '123.png'})

    worksheet2.set_column('A:A', 50)
    worksheet2.write('A1', preview)


    ######################################################################
    #
    # This is an example of some of the header/footer variables.
    #
    worksheet3 = workbook.add_worksheet('Variables')
    header3 = '&LPage &P of &N' + '&CFilename: &F' + '&RSheetname: &A'
    footer3 = '&LCurrent date: &D' + '&RCurrent time: &T'

    worksheet3.set_header(header3)
    worksheet3.set_footer(footer3)

    worksheet3.set_column('A:A', 50)
    worksheet3.write('A1', preview)
    worksheet3.write('A21', 'Next sheet')
    worksheet3.set_h_pagebreaks([20])

    ######################################################################
    #
    # This example shows how to use more than one font
    #
    worksheet4 = workbook.add_worksheet('Mixed fonts')
    header4 = '&C&"Courier New,Bold"Hello &"Arial,Italic"World'
    footer4 = '&C&"Symbol"e&"Arial" = mc&X2'

    worksheet4.set_header(header4)
    worksheet4.set_footer(footer4)

    worksheet4.set_column('A:A', 50)
    worksheet4.write('A1', preview)

    ######################################################################
    #
    # Example of line wrapping
    #
    worksheet5 = workbook.add_worksheet('Word wrap')
    header5 = "&CHeading 1\nHeading 2"

    worksheet5.set_header(header5)

    worksheet5.set_column('A:A', 50)
    worksheet5.write('A1', preview)

    ######################################################################
    #
    # Example of inserting a literal ampersand &
    #
    worksheet6 = workbook.add_worksheet('Ampersand')
    header6 = '&CCuriouser && Curiouser - Attorneys at Law'

    worksheet6.set_header(header6)

    worksheet6.set_column('A:A', 50)
    worksheet6.write('A1', preview)

    workbook.close()


def imag_test_from_web():
    ##############################################################################
    #
    # An example of inserting images from a Python BytesIO byte stream into a
    # worksheet using the XlsxWriter module.
    #
    # Copyright 2013-2019, John McNamara, jmcnamara@cpan.org
    #

    # Import the byte stream handler.
    from io import BytesIO

    # Import urlopen() for either Python 2 or 3.
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen


    import xlsxwriter
    # Create the workbook and add a worksheet.
    workbook  = xlsxwriter.Workbook('images_bytesio.xlsx')
    worksheet = workbook.add_worksheet()


    # Read an image from a remote url.
    url = 'https://raw.githubusercontent.com/jmcnamara/XlsxWriter/' + \
        'master/examples/logo.png'

    image_data = BytesIO(urlopen(url).read())

    # Write the byte stream image to a cell. Note, the filename must be
    # specified. In this case it will be read from url string.
    worksheet.insert_image('B2', url, {'image_data': image_data})


    # Read a local image file into a a byte stream. Note, the insert_image()
    # method can do this directly. This is for illustration purposes only.
    filename   = '123.png'

    image_file = open(filename, 'rb')
    image_data = BytesIO(image_file.read())
    image_file.close()


    # Write the byte stream image to a cell. The filename must  be specified.
    worksheet.insert_image('B8', filename, {'image_data': image_data})


    workbook.close()
def chart_line_test():
    import xlsxwriter

    workbook = xlsxwriter.Workbook('chart_line.xlsx')
    worksheet = workbook.add_worksheet()

    # Add the worksheet data to be plotted.
    data = [10, 40, 50, 20, 10, 50]
    worksheet.write_column('A1', data)

    # Create a new chart object.
    chart = workbook.add_chart({'type': 'line'})

    # Add a series to the chart.
    chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

    # Insert the chart into the worksheet.
    worksheet.insert_chart('C1', chart)

    workbook.close()