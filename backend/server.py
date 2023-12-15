from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from tujia_new import get_data
import json


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        global pending
        if pending:
            datas = {
                "code": 500,
                "data": "",
                "msg": "任务已有他人执行，稍后再试！"
            }
        else:
            pending = True
            query = parse_qs(urlparse(self.path).query)
            # 获取参数值
            id = query.get('id', [''])[0]
            name = query.get('name', [''])[0]
            area = query.get('area', [''])[0]
            datas = {
                "code": 200,
                "data": get_data(id, name, area),
                "msg": "success"
            }
            pending = False
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(datas).encode())


if __name__ == '__main__':
    pending = False
    host = ('', 8088)
    server = HTTPServer(host, Resquest)
    print("[+] http://%s:%s\n" % host)
    server.serve_forever()
