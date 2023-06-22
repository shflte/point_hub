var pointButton = document.getElementById('pointButton');
var pointCount = document.getElementById('pointCount');
var points = 0;

pointButton.addEventListener('click', function() {
  points++;
  pointCount.textContent = 'Points: ' + points;
});
