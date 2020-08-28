try:
    nCoV
except NameError:
        print("Không tồn tại nCoV")
else:
    print("Tồn tại nCoV")
    del nCoV
    print("Đã xóa nCoV")