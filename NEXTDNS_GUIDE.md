# Hướng dẫn cấu hình Chặn Thu Hồi (Anti-Revoke) trên NextDNS

Để Locket Gold (và các app cài ngoài khác) không bị Apple thu hồi chứng chỉ, bạn cần chặn các máy chủ kiểm tra của Apple.

**LƯU Ý QUAN TRỌNG:**
Trong ảnh bạn gửi, bạn đang chặn `*.locket.com`... -> **HÃY XÓA NGAY**. Việc này sẽ khiến bạn không thể nhắn tin hay xem ảnh trên Locket được.

## Các bước thực hiện đúng:

1.  Truy cập [Tab Danh sách đen (Denylist)](https://my.nextdns.io/8cb53e/denylist).
2.  **Xóa** các dòng liên quan đến `locket` mà bạn vừa thêm.
3.  **Thêm mới** các tên miền sau đây (copy và paste vào ô "Thêm tên miền..."):

```text
ocsp.apple.com
ocsp2.apple.com
ppq.apple.com
crl.apple.com
certs.apple.com
vpp.itunes.apple.com
```

## Giải thích:
- Các tên miền trên là máy chủ của Apple dùng để kiểm tra xem ứng dụng có hợp lệ không.
- Khi chặn chúng, điện thoại sẽ không thể "hỏi" Apple, và do đó Apple không thể "nói" rằng ứng dụng này đã bị thu hồi -> App vẫn mở được.

## Kiểm tra:
Sau khi thêm, danh sách đen của bạn nên trông giống như danh sách các tên miền của Apple, KHÔNG PHẢI tên miền của Locket.
