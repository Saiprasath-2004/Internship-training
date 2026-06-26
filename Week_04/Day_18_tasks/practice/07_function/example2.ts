function addNumbers(a:number,b:number) {
    return a +b;
}

var result = addNumbers(1,2);
// result = addNumbers("1","2"); -> error in ts
console.log(result);