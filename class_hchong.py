class book:
    def __init__(self, ten, tacgia, trang):
        print("Book creater")
        self.ten = ten
        self.tacgia = tacgia
        self.trang = trang
    def __str__(self):
        return ("Title: %s, Author: %s, Pages: %s"%(self.ten, self.tacgia, self.trang))
    def __len__(self):
        return self.ten

b = book("sach123", "Quang Vinh ", 2000)
print(b)
print(len(b))