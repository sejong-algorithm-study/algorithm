function solution(new_id) {
    let str = new_id.toLowerCase();

    const reg2 = /[^0-9a-z\-_\.]/g;
    str = str.replace(reg2, "");

    const reg3 = /\.+/g;
    str = str.replace(reg3,".");

    const reg4 = /^[\.]|[\.]$/g;
    str = str.replace(reg4, "");

    if(!str) str = "a";

    const reg6 = /[\.]$/g;
    str = str.substring(0, 15).replace(reg6, "");

    const len = str.length;
    if(len <= 2){
        for(let i = 0; i < 3 - len; i++){
            str += str.substring(str.length-1);
        }
    }

    return str;
}