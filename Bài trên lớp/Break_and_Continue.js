for (let i = 1; i <= 10; i++){
    console.log("Từ khóa break lần thứ", i);
    if (i == 5){
        break;
    }
} //Dùng break để dừng vòng lặp khi đạt đến điều kiện nào đó

for (let a = 1; a <= 10; a ++){
    if (a == 5){
        continue;
    }
    console.log("Từ khóa continue lần thứ", a);
} ///Dùng continue để vòng lặp bỏ qua trường hợp với điều kiện nào đó