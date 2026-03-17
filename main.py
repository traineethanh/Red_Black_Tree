import sys
import os
import io
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from src.rbt_tree import RedBlackTree

def show_menu():    
    print("\n--- CHƯƠNG TRÌNH CÂY ĐỎ ĐEN (RED-BLACK TREE) ---")
    print("1. Thêm phần tử vào cây")
    print("2. Tìm kiếm một giá trị")
    print("3. Duyệt cây (In-order)")
    print("4. Thoát")
    print("------------------------------------------------")

def main():
    tree = RedBlackTree()
    
    while True:
        show_menu()
        choice = input("Lựa chọn của bạn (1-4): ")

        if choice == '1':
            try:
                line = input("Nhập các số muốn thêm (cách nhau bằng dấu phẩy hoặc khoảng trắng): ")
                import re
                values = re.split(r'[,\s]+', line.strip())
                
                for v in values:
                    if v:
                        val = int(v)
                        tree.insert(val)
                        print(f"Đã thêm {val} thành công!")
            except ValueError:
                print("Lỗi: Có giá trị không phải là số nguyên!")

        elif choice == '2':
            val = int(input("Nhập giá trị cần tìm: "))
            node = tree.search_tree_helper(tree.root, val)
            if node != tree.TNULL:
                color = "Đỏ" if node.color == 1 else "Đen"
                print(f"Tìm thấy {val}! Node này có màu: {color}")
            else:
                print(f"Không tìm thấy {val} trong cây.")

        elif choice == '3':
            print("Cấu trúc cây hiện tại (In-order):")
            tree.print_tree() 

        elif choice == '4':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()