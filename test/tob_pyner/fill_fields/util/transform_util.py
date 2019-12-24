from datetime import datetime

from test.tob_pyner.fill_fields.util.MySqlHelper import query


def test_idc_area():
    """先获取地区字典 避免多次查询数据库"""
    area_dict = get_area_dict()

    """将身份证前六位转化成地区信息"""
    idc = "330381111111111111"
    idc = "320721198902194213"

    """从字典重查询地区信息"""
    location = trans_idc_area(idc, area_dict)
    print("%s %s %s %s %s" % (location.province_name,
                              location.city_name, location.area_name, location.longitude, location.latitude))


def test_transform_sex():
    """转换性别"""
    # idc = '33038119960418101X '
    idc = '130503670401002'
    print(trans_sex(idc))


def test_transform_birthday():
    """转换生日"""
    idc = '33038119960418101X'
    print(trans_birthday(idc))


def test_uscc_area():
    area_dict = get_area_dict()
    """转换统一社会代码为地区"""
    # uscc = '91440101310522234C'
    uscc = '91110107330246732H'

    location = trans_uscc_area(uscc, area_dict)
    print("%s %s %s %s %s" % (location.province_name,
                              location.city_name, location.area_name, location.longitude, location.latitude))


def trans_uscc_area(uscc, area_dict):
    if uscc is None:
        return Location()
    province = uscc[2:4]
    city = uscc[4:6]
    area = uscc[6:8]

    return get_area_name(area, city, province, area_dict)


def trans_birthday(idc):
    if idc is None:
        return None
    if len(idc) == 15:
        birthday = '19' + idc[6:12]
    else:
        birthday = idc[6:14]
    try:
        return datetime.strptime(birthday, "%Y%m%d")
    except ValueError:
        return None


def trans_sex(idc):
    if idc is None:
        return None
    """
    转换性别 'M'为男 'F'为女
    """
    if len(idc) == 15:
        sex = int(idc[14])
    elif len(idc) == 18:
        sex = int(idc[16])
    else:
        return None
    if sex % 2 == 0:
        # 偶数为女
        return 'F'
    else:
        # 奇数为男
        return 'M'


class Area:
    def __init__(self, code, name, longitude, latitude):
        self.code = code
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.subArea = {}


class Location:
    def __init__(self):
        self.province_code = None
        self.province_name = None
        self.city_code = None
        self.city_name = None
        self.area_code = None
        self.area_name = None
        self.longitude = None
        self.latitude = None


def get_area_dict():
    """查询身份证地区配置"""
    area_dict = {}
    results = query(
        'select area_code, area_name, city_code, city_name, province_code, province_name,longitude,latitude '
        'from b2b_pyner_config.b2b_pyner_area')
    for result in results:
        area_code = result[0]
        area_name = result[1]
        city_code = result[2]
        city_name = result[3]
        province_code = result[4]
        province_name = result[5]
        longitude = result[6]
        latitude = result[7]

        if province_code not in area_dict:
            area = Area(province_code, province_name, longitude, latitude)
            area_dict[province_code] = area

        if city_code not in area_dict[province_code].subArea:
            area = Area(city_code, city_name, longitude, latitude)
            area_dict[province_code].subArea[city_code] = area

        if area_code not in area_dict[province_code].subArea[city_code].subArea:
            area = Area(area_code, area_name, longitude, latitude)
            area_dict[province_code].subArea[city_code].subArea[area_code] = area

    print('获取地区字典成功')
    return area_dict


def trans_idc_area(idc, area_dict):
    """转换18位身份证前六位成地区"""
    if idc is None:
        return Location()
    province = idc[0:2]
    city = idc[2:4]
    area = idc[4:6]

    return get_area_name(area, city, province, area_dict)


def get_area_name(area, city, province, area_dict):
    location = Location()
    if province in area_dict:
        province_info = area_dict[province]
        location.province_code = province_info.code
        location.province_name = province_info.name
        location.longitude = province_info.longitude
        location.latitude = province_info.latitude

        if city in province_info.subArea:
            city_info = province_info.subArea[city]
            location.city_code = city_info.code
            location.city_name = city_info.name
            location.longitude = city_info.longitude
            location.latitude = city_info.latitude

            if area in city_info.subArea:
                area_info = city_info.subArea[area]
                location.area_code = area_info.code
                location.area_name = area_info.name
                location.longitude = area_info.longitude
                location.latitude = area_info.latitude
    return location
