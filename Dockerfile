# Sử dụng hình ảnh cơ bản Python
FROM python:3.12-slim

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép file requirement nếu có, hoặc tạo chúng thủ công
COPY requirements.txt requirements.txt

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở port cho ứng dụng Gradio
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"
# Lệnh chạy ứng dụng
CMD ["python", "app.py"]
