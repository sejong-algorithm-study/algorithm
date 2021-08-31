function solution(array, commands) {
    let answer = []
    answer = commands.map(command => {
        const [i, j, k] = command;
        const newArr = array.slice(i-1,j).sort((a,b) => {
            if(a > b) return 1;
            if(a === b) return 0;
            if(a < b) return -1;
        });

        return newArr[k-1];
    });

    return answer;
}

// javascript sort 는 예상과 다르게