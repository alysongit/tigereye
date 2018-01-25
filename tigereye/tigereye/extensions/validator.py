import functools
from flask import request, jsonify

from tigereye.helper.code import Code


class Validator():
    """接口参数验证器"""
    def __init__(self,**params_template):

        self.pt =params_template #接收参数的模板，并存放至类成员属性

    def __call__(self, f): #实际实现参数过滤的装饰器函数 ：param f api里的接口方法
        @functools.wraps(f)  #用wraps方法包装，传递被装饰函数的信息
        def decorated_function(*args,**kwargs):
            try:
                request.params={}  #先定义一个字典，并赋予request.params
                for k ,v in self.pt.items(): #遍历self.pt,也就是__init__函数内接收到的rams_template
                    #k就是参数名称，v就是具体的去验证，转换这个参数的函数，最后将转换后的结果保存到request.params内
                    request.params[k]=v(request.values[k])
            except Exception:
                #如果发生异常，说明在转换过程中出错，也就是说参数不符合规则或者参数不符合规则
                response = jsonify(
                    rc =Code.required_parameter_missing.value,
                    msg =Code.required_parameter_missing.name,
                    data={
                        'required_param':k,
                        'your_passed':request.values.get(k),
                          }
                )
                #设置response的http响应吗
                response.status_code=400
                #返回response对象
                return response
            #执行被装饰的接口方法，并返回函数
            return f(*args,**kwargs)
        #返回装饰器函数
        return decorated_function

class ValidationError(Exception):
    def __init__(self,message,values):
        super(ValidationError,self).__init__(message)
        self.values = values


def multi_int(values, sperator=','):
    return [int(i) for i in values.split(sperator)]


def complex_int(values,sperator='-'):
    "验证多个数字,类似1-2-3, 并返回一个元祖"
    digits = values.split(sperator)
    result = []
    for digit in digits:
        if not digit.isdigit():
            raise ValidationError('complex int error : %s' % values , values)
        result.append(int(digit))
    return tuple(result)


def multi_complex_int(values, sperator=','):
    "验证多组数字, 类似1-2-3,4-5-6 最后返回一个列表包含N个元祖"
    return [complex_int(i) for i in values.split(sperator)]
