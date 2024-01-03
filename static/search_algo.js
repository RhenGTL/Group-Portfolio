// Get the element with the ID 'bgAnimation'
const bgAnimation = document.getElementById('bgAnimation');

// Define the number of color boxes to be created
const numberOfColorBoxes = 400;

// Loop to create a specified number of color boxes dynamically
for (let i = 0; i < numberOfColorBoxes; i++) {
    // Create a new div element for each color box
    const colorBox = document.createElement('div');

    // Add a CSS class 'colorBox' to each created div element
    colorBox.classList.add('colorBox');

    // Append each created color box to the 'bgAnimation' element
    bgAnimation.append(colorBox)
}
