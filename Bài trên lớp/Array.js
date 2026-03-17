/*Mảng (Array) là một kiểu dữ liệu đặc biệt trong JS, dùng để lưu trữ nhiều giá trị trong một biến duy nhất.
- Mỗi giá trị trong mảng được gọi là một phần tử (element).
- Mỗi phần tử có chỉ số (index) bắt đầu từ 0.
* Cú pháp:
1. Cách ngắn gọn:
let numbers = [1, 2, 3, 4, 5];  =>  Khuyên dùng

2. Dùng từ khóa new Array:
let numbers = new Array(1, 2, 3, 4, 5);*/

let ban_be = ["An", "Dũng", "Bằng", "Việt", "Thành"];
console.log(ban_be);

console.log(ban_be[0]);
console.log(ban_be[1]);
console.log(ban_be[2]);
console.log(ban_be[3]);
console.log(ban_be[4]);

for(let i = 0; i <= ban_be.length; i += 2){
    console.log(ban_be[i]);
}

for(let ban of ban_be){
    console.log(ban);
}

ban_be[0] = "Anh";  //thay đổi phần tử
ban_be[ban_be.length] = "Đức";  //thêm phần tử mới
console.log(ban_be);

ban_be.push("Hoàng");  //thêm một hay nhiều phần tử vào cuối
console.log(ban_be);

ban_be.pop();  //xóa phần tử cuối
console.log(ban_be);

ban_be.shift();  //xóa phần tử đầu
console.log(ban_be);

ban_be.unshift("Yến");  //thêm một hay nhiều phần tử đầu
console.log(ban_be);

console.log(ban_be.length);  //độ dài mảng

console.log(ban_be.indexOf("Bằng"));  //tìm vị trí phần tử

let score = [["An",9],["Bình",7],["Chi",10]];  //mảng lồng nhau
console.log(score[0][1]);
console.log(score[1][0]);
console.log(score[2].at(-1));  //Hàm at() để truyền index (có thể cả index âm)

console.log(ban_be.join('-'));  //Hàm join nối các giá trị mảng thành một chuỗi (mặc định ngăn cách bằng dấu ,)

console.log(ban_be.concat(score));  //Hàm concat dùng để nối mảng

console.log(ban_be.slice(1,3));  //Hàm slice dùng để lấy một hoặc nhiều phần tử ra khỏi mảng (lấy ra kiểu dữ liệu array)

console.log(ban_be.reverse());  //Hàm reverse đảo ngược mảng

let numbers = [7, 1, 8, 6, 2, 3, 4, 9, 5, 10];
console.log(numbers.sort(function(a,b){
    return a - b
}));  //Hàm sort sắp xếp lại mảng theo giá trị tăng dần (với kiểu giá trị number)
console.log(ban_be.sort());  //Sắp xếp theo thứ tự Alphabet (với kiểu giá trị string)
console.log(score.sort());  //Tự biến đổi các mảng con thành một giá trị duy nhất 