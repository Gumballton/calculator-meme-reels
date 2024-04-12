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
    background-color: #333; /* Dark background color */
    color: #fff; /* Light text color */
    margin: 0;
    padding: 0;
  }

  h1 {
    font-size: 36px; 
  }

  p {
    font-size: 20px; 
  }

  .calculator-container {
    max-width: 600px; /* Maximum width for responsiveness */
    margin: 50px auto; /* Center the calculator */
    padding: 20px;
    background-color: #444; /* Darker background color */
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Box shadow for depth */
  }

  .loading-spinner {
    border: 8px solid #f3f3f3;
    border-top: 8px solid #34db3f;
    border-radius: 50%;
    width: 150px; 
    height: 150px; 
    animation: spin 2s linear infinite;
    display: none;
    margin-top: 20px; /* Add margin to separate from input forms */
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .slow-image {
    display: none;
    max-width: 100%; /* Make the image responsive */
  }

  /* Style input forms and button */
  input[type="text"], button {
    background-color: #555; /* Darker background color */
    color: #fff; /* Light text color */
    border: none;
    border-radius: 5px;
    padding: 10px;
    margin: 5px 0;
    font-size: 24px;
  }

  button {
    cursor: pointer;
    transition: background-color 0.3s;
  }

  button:hover {
    background-color: #666; /* Darker background color on hover */
  }
</style>
</head>
<body>

<div class="calculator-container">
  <h1>Calculator</h1>
  <p>This is a calculator. Please enter two numbers below and click "Calculate".</p>

  <input type="text" id="firstNumber" placeholder="Enter first number">
  <span> + </span>
  <input type="text" id="secondNumber" placeholder="Enter second number"> 
  <button onclick="calculate()">Calculate</button>

  <div class="loading-spinner"></div>

  <canvas class="slow-image" width="640" height="360"></canvas>
</div>

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
    img.src = "idk.jpg"; 
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
