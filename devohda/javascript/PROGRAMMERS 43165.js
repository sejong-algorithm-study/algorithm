function makeTarget(numArr, num, target){
    const arrLen = numArr.length
    if(arrLen === 0){
        if(target === num){
            return 1;
        }else{
            return 0;
        }
    }

    const tmp = numArr[0];
    const newArr = numArr.slice(1, arrLen);

    return makeTarget(newArr, num + tmp, target) + makeTarget(newArr, num - tmp, target);
}

function solution(numbers, target) {
    const answer = makeTarget(numbers, 0, target);
    return answer;
}