/*Toán tử là các kí hiệu đặc biệt giúp JavaScript thực hiện các phép toán trên dữ liệu.
- Mỗi toán tử kết hợp với một hoặc nhiều toán hạng (operand) để tạo ra kết quả.*/


//Toán tử số học:
let a = 3;
let b = 5;
console.log(a + b);  /* Dấu + là toán tử cộng; a, b là các toán hạng*/
console.log(a - b);  //Trừ
console.log(a * b);  //Nhân
console.log(a / b);  //Chia
console.log(a % b);  //Chia lấy dư
console.log(a --);  // --: Trừ một đơn vị
console.log(a ++);  // ++: Cộng một đơn vị


//Toán tử gán:
let y = 10;
y += 5;
console.log(y)  //15
/*Các toán tử gán:
= -> x=10 -> Gán 10 cho x
+= -> x+=10 -> x = x+10
-= -> x-=10 -> x = x-10
*= -> x*=10 -> x = x*10
/= -> x/=10 -> x = x/10*/


//Toán tử so sánh:
/*Dùng để so sánh hai giá trị, kết quả luôn trả về là true hoặc false*/
let c = 5, d = "5";
console.log(c==d);  //Bằng (so sánh giá trị)  => true
console.log(c===d);  //Bằng tuyệt đối (so sánh cả kiểu và giá trị)  => false
console.log(c!==d);  //Khác tuyệt đối  => true
/*Còn các toán tử khác: != , > , < , >= , <= */


//Toán tử logic:
tuoi = 20;
console.log(tuoi>18 && tuoi>30);  //AND(Và)  => false
console.log(tuoi>18 || tuoi>30);  //OR(Hoặc)  => true
console.log(!tuoi>18);  //NOT(Phủ định)  => false


//Toán tử chuỗi:
let ten ="Dũng";
let loichao = "Xin chào" + ten;  //Dấu + được dùng để nối chuỗi
console.log(loichao);  //Kết quả: Xin chàoDũng


//Toán tử đặc biệt:
console.log(typeof(20));  //typeof: Dùng để kiểm tra kiểu dữ liệu  => number
console.log(typeof null);  // => object
let diem = 8;
let thongbao = (diem>=8)? "Đủ điểm":"Chưa đủ điểm";
console.log(thongbao);  //điều kiện