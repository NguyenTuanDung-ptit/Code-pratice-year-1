let tuoi = 20;
let diem = 8.5;
console.log(tuoi + diem);  //number(Dùng để biểu diễn các giá trị số học)

let ten = 'Dũng';
console.log("Xin chào" + ten);
console.log(`Xin chào, mình là ${ten}`);  //string(Là dãy ký tự nằm trong dấu '' hoặc "")

let DaHoc = true;
console.log(DaHoc);  //boolean(Chỉ có 2 giá trị true hoặc false)

let x;
console.log(x);  //undefined(Xảy ra khi biến được khai báo nhưng chưa được gán giá trị)

let nguoi_yeu_cu = null;
console.log(nguoi_yeu_cu);  //null(Tạo ra biến nhưng gán sẵn giá trị là null)

let sinh_vien = {
    ten: "Minh",
    tuoi: 18,
    da_tot_nghiep: false
};
console.log(sinh_vien.ten);  //object - Đối tượng(Dùng để lưu nhiều thông tin liên quan trong một biến)

let ngon_ngu = ["HTML", "CSS", "JS"];
console.log(ngon_ngu[2]);  //array - Mảng(Dùng để lưu nhiều giá trị trong một biến)




//Một số câu lệnh, cú pháp cơ bản:
console.log(typeof 20) //typeof: Kiểm tra kiểu dữ liệu