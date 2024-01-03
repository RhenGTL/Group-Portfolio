// Profile Page
function slide(index) {
    var sliderContent = document.getElementById('slider-content');
    sliderContent.style.marginLeft = (-index * 100) + '%';
}

// Uppercase Converter
var originalResult = document.getElementById('result').innerText;
var isHovering = false;

document.getElementById('result').onclick = function() {
    var textarea = document.createElement('textarea');
    textarea.value = originalResult;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    this.innerText = "Text Copied!";
    var button = this;
    setTimeout(function() {
        button.innerText = isHovering ? "Click to Copy" : originalResult;
    }, 2000);
}

document.getElementById('result').addEventListener('mouseover', function() {
    isHovering = true;
});

document.getElementById('result').addEventListener('mouseout', function() {
    isHovering = false;
});

$(document).ready(function(){
    $("#result").hover(function(){
        $(this).data('originalText', $(this).text());
        $(this).text("Click to Copy");
    }, function(){
        $(this).text($(this).data('originalText'));
    });
});
