/*Vòng lặp for:
Cấu trúc for là loại vòng lặp được dùng phổ biến nhất, thường khi biết trước số lần lặp.
Cú pháp:
for (khởi_tạo; điều_kiện; bước_nhảy){
    // khối lệnh lặp
}
    Trong đó:
        khởi_tạo: Tạo biến đếm ban đầu (ví dụ: let i = 1).
        điều_kiện: Xác định khi nào vòng lặp dừng lại (ví dụ: i <= 5). => Vòng lặp sẽ chạy khi nào còn thỏa mãn điều kiện.
        bước_nhảy: Tăng hoặc giảm biến đếm (ví dụ: i++).*/
for(let i = 1; i <= 9; i += 2){
    console.log("Lần lặp thứ", (i+1)/2);
}


/*Vòng lặp while:
Vòng lặp while dùng khi chưa biết trước số lần lặp.
Chỉ cần điều kiện còn đúng (true), chương trình sẽ tiếp tục.
Cú pháp:
while (điều_kiện){
    // khối lệnh lặp
}
    Trong đó:
        điều_kiện => Vòng lặp sẽ chạy khi nào còn thỏa mãn điều kiện.*/
let a = 1;
let sum = 0;
while(a<=10){
    sum += a;
    a ++;
}
console.log("Tổng từ 1 đến 10:", sum);


/*Vòng lặp do...while:
Vòng lặp do...while luôn thực hiện ít nhất một lần lặp, dù điều kiện đúng hay sai. => Cần chạy ít nhất một lần lặp.
Cú pháp:
do{
    // khối lệnh lặp
} while (điều_kiện);*/
let diem = 0;
do{
    console.log("Trượt rồi");
} while(diem > 0);