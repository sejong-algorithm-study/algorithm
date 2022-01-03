function solution(numbers, hand) {
    let answer = "";

    let leftX = 0;
    let leftY = 3;

    let rightX = 2;
    let rightY = 3;

    let used = '';
    for(let number of numbers){
        if(number === 1 || number === 4 || number === 7)
            used = 'L';
        else if(number === 3 || number === 6 || number === 9)
            used = 'R'
        else{
            let targetX = (number - 1) % 3;
            let targetY = Math.floor((number - 1) / 3);

            if(!number){
                targetX = 1;
                targetY = 3;
            }

            const destLeft = Math.abs(leftX - targetX) + Math.abs(leftY - targetY);
            const destRight = Math.abs(rightX - targetX) + Math.abs(rightY - targetY);

            if(destLeft < destRight)
                used = 'L';
            else if(destLeft > destRight)
                used = 'R';
            else{
                if(hand === 'left')
                    used = 'L';
                else
                    used = 'R';
            }

        }

        answer += used;
        if (used === 'L'){
            if(!number){
                leftX = 1;
                leftY = 3;
            }else{
                leftX = (number - 1) % 3;
                leftY = Math.floor((number - 1) / 3);
            }
        }else{
            if(!number){
                rightX = 1;
                rightY = 3;
            }else{
                rightX = (number - 1) % 3;
                rightY = Math.floor((number - 1) / 3);
            }
        }
    }

    return answer;
}