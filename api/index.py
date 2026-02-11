from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Parse 'name' from query string
        query = parse_qs(urlparse(self.path).query)
        name = query.get('name', [''])[0].strip()
        
        # 2. Base NextDNS ID
        base_id = "8cb53e"
        
        # 3. Construct Server URL
        # If name is provided, append it: https://dns.nextdns.io/8a922e/Name
        # If not, use default: https://dns.nextdns.io/8a922e
        if name:
             # Sanitize name to ensure it's valid for URL (basic alphanumeric + - _)
            import re
            safe_name = re.sub(r'[^a-zA-Z0-9_-]', '', name)
            if not safe_name: safe_name = "Device"
            server_url = f"https://dns.nextdns.io/{base_id}/{safe_name}"
            profile_name = f"LOCKET GOLD - {safe_name}"
        else:
            server_url = f"https://dns.nextdns.io/{base_id}"
            profile_name = "LOCKET GOLD - Marineshop"

        # 4. XML Template (Embedded to avoid file path issues on Vercel)
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

        # 5. Send Response
        self.send_response(200)
        self.send_header('Content-Type', 'application/x-apple-aspen-config')
        self.send_header('Content-Disposition', 'attachment; filename=KM.mobileconfig')
        self.end_headers()
        self.wfile.write(xml_content.encode('utf-8'))
        return
