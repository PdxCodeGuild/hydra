
let message = prompt('Enter message to be encoded:');
let rot = Number(prompt('Enter a number of rotations: '));
let messageArray = message.split('');
let baseArray = [];
let index = 0;

//Handles the Lowercase range
function convertLower(number){
    const lowerAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
    number -= 97;
    number += rot;
    number = InBounds(number);
    return lowerAlphabet[number];
}

//Handles the uppercase range
function convertUpper(number){
    const upperAlphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    number -= 65;
    number += rot;
    number = InBounds(number);
    return upperAlphabet[number];
}

//Keeps the numbers within the range of the array
function InBounds(number){
    if (number < 0){
        number = number % 26;
        number += 26;
    } else if (number > 25){
        number = number % 26;
    }

    return number;
}

// This function serves as a filter:_________________________________________//
// Capital letters are passed to the convertUpper function.
// Lower case letters are passed to the convertLower function.
// Non-letter charicters are simply returned.
function convertChar(letter){
    number = letter.charCodeAt(0);
    if (number > 96 && number < 123){
        return convertLower(number);
    }else if (number > 64 && number < 91){
        return convertUpper(number);
    }else {
        return letter;
    }
}
//_________________________________________________________________________//


while (index < messageArray.length){
    let char = messageArray[index];
    baseArray.push(convertChar(char));
    
    index++
}

console.log(baseArray.join(''));
// hello there