Product_list = [
    {
        "id_product": "HD001",
        "name_product": "Ban Phim Co Corsair",
        "price_product": 1800000,
        "quantity_product": 2,
        "sale_price": 200000,
        "total_price": 3740000.0,
        "ranking": "Vừa" 
    }
]

# Hàm tổng tiền thực thanh thanh toán bao gồm 10% VAT
# item ở đây là một dictionary đơn lẻ
def total_price(item):
    total = ((item['price_product'] * item['quantity_product']) - item['sale_price']) * 1.1
    return total

# Hàm phân loại giá trị hóa đơn
def type_ranking(total_val):
    if total_val < 1_000_000:
        return "Nhỏ"
    elif 1_000_000 <= total_val < 5_000_000:
        return "Vừa"
    elif 5_000_000 <= total_val < 15_000_000:
        return "Lớn"
    elif total_val >= 15_000_000:
        return "Cao cấp"
    else:
        return "Lỗi!"

# Case 1: Hiển thị danh sách hóa đơn
def display_product(lst):
    if len(lst) == 0:
        print("Danh sách hóa đơn đang trống!")
        return

    for item in lst:
        print(f"""
    Mã sản phẩm: {item['id_product']}
    Tên sản phẩm: {item['name_product']}
    Giá sản phẩm: {item['price_product']}
    Số lượng sản phẩm: {item['quantity_product']}
    Số tiền giảm giá (Voucher): {item['sale_price']}
    Tổng tiền hóa đơn: {item['total_price']}
    Phân loại giá trị hóa đơn: {item['ranking']}
""")

# Case 2: Thêm mới hóa đơn
def add_product(lst):
    while True:
        new_id = input("Nhập mã đơn hàng mới: ").strip().upper()
        if new_id == "":
            print("Mã đơn hàng không được để trống!")
            continue
        
        # Kiểm tra trùng ID trong danh sách
        is_duplicate = False
        for item in lst:
            if item['id_product'] == new_id:
                is_duplicate = True
                break
        if is_duplicate:
            print("Mã đơn hàng bị trùng, vui lòng nhập lại!")
            continue
        break

    while True:
        new_name = input("Nhập tên sản phẩm mới: ").strip().title()
        if new_name == "":
            print("Tên sản phẩm mới không được để trống!")
            continue
        break

    while True:
        price_str = input("Nhập giá tiền cho sản phẩm mới: ").strip()
        if price_str == "" or not price_str.isdigit() or int(price_str) <= 0:
            print("Giá tiền không hợp lệ (phải là số nguyên dương và không để trống)!")
            continue
        new_price = int(price_str)
        break

    while True:
        qty_str = input("Nhập số lượng sản phẩm cho sản phẩm mới: ").strip()
        if qty_str == "" or not qty_str.isdigit() or int(qty_str) <= 0:
            print("Số lượng không hợp lệ (phải là số nguyên dương và không để trống)!")
            continue
        new_quantity = int(qty_str)
        break

    while True:
        sale_str = input("Nhập tiền giảm giá cho sản phẩm mới: ").strip()
        if sale_str == "" or not sale_str.isdigit() or int(sale_str) < 0:
            print("Giá tiền giảm giá không hợp lệ (phải là số nguyên và không âm)!")
            continue
        new_sale_price = int(sale_str)
        break

    temp_item = {
        "price_product": new_price,
        "quantity_product": new_quantity,
        "sale_price": new_sale_price
    }
    calc_total = total_price(temp_item)
    calc_ranking = type_ranking(calc_total)

    new_product = {
        "id_product": new_id,
        "name_product": new_name,
        "price_product": new_price,
        "quantity_product": new_quantity,
        "sale_price": new_sale_price,
        "total_price": calc_total,
        "ranking": calc_ranking
    }
    
    lst.append(new_product)
    print(f"Đã thêm đơn hàng mới có ID: {new_id}")

# Case 3: Cập nhật hóa đơn
def update_product(lst):
    while True:
        update_id = input("Nhập ID đơn hàng cần cập nhật: ").strip().upper()
        if update_id == "":
            print("Mã đơn hàng cần cập nhật không được để trống!")
            continue
        
        # Tìm kiếm sản phẩm theo ID
        found_item = None
        for item in lst:
            if item['id_product'] == update_id:
                found_item = item
                break
        
        if found_item is None:
            print("Không tìm thấy ID đơn hàng cần cập nhật!")
            continue
        else:
            print("Đã tìm thấy ID cần cập nhật!")
            
            while True:
                update_name = input("Nhập tên sản phẩm cần cập nhật: ").strip().title()
                if update_name == "":
                    print("Tên sản phẩm cập nhật không được để trống!")
                    continue
                break

            while True:
                price_str = input("Nhập giá tiền mới: ").strip()
                if price_str == "" or not price_str.isdigit() or int(price_str) <= 0:
                    print("Giá tiền không hợp lệ!")
                    continue
                update_price = int(price_str)
                break

            while True:
                qty_str = input("Nhập số lượng mới: ").strip()
                if qty_str == "" or not qty_str.isdigit() or int(qty_str) <= 0:
                    print("Số lượng không hợp lệ!")
                    continue
                update_quantity = int(qty_str)
                break

            while True:
                sale_str = input("Nhập tiền giảm giá mới: ").strip()
                if sale_str == "" or not sale_str.isdigit() or int(sale_str) < 0:
                    print("Tiền giảm giá không hợp lệ!")
                    continue
                update_sale_price = int(sale_str)
                break

            found_item['name_product'] = update_name
            found_item['price_product'] = update_price
            found_item['quantity_product'] = update_quantity
            found_item['sale_price'] = update_sale_price
            found_item['total_price'] = total_price(found_item)
            found_item['ranking'] = type_ranking(found_item['total_price'])
            
            print(f"Đã cập nhật thành công đơn hàng có ID: {update_id}")
            break

