# Hướng dẫn sử dụng Server MobileConfig

Để tự động tải `KM.mobileconfig` khi truy cập domain:

## Cách 1: Chạy Local (Khi bật máy tính)
1. **Chạy Server:**
   Mở terminal tại thư mục này và chạy lệnh:
   ```bash
   python start_server.py
   ```
   Server sẽ chạy tại `http://localhost:8000`.

2. **Cấu hình Domain:**
   - Trỏ domain của bạn về địa chỉ IP của máy tính chạy server này.
   - Nếu chạy trên máy cá nhân sau router/modem, bạn cần **Port Forward** cổng 8000 trên router về IP máy tính của bạn.

## Cách 2: Chạy Online 24/7 (Khuyên dùng)
Để link hoạt động ngay cả khi tắt máy tính, bạn cần deploy lên server cloud. **Vercel** là giải pháp miễn phí và dễ nhất.

1. **Chuẩn bị:**
   - Thư mục này đã có sẵn file `vercel.json` để cấu hình tự động.
   - Đảm bảo file `KM.mobileconfig` nằm cùng thư mục.

2. **Deploy lên Vercel:**
   - **Cách 1 (Dễ nhất):** Cài đặt [Vercel CLI](https://vercel.com/cli) rồi chạy lệnh `vercel` tại thư mục này.
   - **Cách 2:** Đẩy thư mục này lên GitHub/GitLab, sau đó vào [Vercel.com](https://vercel.com) import repo vừa tạo.

3. **Truy cập:**
   - Vercel sẽ cấp cho bạn một domain (ví dụ: `du-an-cua-ban.vercel.app`).
   - Vào domain đó trên iPhone/iPad, profile sẽ tự động tải về.

## Lưu ý kỹ thuật
File `vercel.json` hoặc `start_server.py` đều có nhiệm vụ quan trọng là thêm header:
- `Content-Type: application/x-apple-aspen-config`
- `Content-Disposition: attachment; filename="KM.mobileconfig"`
Điều này giúp iOS nhận diện đây là profile cài đặt chứ không phải một file text bình thường.
