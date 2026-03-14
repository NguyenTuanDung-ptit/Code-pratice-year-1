/*CẤU TRÚC IF:
Cách máy tính ra quyết định.
Cú pháp: if (điều kiệu) {đoạn mã được thực thi khi điều kiện đúng}
=> Nếu sai đoạn mã sẽ bị bỏ qua và tiếp tục chương trình.*/
let tuoi = 20;
if(tuoi>=18){
    console.log("Bạn đã đủ tuổi trưởng thành");
}


/*CẤU TRÚC IF-ELSE:
Nếu đúng thì làm A, nếu sai thì làm B.
Cú pháp: 
if(điều kiện){
    khi điều kiện đúng
} else{
    khi điều kiện sai    
}*/
let gio = 9;
if(gio<12){
    console.log("Chào buổi sáng");
} else{
    console.log("Chào buổi chiều");
}


/*CẤU TRÚC IF ELSE IF ELSE:
Nhiều điều kiện.
Cú pháp:
if(điều kiện 1){
    // ..
} else if(điều kiện 2){
    // ..
} else{
    // ..
}*/


/*CẤU TRÚC SWITCH CASE:
Khi có nhiều trường hợp cụ thể rõ ràng.
Ví dụ: Các ngày trong tuần.
Có thể dùng switch case thay cho if else.
Cú pháp:
switch(biến){
    case giá_trị_1:
        // code khi biến == giá_trị_1
        break;
    case giá_trị_2:
        // code khi biến == giá_trị_2
        break;
    default:
        // code khi không khớp trường hợp nào
}*/
let ngay = 8;
switch(ngay){
    case 1:
        console.log("Thứ 2");
        break;
    case 2:
        console.log("Thứ 3");
        break;
    case 3:
        console.log("Thứ 4");
        break;
    case 4:
        console.log("Thứ 5");
        break;
    case 5:
        console.log("Thứ 6");
        break;
    case 6:
        console.log("Thứ 7");
        break;
    case 7:
        console.log("Chủ nhật");
        break;
    default:
        console.log("Không hợp lý");
}