var pointButton = document.getElementById('pointButton');
var pointCount = document.getElementById('pointCount');
var pointsPerClick = 0;
var points = 0;

$(document).ready(function() {
  $.ajax({
    url: '/getUserPoints',
    method: 'GET',
    success: function(response) {
      pointsPerClick = response.pointsPerClick;
      points = response.currentPoints;
      
      pointCount.textContent = 'Points: ' + points;
      pointButton.textContent = 'Earn +' + pointsPerClick + ' Points';
    },
    error: function(error) {
      // 處理錯誤情況
    }
  });
});

pointButton.addEventListener('click', function() {
  points += pointsPerClick;
  pointCount.textContent = 'Points: ' + points;
});

$('#pointButton').on('click', function() {
  $.ajax({
    url: '/updatePoints',
    method: 'POST',
    data: { pointsPerClick: pointsPerClick },
    success: function(response) {
      // 處理成功情況
    },
    error: function(error) {
      // 處理錯誤情況
    }
  });
});
