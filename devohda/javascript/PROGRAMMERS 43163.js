function solution(begin, target, words) {
    const visited = Array.from({length : words.length}, () => false);
    const queue = [[0, begin]];

    while(queue.length !== 0){
        const [cnt, word] = queue.shift();

        if(word === target){
            return cnt
        }

        for(let i = 0; i < words.length; i++){
            let difference = 0;
            if(visited[i]){
                continue;
            }

            for(let j = 0; j < word.length; j++){
                if(word[j] !== words[i][j]){
                    difference++;
                }
            }

            if(difference === 1){
                visited[i] = true;
                queue.push([cnt + 1, words[i]]);
            }
        }
    }

    return 0;
}