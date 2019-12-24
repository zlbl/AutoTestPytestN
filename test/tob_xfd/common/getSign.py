# -*- coding:utf-8 -*-
from test.tob_xfd.common.getStrMD5 import md5
from test.tob_xfd.data.accessToken_params import xfd_accessToken_params

"""
TOB_生成验签
"""
def getSign(params, merchantKey):
    strParams=""
    #取出参数的所有key进行排序
    # keys = params.keys()
    # keys.sorted(keys)

    #将数据字典的值按照key=value，通过&拼接成字符串
    for key in sorted(params):
        # print(key, ' value : ', params[key])
        # if len(str(params[key]))>0:
        #     if str(params[key])[0] == '{':
        #         keyValue=key+"="+"\""+str(params[key])+"\""
        #         strParams=strParams+keyValue+"&"
        #     else:
        #         keyValue = key + "=" + str(params[key])
        #         strParams = strParams + keyValue + "&"
        # else:
        keyValue = key + "=" + str(params[key])
        strParams = strParams + keyValue + "&"

    #将字符串进行MD5加密
    strParams=strParams[:-1]
    strParams=strParams.replace("\'", "\"");
    strParams=strParams.replace(" ", "")
    strParams=strParams+"&key="+merchantKey
    sign = md5(strParams)
    return sign.upper()