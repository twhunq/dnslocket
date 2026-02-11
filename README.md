# Hướng dẫn sử dụng Server MobileConfig

Để quản lý và chặn người dùng cụ thể, bạn cần sử dụng link có kèm ID.

**Link trang chủ (Link chung) đã bị vô hiệu hóa.**

## Hướng dẫn tạo Link (Bắt buộc dùng ID)

Bạn cần tạo ID trên NextDNS trước, sau đó gắn vào link.

**Bước 1:** Vào NextDNS tạo Hồ sơ mới -> Lấy ID mới (ví dụ: `112233`).
**Bước 2:** Cấu hình chặn thu hồi (xem file `NEXTDNS_GUIDE.md`) cho hồ sơ đó.
**Bước 3:** Gửi link cho khách theo cấu trúc: `.../dp/TenKhach?id=ID`

Cấu trúc: `https://dnslocket.vercel.app/dp/TenKhach?id=ID_CUA_BAN`

Ví dụ:
- Khách A dùng ID `112233`: `https://dnslocket.vercel.app/dp/KhachA?id=112233`
- Khách B dùng ID `224466`: `https://dnslocket.vercel.app/dp/KhachB?id=224466`

### Cách hủy dịch vụ:
- Vào NextDNS -> Chọn hồ sơ tương ứng.
- Xóa hồ sơ đó đi HOẶC vào chặn Locket trong hồ sơ đó.
- Toàn bộ khách dùng ID đó sẽ bị ngắt kết nối.

---

## Cài đặt & Cập nhật
Mỗi khi sửa code, bạn cần chạy lệnh sau để cập nhật lên Vercel:

```bash
git add .
git commit -m "update code"
git push
```
