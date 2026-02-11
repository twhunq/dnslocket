# Hướng dẫn sử dụng Server MobileConfig

Để quản lý và chặn người dùng cụ thể, bạn cần sử dụng link có kèm ID.

**Link trang chủ (Link chung) đã bị vô hiệu hóa.**

## Hướng dẫn tạo Link nhanh
**Cấu trúc:** `https://dnslocket.vercel.app/ID_CUA_BAN`

**Bước 1:** Vào NextDNS tạo Hồ sơ mới -> Lấy ID mới (ví dụ: `ce1376` hoặc `112233`).
**Bước 2:** Cấu hình chặn thu hồi cho hồ sơ đó (xem file `NEXTDNS_GUIDE.md`).
**Bước 3:** Gửi thẳng ID cho khách.

Ví dụ:
- Khách dùng ID `ce1376`: `https://dnslocket.vercel.app/ce1376`
- Khách dùng ID `112233`: `https://dnslocket.vercel.app/112233`

### Cách quản lý:
- Vào NextDNS -> Chọn hồ sơ tương ứng.
- Trong phần Logs, tên thiết bị sẽ hiện là `LOCKET GOLD - ID`.
- Muốn cắt mạng -> Xóa hồ sơ đó đi HOẶC vào chặn Locket trong hồ sơ đó.

---

## Cài đặt & Cập nhật
Mỗi khi sửa code, bạn cần chạy lệnh sau để cập nhật lên Vercel:

```bash
git add .
git commit -m "update code"
git push
```
