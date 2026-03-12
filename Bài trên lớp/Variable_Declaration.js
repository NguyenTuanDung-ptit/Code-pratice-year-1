//var:
var tuoi = 18;
var tuoi = 20;
console.log(tuoi);  //20

/*Cách khai báo biến var (cách cũ):
1.Biến có phạm vi toàn hàm (Function scope)
2.Có thể khai báo được nhiều lần mà không báo lỗi
3.Hiện tượng Hoisting (Đưa phần khai báo biến lên đầu phạm vi nhưng giá trị ban đầu sẽ là undefined)*/



//let:
let x = 10;
if(true){
    let x = 20;
    console.log(x);
}  //20
console.log(x)  //10

/*Cách khai báo biến let (cách hiện đại hơn):
1.Biến có phạm vi khối (Block scope) 
2.Biến chỉ tồn tại trong cặp {} được khai báo
3.Không thể khai báo lại biến (nếu khai báo lại trình duyệt sẽ báo lỗi ngay)
=> Dùng cho biến thay đổi*/



//const:
const PI = 3.14;
console.log(PI);  //3.14
const nguoi = {
    tuoi: 20,
    hoten: "Nguyen Van A",
}
nguoi.tuoi = 22;
console.log(nguoi.tuoi);  //22

/*Cách khai báo biến const (hằng số):
1.Tạo ra một giá trị không thay đổi (tuy nhiên vẫn có thể thay đổi giá trị trong các biến có kiểu dữ liệu object và array)
2.Biến chỉ tồn tại trong cặp {} được khai báo
=> Dùng cho giá trị cố định*/