//Bài tập học OOP (Gemini)
class User{
    #username
    constructor(username){
        this.#username = username;
    }
    login(){
        this.#checkDatabase();
        console.log(`Người dùng có tên ${this.#username}`)
    }
    #checkDatabase(){
        console.log('Đang kiểm tra dữ liệu...');
    }
    get name(){
        return this.#username;
    }
}

class Admin extends User{
    constructor(username){
        super(username);
       
    }
    deletePost(){
        console.log('Đã xóa bài viết');
    }
    login() {
        super.login(); 
        console.log(`Quản trị viên tối cao ${this.name} đã đăng nhập hệ thống`);
    }
}

const admin = new Admin('abc');
console.log(admin.name);
admin.login();