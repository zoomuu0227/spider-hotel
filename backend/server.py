from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from tujia import get_data
import json


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        '''
        处理get请求
        '''
        # 打印请求方法
        print(self.command)
        # 打印请求头
        print(self.headers)
        # 打印请求路径
        print(self.requestline)

        print(self.path)
        query = parse_qs(urlparse(self.path).query)

        # 获取参数值
        id = query.get('id', [''])[0]
        name = query.get('name', [''])[0]
        area = query.get('area', [''])[0]
        datas = get_data(id,name,area)
        # datas = {
        #     "msg": "hello"
        # }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(datas).encode())

    def do_POST(self):
        '''
        处理post请求
        '''
        # 接收post数据
        req = self.rfile.read(int(self.headers['content-length']))
        req_datas = req.decode('utf-8')
        # 打印post数据
        # print(req_datas)

        # 处理post参数
        key, value = req_datas[:req_datas.find('=')], req_datas[req_datas.find('=') + 1:]
        res_datas = str({'key': key, 'value': value})

        # 返回响应头
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')  # 返回结果为信息
        # self.send_header('Content-type', 'application/json')	# 返回结果为json
        # self.send_header('Content-type', 'application/text')	# 返回结果为文本文件
        self.end_headers()

        # 打印请求结果
        self.wfile.write(res_datas.encode('utf-8'))


if __name__ == '__main__':
    host = ('', 8088)
    server = HTTPServer(host, Resquest)
    print("[+] http://%s:%s\n" % host)
    server.serve_forever()
