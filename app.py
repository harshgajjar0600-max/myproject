import http.server, socketserver, os, platform
PORT = 8080
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            files = "<br>".join(os.listdir('.'))
            html = f"<html><body style='font-family:sans-serif;padding:20px;background:#121212;color:#fff'><h2>iPhone iSH Control Panel</h2><p><b>System:</b> {platform.system()}</p><p><b>Folder:</b> {os.getcwd()}</p><h3>Files:</h3><div>{files}</div></body></html>"
            self.wfile.write(html.encode('utf-8'))
        else:
            super().do_GET()
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
