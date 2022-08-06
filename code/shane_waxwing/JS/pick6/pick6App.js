function pick6(){
    const nums = [];

    while (nums.length < 6){
        nums.push(Math.floor(Math.random() * 100));
        
    }
    return nums;
}

function matchingNums(arrayOne, arrayTwo){
    let matches = 0;
    for (let i = 0; i < arrayOne.length; i++) {
        if (arrayOne[i] === arrayTwo[i]){
            matches++;
        }
    }
    return matches;
}
let earnings = 0;
let expenses = 0;
let balance = 0;
let interations = 0;
let winngingNums = pick6();


while (interations < 100000){
    let ticket = pick6();
    balance -= 2;
    expenses += 2;
    let matches = matchingNums(winngingNums, ticket);
    
    if (matches === 1){
        balance += 4;
        earnings +=4;
    } else if (matches === 2) {
        balance += 7;
        earnings += 7;
    } else if (matches === 3) {
        balance += 100;
        earnings += 100;
    } else if (matches === 4) {
        balance += 50000;
        earnings += 50000;
    } else if (matches === 5) {
        balance += 1000000;
        earnings += 1000000;
    } else if (matches === 6) {
        balance += 25000000;
        earnings +=25000000;
    }
    interations++
}
console.log("Earnings:",earnings)
console.log("Expenses:", expenses)

let roi = parseInt((earnings-expenses)/expenses);
console.log(balance);
console.log(typeof roi);
console.log(roi)
let EvE = expenses-earnings
console.log("EvE:", EvE)
let roiTest = EvE / expenses
console.log("Test:", roiTest)
