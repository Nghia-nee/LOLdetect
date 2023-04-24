import os

# Thay đổi đường dẫn thư mục cần tìm kiếm
directory = 'D:\Desktop\LOLBAS'

# Khởi tạo danh sách tên file
file_list = []

def get_files(directory):
    # Duyệt qua tất cả các file và thư mục trong thư mục hiện tại
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Lọc ra các file có đuôi là .md
            if file.endswith('.md'):
                # Thêm tên file vào danh sách
                file_list.append(os.path.splitext(file)[0])

# Lấy danh sách tất cả các file trong thư mục, bao gồm cả các file trong các thư mục con
get_files(directory)

# Tạo một file .txt mới và lưu tên các file đã lấy được vào file này
with open('filtered.txt', 'w') as f:
    for file in file_list:
        f.write(file + '\n')
