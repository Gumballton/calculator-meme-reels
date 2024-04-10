from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calculator</title>
<style>
  body {
    font-size: 24px; 
  }

  h1 {
    font-size: 36px; 
  }

  p {
    font-size: 20px; 
  }

  .loading-spinner {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #34db3f;
    border-radius: 50%;
    width: 150px; 
    height: 150px; 
    animation: spin 2s linear infinite;
    display: none;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .slow-image {
    display: none;
  }
</style>
</head>
<body>

<h1>Calculator</h1>
<p>This is a calculator. Please enter two numbers below and click "Calculate".</p>

<div class="loading-spinner"></div>

<input type="text" id="firstNumber" style="font-size: 24px;" placeholder="Enter first number">
<span style="font-size: 24px;"> + </span>
<input type="text" id="secondNumber" style="font-size: 24px;" placeholder="Enter second number"> 
<button onclick="calculate()" style="font-size: 24px;">Calculate</button>

<canvas class="slow-image" width="640" height="360"></canvas>

<script>
function calculate() {
    var firstNumber = document.getElementById("firstNumber").value;
    var secondNumber = document.getElementById("secondNumber").value;
    var animationDuration = 2000; 
    document.querySelector('.loading-spinner').style.display = 'inline-block'; 

    setTimeout(function() {
        document.querySelector('.loading-spinner').style.display = 'none'; 
        document.querySelector('.slow-image').style.display = 'block'; 
        loadSlowImage();
    }, animationDuration);
}

function loadSlowImage() {
    var img = new Image();
    img.src = "https://www.meme-arsenal.com/memes/8b955bf4c55ba0ae6f324087fd02777b.jpg"; 
    img.onload = function() {
        var canvas = document.querySelector('.slow-image');
        var ctx = canvas.getContext('2d');
        canvas.width = img.width; 
        canvas.height = img.height;

        var imgWidth = img.width;
        var imgHeight = img.height;
        var chunkHeight = 1;
        var chunks = Math.ceil(imgHeight / chunkHeight);
        var currentChunk = 0;

        function drawChunk() {
            if (currentChunk >= chunks) {
                return;
            }
            var y = currentChunk * chunkHeight;
            ctx.drawImage(img, 0, y, imgWidth, chunkHeight, 0, y, imgWidth, chunkHeight);
            currentChunk++;
            setTimeout(drawChunk, 5);
        }
        drawChunk();
    };
}
</script>
</body>
</html>

'''

@app.get("/")
async def get(request: Request):
    return HTMLResponse(content=html, status_code=200)