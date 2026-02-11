from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import re

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Parse query parameters
        query = parse_qs(urlparse(self.path).query)
        name = query.get('name', [''])[0].strip()
        custom_id = query.get('id', [''])[0].strip()
        
        # 2. REQUIRED: Name must be present
        if not name:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Error: Missing user name. (Format: /dp/Name?id=ID)")
            return

        # 3. REQUIRED: ID must be present
        if not custom_id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Error: Missing NextDNS ID. (Format: /dp/Name?id=ID)")
            return

        # 4. Validate ID
        if re.match(r'^[a-zA-Z0-9]{6}$', custom_id):
            final_id = custom_id
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Error: Invalid NextDNS ID format.")
            return
        
        # 5. Construct Server URL
        # Sanitize name to ensure it's valid for URL
        safe_name = re.sub(r'[^a-zA-Z0-9_-]', '', name)
        if not safe_name: safe_name = "Device"
        
        server_url = f"https://dns.nextdns.io/{final_id}/{safe_name}"
        profile_name = f"LOCKET GOLD - {safe_name}"

        # 6. XML Template
        xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>DNSSettings</key>
            <dict>
                <key>DNSProtocol</key>
                <string>HTTPS</string>
                <key>ServerURL</key>
                <string>{server_url}</string>
            </dict>
            <key>PayloadDescription</key>
            <string>CHẶN THU HỒI LOCKET GOLD</string>
            <key>PayloadDisplayName</key>
            <string>{profile_name}</string>
            <key>PayloadOrganization</key>
            <string>Locket Gold</string>
            <key>PayloadIdentifier</key>
            <string>com.camsitup.controld.dnsprofile</string>
            <key>PayloadType</key>
            <string>com.apple.dnsSettings.managed</string>
            <key>PayloadUUID</key>
            <string>0E3B4D2E-4C3F-4B2D-BAE6-8E1F6E7A2F44</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array> <key>PayloadDescription</key>
    <string>CHẶN THU HỒI LOCKET GOLD
</string>
    <key>PayloadDisplayName</key>
    <string>{profile_name}</string>
    <key>PayloadOrganization</key>
    <string>Locket Gold</string>
    <key>PayloadIdentifier</key>
    <string>com.camsitup.profile.controld.doh</string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>5A9E1F7C-01B3-4E90-BB7E-712F93E19F66</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>"""

        # 7. Send Response
        self.send_response(200)
        self.send_header('Content-Type', 'application/x-apple-aspen-config')
        self.send_header('Content-Disposition', 'attachment; filename=KM.mobileconfig')
        self.end_headers()
        self.wfile.write(xml_content.encode('utf-8'))
        return
