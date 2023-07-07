from flask import session
from ..trade import bp

from flask import request
import os
from data_sheet import session, Transaction


@bp.route("/getalltransaction",methods=["POST"])
def getalltransaction():
    resultlist = []
    result = session.query(Transaction).all()
    if result is None:
        return {"code":302,"message":"这条商品信息不存在"}
    for r in result:
        if r.approved == 0:
            continue
        try:
            price = r.price
            channel = r.channel
            login_method = r.login_method
            system = r.system
            addiction = r.addiction
            approved = r.approved
            message = ""
            file_path = r'E:\trade\account' + '\\' + str(r.id) + ".txt"
            if not os.path.exists(file_path):  # 检测目录是否存在，不在则创建
                return {'code': 302, 'message': '交易信息不存在'}
            f = open(file_path, 'r')
            for line in f:
                message += line
            resultlist.append({"tid":r.id,"price": price, "channel": channel, "login_method": login_method, "message": message, "system": system,
                "addiction": addiction, "seller": r.seller})
        except Exception as e:
            print(e)
            return {"code": 307, "message": "信息获取失败，请稍后再试"}
    return {"code":200,"message":"success","data":resultlist}
