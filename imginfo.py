# 文件名PictureGps.py
import exifread
import re


# 读取图片中的信息
def FindGPSTime(filePath):
    GPS = {}
    Data = ""
    f = open(filePath, 'rb')  # 读取图片信息
    tags = exifread.process_file(f)

    for tag, value in tags.items():
        if re.match('GPS GPSLatitudeRef', tag):
            GPS['GPSLatitudeRef(纬度标识)'] = str(value)
        elif re.match('GPS GPSLongitudeRef', tag):
            GPS['GPSLongitudeRef(经度标识)'] = str(value)
        elif re.match('GPS GPSAltitudeRef', tag):
            GPS['GPSAltitudeRef(高度标识)'] = str(value)
        elif re.match('GPS GPSLatitude', tag):
            try:
                match_result = re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]', str(value)).groups()  # 匹配临近的字符
                GPS['GPSLatitude(纬度)'] = [int(match_result[0]), int(match_result[1]),int(match_result[2]) / int(match_result[3])]
            except:
                GPS['GPSLatitude(纬度)'] = str(value)
        elif re.match('GPS GPSLongitude', tag):
            try:
                match_result = re.match('\[(\w*), (\w*), (\w.*)/(\w.*)\]', str(value)).groups()
                GPS['GPSLongitude(经度)'] = [int(match_result[0]), int(match_result[1]),
                                           int(match_result[2]) / int(match_result[3])]
            except:
                GPS['GPSLongitude(经度)'] = str(value)
        elif re.match('GPS GPSAltitude', tag):
            GPS['GPSAltitude(高度)'] = str(value)
        elif re.match('Image DateTime', tag):
            Data = str(value)
    return {'GPS 信息': GPS, '时间信息': Data}


# 将经纬度的度分秒转换成十进制格式
def GPSSwitch(filepath):
    print(FindGPSTime(filepath))
    PictureGPS = FindGPSTime(filepath)
    GPSLongitude = PictureGPS['GPS 信息']['GPSLongitude(经度)']  # 经度的列表内容
    GPSLatitude = PictureGPS['GPS 信息']['GPSLatitude(纬度)']  # 纬度的列表内容
    x = GPSLongitude[0] + GPSLongitude[1] / 60 + GPSLongitude[2] / 3600  # 进制转换
    y = GPSLatitude[0] + GPSLatitude[1] / 60 + GPSLatitude[2] / 3600
    return {'经度转换': x, '纬度转换': y}


if __name__ == '__main__':
    print(GPSSwitch("1.jpg"))  # 需要提取信息的图片名
