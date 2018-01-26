# Flask设置返回json格式数据

## 问题描述

在Flask中直接返回`list`或`dict`是不行的，如

Python

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return t

if __name__ == '__main__':
    app.debug = True
    app.run()
```

这样访问会直接提示

```python
TypeError: 'dict' object is not callable
```

其原因是Flask并不会将`list`或`dict`默认转换为json格式。

## 解决方法

HTTP返回json格式数据主要有两个方面：

1. 数据本身为json格式；
2. `Content-Type`声明为json格式。

### 使用标准库`json`

比较常见的是采用标准库`json`进行格式转换：

Python

```python
from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return json.dumps(t)

if __name__ == '__main__':
    app.debug = True
    app.run()
```

这样当访问时即能够正常得到json数据。但这么做有一个缺点，就是HTTP返回的`Content-Type`仍然是`text/html`，即HTTP认为内容是HTML。

### 声明`Content-Type`为json格式

在上面的解决方法上作一个加强，手动指定其`Content-Type`为`application/json`，通常采用的是修改Flask中的`Response`模块：

Python

```python
from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return Response(json.dumps(t), mimetype='application/json')

if __name__ == '__main__':
    app.debug = True
    app.run()
```

这样不仅HTTP返回的内容是json，而且返回的`Content-Type`也是`application/json`了。

### 使用Flask的`jsonify`模块

实际上flask已经为json准备了专门的模块：`jsonify`。`jsonify`不仅会将内容转换为json，而且也会修改`Content-Type`为`application/json`。

Python

```python
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)

if __name__ == '__main__':
    app.debug = True
    app.run()
```

### 自定义Flask的`Response`，使用`force_type()`（2017.11.9更新）

对于某些特殊的情况，可能并不想每个返回json数据的方法都使用`jsonify()`包起来，那有没有什么“非侵入式”的方法实现`jsonify()`的功能呢？其实是有的，不过这个方法相对比较高端。

Flask返回的内容实际是`Response`对象，`return`语句的内容实际是交给`Response`处理后才输出由HTTP返回的；也就是说，之前直接返回`dict`报错`TypeError: 'dict' object is not callable`也是`Response`干的。那么只需要在`Response`处理如`dict`等“非法”数据是，告诉`Response`该怎么做就好了，这里就是用到了其`force_type()`方法了，所有不能处理的数据，都由`force_type()`方法尝试处理后，再决定报错或通过。直接看例子吧。

Python

```python
from flask import Flask, Response, jsonify

class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)

app = Flask(__name__)
app.response_class = MyResponse

@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return t

if __name__ == '__main__':
    app.debug = True
    app.run()
```

或者还可以以继承的方式来实现自定义`Response`，如：

Python

```python
from flask import Flask, Response, jsonify

class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)

class MyFlask(Flask):
    response_class = MyResponse

app = MyFlask(__name__)

@app.route('/')
def root():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return t

if __name__ == '__main__':
    app.debug = True
    app.run()
```