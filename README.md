# Hướng dẫn sử dụng Server MobileConfig

## Cách 1: Link chung (Cũ)
- Truy cập thẳng vào domain: `https://dnslocket.vercel.app`
- ID NextDNS đang dùng: `8cb53e` (Của bạn)

## Cách 2: Link riêng cho từng người (Mới - Khuyên dùng)
Để quản lý và chặn người dùng cụ thể, hãy gửi cho mỗi người một link riêng biệt.

Cấu trúc link:
`https://dnslocket.vercel.app/dp/TenNguoiDung`

Ví dụ:
- Cho bạn Tùng: `https://dnslocket.vercel.app/dp/Tung`
- Cho bạn Hoa: `https://dnslocket.vercel.app/dp/Hoa`
- Cho khách: `https://dnslocket.vercel.app/dp/Khach1`

### Cách chặn người dùng:
1. Vào trang quản trị NextDNS (ID `8cb53e`).
2. Mục **Logs** hoặc **Analytics**.
3. Bạn sẽ thấy tên thiết bị hiện lên là `LOCKET GOLD - Tung`, `LOCKET GOLD - Hoa`... thay vì chung chung.
4. Bạn có thể lọc và chặn theo tên thiết bị hoặc profile ID tương ứng.

---

## Cài đặt & Cập nhật
Mỗi khi sửa code, bạn cần chạy lệnh sau để cập nhật lên Vercel:

```bash
git add .
git commit -m "update user id and guide"
git push
```
