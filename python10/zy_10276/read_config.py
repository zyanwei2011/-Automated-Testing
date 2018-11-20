import configparser


class ReadConfig:
    def read_config(self,filenames, section, option):
        cf = configparser.ConfigParser()
        cf.read(filenames, encoding='UTF_8')
        value = cf.get(section, option)
        return value


if __name__ == '__main__':
    button = ReadConfig().read_config('case.config', 'CASE_LIST', 'button')
    case_id_list = ReadConfig().read_config('case.config', 'CASE_LIST', 'case_id_list')
    print(button, case_id_list)




