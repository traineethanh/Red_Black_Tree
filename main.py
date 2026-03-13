import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.rbt_tree import RedBlackTree

def show_menu():
    print("\n--- CHƯƠNG TRÌNH CÂY ĐỎ ĐEN (RED-BLACK TREE) ---")
    print("1. Thêm phần tử vào cây")
    print("2. Tìm kiếm một giá trị")
    print("3. Xóa một phần tử (Coming soon)")
    print("4. Duyệt cây (In-order)")
    print("5. Thoát")
    print("------------------------------------------------")

def main():
    tree = RedBlackTree()
    
    while True:
        show_menu()
        choice = input("Lựa chọn của bạn (1-5): ")

        if choice == '1':
            try:
                val = int(input("Nhập giá trị muốn thêm: "))
                tree.insert(val)
                print(f"Đã thêm {val} vào cây.")
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên!")

        elif choice == '2':
            val = int(input("Nhập giá trị cần tìm: "))
            node = tree.search_tree_helper(tree.root, val)
            if node != tree.TNULL:
                color = "Đỏ" if node.color == 1 else "Đen"
                print(f"Tìm thấy {val}! Node này có màu: {color}")
            else:
                print(f"Không tìm thấy {val} trong cây.")

        elif choice == '3':
            print("Chức năng xóa đang được cập nhật...")

        elif choice == '4':
            print("Cấu trúc cây hiện tại (In-order):")
            # Giả sử bạn đã viết hàm này trong RedBlackTree
            tree.print_tree() 

        elif choice == '5':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()