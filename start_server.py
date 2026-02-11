
import http.server
import socketserver
import os

# Configuration
PORT = 8000
FILE_TO_SERVE = "KM.mobileconfig"
MIME_TYPE = "application/x-apple-aspen-config"

class MobileConfigHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve the mobileconfig file for root path or direct file access
        if self.path == "/" or self.path == "/" + FILE_TO_SERVE:
            if os.path.exists(FILE_TO_SERVE):
                try:
                    # Open file in binary mode
                    with open(FILE_TO_SERVE, 'rb') as f:
                        content = f.read()
                    
                    self.send_response(200)
                    self.send_header("Content-Type", MIME_TYPE)
                    self.send_header("Content-Disposition", f'attachment; filename="{FILE_TO_SERVE}"')
                    self.send_header("Content-Length", str(len(content)))
                    self.end_headers()
                    self.wfile.write(content)
                    print(f"Served {FILE_TO_SERVE} across to {self.client_address[0]}")
                except Exception as e:
                    self.send_error(500, f"Error reading file: {e}")
            else:
                self.send_error(404, "File not found")
        else:
            # For any other path, just redirect to root to force download (optional strategy)
            # or return 404. Let's redirect to be helpful.
            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()

if __name__ == "__main__":
    # Ensure we are in the directory containing the script/file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    if not os.path.exists(FILE_TO_SERVE):
        print(f"Error: {FILE_TO_SERVE} not found in {os.getcwd()}")
        exit(1)

    print(f"Starting server on port {PORT}...")
    print(f"Serving {FILE_TO_SERVE} with MIME type {MIME_TYPE}")
    print(f"URL: http://localhost:{PORT}")
    
    try:
        with socketserver.TCPServer(("", PORT), MobileConfigHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
