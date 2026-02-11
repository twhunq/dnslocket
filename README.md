# Hướng dẫn sử dụng Server MobileConfig

Để quản lý và chặn người dùng cụ thể, bạn cần sửa dụng link riêng.

**Link trang chủ (Link chung) đã bị vô hiệu hóa.**

## Link riêng cho từng người
Cấu trúc link:
`https://dnslocket.vercel.app/dp/TenNguoiDung`

Ví dụ:
- Cho bạn Tùng: `https://dnslocket.vercel.app/dp/Tung`
- Cho bạn Hoa: `https://dnslocket.vercel.app/dp/Hoa`
- Cho khách: `https://dnslocket.vercel.app/dp/Khach1`

### Cách chặn người dùng:
1. Vào trang quản trị NextDNS (ID `8cb53e`).
2. Mục **Logs** hoặc **Analytics**.
3. Bạn sẽ thấy tên thiết bị hiện lên là `LOCKET GOLD - Tung`, `LOCKET GOLD - Hoa`...
4. Bạn có thể lọc và chặn theo tên thiết bị hoặc profile ID tương ứng.

---

## Cài đặt & Cập nhật
Mỗi khi sửa code, bạn cần chạy lệnh sau để cập nhật lên Vercel:

```bash
git add .
git commit -m "disable general link"
git push
```
