// Arrow Slider
function slide(index, requestMethod) {
    var sliderContent = document.getElementById('slider-content');
    var newMargin = (-index * 100) + '%';
    sliderContent.style.marginLeft = newMargin;
    localStorage.setItem('sliderMargin', newMargin);
    localStorage.setItem('requestMethod', requestMethod);
}

window.onload = function() {
    var savedMargin = localStorage.getItem('sliderMargin');
    var savedRequestMethod = localStorage.getItem('requestMethod');
    var sliderButtons = document.getElementsByClassName('slider-button');
    var sliderContent = document.getElementById('slider-content');
    if (savedMargin) {
        sliderContent.style.transition = 'none';
        sliderContent.style.marginLeft = savedMargin;
        void sliderContent.offsetWidth;
        sliderContent.style.transition = '';
    }
    if (savedRequestMethod === "POST") {
        sliderContent.style.marginLeft = savedMargin;
    } else if (savedRequestMethod === "GET") {
        sliderContent.style.marginLeft = "0";
    }
    sliderContent.style.visibility = 'visible';
    sliderButtons[0].style.visibility = 'visible';
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