# Case 4: Hủy hóa đơn lỗi và confirm y/n
def delete_product(lst):
    while True:
        delete_id = input("Nhập ID đơn hàng cần xóa: ").strip().upper()
        if delete_id == "":
            print("Mã đơn hàng không được để trống!")
            continue
        
        found_item = None
        for item in lst:
            if item['id_product'] == delete_id:
                found_item = item
                break
                
        if found_item is None:
            print("Không tìm thấy ID đơn hàng cần xóa!")
            return
        
        # Xác nhận Y/N
        confirm = input(f"Bạn có chắc muốn xóa hóa đơn {delete_id} không? (Y/N): ").strip().upper()
        if confirm == 'Y':
            lst.remove(found_item)
            print(f"Xóa thành công hóa đơn: {delete_id}")
        else:
            print("Đã hủy thao tác xóa.")
        break

# Case 5: Tìm kiếm hóa đơn
def find_product(lst):
    while True:
        print("""
            1. Tìm kiếm theo ID đơn hàng.
            2. Tìm kiếm theo tên.
            3. Trở về menu chính.
    """)
        choice = input("Nhập lựa chọn của bạn: ").strip()
        if choice not in ['1', '2', '3']:
            print("Nhập sai lựa chọn vui lòng nhập lại!")
            continue
        
        choice = int(choice)
        if choice == 3:
            return

        found = False
        if choice == 1:
            search_id = input("Nhập ID đơn hàng cần tìm: ").strip().upper()
            for item in lst:
                if item['id_product'] == search_id:
                    print(f"--- Kết quả tìm thấy cho ID {search_id} ---")
                    print(f"Tên: {item['name_product']} | Tổng tiền: {item['total_price']} | Phân loại: {item['ranking']}")
                    found = True
            if not found:
                print("Không tìm thấy hóa đơn nào khớp với ID yêu cầu.")

        elif choice == 2:
            search_name = input("Nhập tên sản phẩm cần tìm: ").strip().lower()
            print(f"--- Kết quả tìm thấy cho tên chứa '{search_name}' ---")
            for item in lst:
                if search_name in item['name_product'].lower():
                    print(f"ID: {item['id_product']} | Tên: {item['name_product']} | Tổng tiền: {item['total_price']}")
                    found = True
            if not found:
                print("Không tìm thấy hóa đơn nào khớp với tên yêu cầu.")

# Case 6: Đếm và hiển thị số lượng đơn Cao cấp, Lớn, Vừa, Nhỏ
def count_product(lst):
    small = 0
    medium = 0
    big = 0
    vip = 0
    
    for item in lst:
        if item['ranking'] == "Nhỏ":
            small += 1
        elif item['ranking'] == "Vừa":
            meidum += 1
        elif item['ranking'] == "Lớn":
            big += 1
        elif item['ranking'] == "Cao cấp":
            vip += 1

    print("===== THỐNG KÊ PHÂN LOẠI HÓA ĐƠN =====")
    print(f"Số lượng đơn Nhỏ:     {small}")
    print(f"Số lượng đơn Vừa:     {medium}")
    print(f"Số lượng đơn Lớn:     {big}")
    print(f"Số lượng đơn Cao cấp: {vip}")
    print("======================================")

def main():
    while True:
        print("""
    ===== QUẢN LÝ SẢN PHẨM =====
    1. Hiển thị danh sách hóa đơn
    2. Lập hóa đơn mới tại quầy
    3. Cập nhật thông tin hóa đơn
    4. Hủy hóa đơn lỗi
    5. Tìm kiếm hóa đơn
    6. Thống kê phân loại doanh thu
    7. Phân loại hóa đơn tự động (Cập nhật lại rank toàn bộ list)
    8. Thoát chương trình
""")
        choice = int(input("Mời bạn nhập lựa chọn: ")).strip()
        if choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("Lựa chọn không hợp lệ! Vui lòng nhập từ 1 đến 8.")
            continue
            
        match choice:
            case 1:
                display_product(Product_list)
            case 2:
                add_product(Product_list)
            case 3:
                update_product(Product_list)
            case 4:
                delete_product(Product_list)
            case 5:
                find_product(Product_list)
            case 6:
                count_product(Product_list)
            case 7:
                break
            case 8:
                print("Thoát chương trình!")
                break

main()
