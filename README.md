# Nginx-Reverse-Proxy-Flask-App
**Cấu hình Reverse Proxy trên Nginx**
1. Reverse Proxy là gì?
Đối lập với forward proxy, đây là một loại proxy phía server. Server đóng vai trò làm reverse proxy sẽ chắn trước các request từ client đẩy đến và che dấu toàn bộ backend server đằng sau.
2. Mục đích sử dụng:
- Load Balancing: Như theo sơ đồ trên, Reverse Proxy sẽ nhận request, phân bố cho Server tương ứng, nhận kết quả và trả về cho client.
- Web Acceleration: Reverse Proxy có thể được dùng cho việc nén dữ liệu inbound và outbound, cũng như cache lại các request nhằm giảm dung lượng dữ liệu và tăng tốc độ cho cả phía client lẫn server.
- Bảo mật và ẩn danh: Reverse Proxy có thể được dùng như một tường lửa đơn giản để block hoặc filter các bad-request.
3. Cài đặt Nginx:
  Tham khảo link: https://nginx.org/en/download.html
4. Một số câu lệnh cơ bản để thao tác với Nginx
a. Khởi động Nginx
- start nginx
b. Dừng hoạt động Nginx
- start nginx
c. Khởi động lại Nginx
- restart nginx
d. Kiểm tra trạng thái của Nginx
- status nginx
5. Cấu hình Reverse Proxy trên Nginx
Bước 1: Vào thư mục conf -> nginx.conf ta tiến hành cấu hình như ảnh:
Hiện tại mình đang dùng Flask app. Bạn có thể sử dụng các Framework khác để thử Reverse Proxy trên Nginx nhé!
![image](https://github.com/tanvinhluong/Nginx-Reverse-Proxy-Flask-App/assets/94514193/09ebfcf9-4389-4c2a-b004-6ca2c7305149)
