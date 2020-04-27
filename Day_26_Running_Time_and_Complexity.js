function processData(input) {
    //Enter your code here
    let result = input.split("\n").slice(1).map(isPrime);
    function isPrime(inp){
        if (inp < 2) {
            return 'Not prime'
        } else if (inp === 2) {
            return 'Prime'
        } else if (inp % 2 === 0) {
            return 'Not prime'
        } else {
            for (let i = 3, s = Math.sqrt(inp); i < s+1; i += 2) {
                if (inp % i === 0) {
                    return 'Not prime'
                }
            }
        }            return 'Prime'   

        }        console.log(result.join('\n'))

    }


process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function(input) {
    _input += input;
});

process.stdin.on("end", function() {
    processData(_input);
});
