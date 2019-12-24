# -*- coding:utf-8 -*-
from test.tob_xfd.common.getSign import getSign
from test.tob_xfd.data.accessToken_params import xfd_accessToken_params, gfd_accessToken_params
from test.tob_xfd.testCase.gfdOrder.test_gfd_accessToken import gfd_accessToken
from test.tob_xfd.testCase.order.test_accessToken import accessToken

"""
合并令牌的参数并加密
"""
def getMergeParams(params):
    # 获取到商户的密钥
    merchantKey = xfd_accessToken_params.params_ZXXD['merchantKey']

    #获取令牌参数
    token = accessToken(xfd_accessToken_params.params_ZXXD).json()['data']

    #参数变量
    params = params

    #合并参数
    params.update(token)

    #删除不需要的元素
    del params['expiresIn']
    del params['refreshToken']

    #对参数进行加签
    sign = getSign(params, merchantKey)

    params['sign'] = sign
    return params

"""
合并"功夫贷"令牌的参数并加密
"""
def getGFDMergeParams(params):
    # 获取到商户的密钥
    merchantKey = gfd_accessToken_params.params_ZXXD['client_secret']

    #获取令牌参数
    token = gfd_accessToken(gfd_accessToken_params.params_ZXXD).json()

    #参数变量
    params = params

    #合并参数
    params.update(token)

    #删除不需要的元素
    del params['username']
    del params['expires_in']

    #对参数进行加签
    sign = getSign(params, merchantKey)

    params['sign'] = sign
    return params