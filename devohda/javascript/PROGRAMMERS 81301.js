function solution(s) {
    let answer = "";

    for(let i = 0; i < s.length; i++){
        if(s[i] === 'z'){
            i += 3;
            answer += '0';
        }else if(s[i] === 'o'){
            i += 2;
            answer += '1';
        }else if(s[i] === 't'){
            if(s[i+1] === 'w'){
                i += 2;
                answer += '2';
            }else{
                i += 4;
                answer += '3';
            }
        }else if(s[i] === 'f'){
            if(s[i+1] === 'o'){
                i += 3;
                answer += '4';
            }else{
                i += 3;
                answer += '5';
            }
        }else if(s[i] === 's'){
            if(s[i+1] === 'i'){
                i += 2;
                answer += '6';
            }else{
                i += 4;
                answer += '7';
            }
        }else if(s[i] === 'e'){
            i += 4;
            answer += '8';
        }else if(s[i] === 'n'){
            i += 3;
            answer += '9';
        }else{
            answer += s[i]
        }
    }

    return parseInt(answer);
}