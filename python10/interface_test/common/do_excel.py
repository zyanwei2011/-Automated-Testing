import openpyxl


class Do_Excel:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self,  button, case_id_list):
        wb = openpyxl.load_workbook(self.file_name)
        sheet_register= wb['register']
        sheet_tel = wb['tel']
        tel = sheet_tel.cell(1,1).value


        test_data = []
        for i in range(2,sheet_register.max_row+1):
            sub_data= {}
            sub_data['id'] = sheet_register.cell(i, 1).value
            sub_data['module'] = sheet_register.cell(i, 2).value
            sub_data['title'] = sheet_register.cell(i, 3).value
            sub_data['method'] = sheet_register.cell(i, 4).value
            sub_data['url'] = sheet_register.cell(i, 5).value
            if sheet_register.cell(i, 6).value.find('${tel}') != -1:
                sub_data['param'] = sheet_register.cell(i, 6).value.replace('${tel}', str(tel))
            else:
                sub_data['param'] = sheet_register.cell(i, 6).value
            sub_data['ExpectedResult(code)'] = sheet_register.cell(i, 7).value
            test_data.append(sub_data)

        if button == 'on':
            final_data = []
            for item in test_data:
                if item['id'] in eval(case_id_list):
                    final_data.append(item)
        else:
            final_data = test_data

        wb['tel'].cell(1,1).value = tel + 1
        wb.save(self.file_name)
        return final_data

    def write_back(self, row, ActualResult, TestResult):
        wb = openpyxl.load_workbook(self.file_name)
        sheet = wb['register']
        sheet.cell(row, 8).value = ActualResult
        sheet.cell(row, 9).value = TestResult
        wb.save(self.file_name)

