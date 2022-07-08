// Chan Saechao 
// Javascript Lab 1

const readline = require('readline-sync');

// let userInput = parseInt(readline.question('enter a number: '));
// console.log(`you entered: ${userInput}`)

// Unit Converter
// Ask the user for the number of feet, and print out the equivalent distance in meters. 
// Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

// Convert Unit to Meter
const unit_conversion = {
    ft: 0.3048,
    mi: 1609.34,
    m: 1,
    km: 1000,
    yd: 0.9144,
    in: 0.0254
}

// Convert Meter to another Unit
const meter_conversion = {
    ft: 3.28084,
    mi: 0.000621371,
    m: 1,
    km: 0.00099999969062399994,
    yd: 1.0936129599999999673,
    in: 39.370066559999997935
}

let distance = parseInt(readline.question('What is the distance: '));
// ------------------------ Version 1-3 ---------------------------------------------------------------

// let unit = readline.question('enter a unit: ').toLocaleLowerCase();
// let conversion = unit_conversion[unit]
// converted_distance = distance * conversion
// console.log(distance)
// console.log(unit)
// console.log('dictionary value', conversion)
// console.log('new unit: ', converted_distance)
// console.log(distance, unit, ' is ', converted_distance, ' m.')

// ------------------------ Version 4 ------------------------------------------------------------------

let input_unit = readline.question('What are the input units? ').toLocaleLowerCase();
let output_unit = readline.question('What are the output units? ').toLocaleLowerCase();
// convert initial unit to m
let convert_meter = unit_conversion[input_unit]
let meter_distance = distance * convert_meter
// convert meter to output unit
let convert_output = meter_conversion[output_unit]
let output_distance = meter_distance * convert_output

// trouble shooting outputs
// console.log(convert_meter)
// console.log('meter distance ', meter_distance)

// console log the initial distance and input unit converted into the output unit
console.log(distance," ", input_unit, " is ", output_distance, output_unit)

// ------------------------ Pick 6 ------------------------------------------------------------------

function winning_6() {
    let num_string = new Array();
    for (let i = 0; i < 6; i++) {
        let random_num = Math.floor(Math.random() * 100);
        while (num_string.includes(random_num)) {
            random_num = Math.floor(Math.random() * 100);
        }
        // console.log([random_num]);
        num_string.push(random_num);
        num_string.sort(function(a, b){return a-b});
    }
    return [num_string[0], num_string[1], num_string[2], num_string[3], num_string[4], num_string[5]]
}
const winning_lottery = winning_6()
console.log('Winning numbers: ',winning_lottery)
// const result = Array.isArray(winning_lottery);
// console.log(result);

function pick_6() {
    let num_string = new Array();
    for (let i = 0; i < 6; i++) {
        let my_num = random_num = Math.floor(Math.random() * 100);
        while (num_string.includes(my_num)) {
            my_num = random_num = Math.floor(Math.random() * 100);
        }
        // console.log(my_num);
        num_string.push(my_num);
        num_string.sort(function(a, b){return a-b});
    }
    return [num_string[0], num_string[1], num_string[2], num_string[3], num_string[4], num_string[5]]
}
// let number_picked = pick_6();
// console.log('Winning numbers: ',winning_lottery)
// console.log(number_picked);

// variables
var balance = 0
var earnings = 0

// match a lotto ticket with winning numbers
function match(lottery_num, my_num, bal, earn) {
    i = 0;
    matching = 0
    for (lotto_num in lottery_num) {
        if (lottery_num[i] == my_num[i]) {
            matching += 1;
        }
        i += 1;
        // console.log('matching', matching)
    }
    // Calculate winnings of each ticket matches to balance
    if (matching == 1) {
        balance += 4
        earnings += 4
    }
    else if (matching == 2) {
        balance += 7
        earnings += 7
    }
    else if (matching == 3) {
        balance += 100
        earnings += 100
    }
        
    else if (matching == 4) {
        balance += 50000
        earnings += 50000
    }
    else if (matching == 5) {
        balance += 1000000
        earnings += 1000000
    }
        
    else if (matching == 6) {
        balance += 25000000
        earnings += 25000000
    }
    else {
        balance += 0
    }  
    // subtract 2 for the cost of each lottery ticket
    balance -= 2;
}

// variables
var ticket_count = 0;
const attempts = 100000;
var expenses = 0;

// while loop to buy 100,000 tickets
while (ticket_count < attempts) {
    let my_lottery = pick_6();
    // console.log('my lotto number ', my_lottery);
    balance_earning = match(winning_lottery, my_lottery, balance, earnings);
    // console.log(ticket_count)
    ticket_count += 1;
    expenses += 2; // add 2 for $2 ticket fee
}
const roi = ((earnings - expenses)/expenses)
console.log('Earnings: ', earnings, ' expenses: ', expenses, ' Return on investments: ', roi);

// ------------------------ Rot13 ------------------------------------------------------------------

// constant lower case and upper case and the before and after encode string
const alphabetLowerCase = "abcdefghijklmnopqrstuvwxyz";
const alphabetRot13LowerCase ='nopqrstuvwxyzabcdefghijklm';
const alphabetUpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const alphabetRot13UpperCase = "NOPQRSTUVWXYZABCDEFGHIJKLM";

// get user input and set encoded string to nothing
let userInput = readline.question('enter a string: ');
let encode = "";

// for loop Rot13 encryption while checking if statements for lower or upper
for ( let i=0; i < userInput.length; i++) {
    for (let j=0; j<26; j++) {
        if (userInput[i] == userInput[i].toLowerCase()){
            if (userInput[i] == alphabetLowerCase[j]) {
                encode += alphabetRot13LowerCase[j]
                // console.log(encode)
            }
        }
        else {
            if (userInput[i] == alphabetUpperCase[j]) {
                encode += alphabetRot13UpperCase[j]
                // console.log(encode)
            }
        }
    }
}
console.log("Encoded: ", encode);



