function squareRoot() {
    closeDiv.style.display = 'inline-block';
    for (i = 0; i < divs.length; i++) {
        divs[i].style.display = 'none';
    }
}

function cubeRoot() {}

function multiply11() {}

function multiply12() {}

function multiplyPowersOf5() {}

function multiply2DigitNumbers() {}

function multiplyClosePowerOf10() {}

function multiplyNumbersUnitsAddTo10() {}

function square30To70() {}

function squareNumbersEndingIn5() {}

function cube2DigitNumbers() {}

function divisibilityTests() {}

function dividePowerOf5() {}

function divide9() {}

function hcf() {}

function lcm() {}

function hcfLcmOfFractions() {}

function solveLinearEquations() {}

function mentalAddition() {}

function mentalSubtraction() {}

w = document.documentElement.scrollWidth;
h = document.documentElement.scrollHeight;

divs = document.getElementsByClassName('divs');

closeDiv = document.getElementById('close');
closeDiv.onclick = () => {
    for (i = 0; i < divs.length; i++) {
        divs[i].style.display = 'inline-block';
    }
    closeDiv.style.display = 'none';
};

if (w > 1000 && w > h) {
    textArr = [
        'Finding Square Root<br>of Perfect Squares',
        'Finding Cube Root<br>of Perfect Cubes',
        'Multiply any<br>Number by 11',
        'Multiply any<br>Number by 12',
        'Multiply any<br>Number by<br>Powers of 5',
        'Multiplication of<br>2 Digit Numbers',
        'Multiplication of<br>Numbers Closer to<br>Powers of 10',
        'Multiplication of<br>Numbers Whose<br>Units Place<br>Add to 10',
        'Squares of<br>30 to 70',
        'Squares of<br>Numbers<br>Ending in 5',
        'Cube of any<br>2 Digit Number',
        'Divisibility<br>Tests',
        'Division by<br>Powers of 5',
        'Division<br>by 9',
        'HCF',
        'LCM',
        'HCF and LCM<br>of Fractions',
        'Solve<br>Linear Equations',
        'Mental<br>Addition',
        'Mental<br>Subtraction'
    ];
    clickFunc = [
        squareRoot,
        cubeRoot,
        multiply11,
        multiply12,
        multiplyPowersOf5,
        multiply2DigitNumbers,
        multiplyClosePowerOf10,
        multiplyNumbersUnitsAddTo10,
        square30To70,
        squareNumbersEndingIn5,
        cube2DigitNumbers,
        divisibilityTests,
        dividePowerOf5,
        divide9,
        hcf,
        lcm,
        hcfLcmOfFractions,
        solveLinearEquations,
        mentalAddition,
        mentalSubtraction
    ];
    for (i = 0; i < divs.length; i++) {
        divs[i].onclick = clickFunc[i];
        divs[i].innerHTML = textArr[i];
        divs[i].style.border = '1px solid black';
        divs[i].style.borderRadius = '1.6vw 3vw';
        divs[i].style.boxShadow = '5px 5px 2px grey';
        divs[i].style.display = 'inline-block';
        divs[i].style.fontFamily = 'Century Gothic';
        divs[i].style.fontSize = '2.5vw';
        divs[i].style.height = '16vw';
        divs[i].style.marginLeft = '2vw';
        divs[i].style.marginTop = '2vw';
        divs[i].style.overflow = 'hidden';
        divs[i].style.paddingLeft = '0.5vw';
        divs[i].style.paddingTop = '0.5vw';
        divs[i].style.textAlign = 'center';
        divs[i].style.verticalAlign = 'middle';
        divs[i].style.width = '30vw';
    }
} else {
    textArr = [
        'Finding<br>Square Root<br>of Perfect Squares',
        'Finding<br>Cube Root<br>of Perfect Cubes',
        'Multiply any<br>Number<br>by 11',
        'Multiply any<br>Number<br>by 12',
        'Multiply any<br>Number by<br>Powers of 5',
        'Multiplication<br>of 2 Digit<br>Numbers',
        'Multiplication<br>of Numbers<br>Closer to<br>Powers of 10',
        'Multiplication<br>of Numbers<br>Whose<br>Units Place<br>Add to 10',
        'Squares of<br>30 to 70',
        'Squares of<br>Numbers<br>Ending in 5',
        'Cube of<br>any 2<br>Digit Number',
        'Divisibility<br>Tests',
        'Division by<br>Powers of 5',
        'Division<br>by 9',
        'HCF',
        'LCM',
        'HCF and LCM<br>of Fractions',
        'Solve<br>Linear<br>Equations',
        'Mental<br>Addition',
        'Mental<br>Subtraction'
    ];
    for (i = 0; i < divs.length; i++) {
        divs[i].innerHTML = textArr[i];
        divs[i].style.border = '1px solid black';
        divs[i].style.borderRadius = '3.5vw 4vw';
        divs[i].style.boxShadow = '5px 5px 2px grey';
        divs[i].style.display = 'inline-block';
        divs[i].style.fontFamily = 'Century Gothic';
        divs[i].style.fontSize = '5vw';
        divs[i].style.height = '35vw';
        divs[i].style.marginLeft = '6vw';
        divs[i].style.marginTop = '6vw';
        divs[i].style.overflow = 'hidden';
        divs[i].style.paddingLeft = '0.5vw';
        divs[i].style.paddingTop = '0.5vw';
        divs[i].style.textAlign = 'center';
        divs[i].style.verticalAlign = 'middle';
        divs[i].style.width = '40vw';
    }
}