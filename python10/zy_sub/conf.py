import configparser


class ReadConfig:
    def read_config(self, file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8')
        value = cf.get(section, option)
        return value


if __name__ == '__main__':
    button = ReadConfig().read_config('case.conf', 'SECTION', 'button')
    case_no = ReadConfig().read_config('case.conf', 'SECTION', 'case_id')
    print(button,case_no)

