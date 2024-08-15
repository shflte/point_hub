var pointsPerClick = document.getElementById('pointsPerClick');
var currentPoints = document.getElementById('currentPoints');

$(document).ready(function() {
    $.ajax({
        url: '/getUserInfo',
        method: 'GET',
        success: function(response) {
            currentPoints.textContent = response.userInfo.currentPoints;
            pointsPerClick.textContent = response.userInfo.pointsPerClick;
        },
        error: function(error) {
            // error handling

        }
    });
});

$('#pointButton').on('click', function() {
    var currentPointsValue = parseInt(currentPoints.textContent);
    var pointsPerClickValue = parseInt(pointsPerClick.textContent);
    var incrementedPoints = currentPointsValue + pointsPerClickValue;

    $.ajax({
        url: '/incrementPoints',
        method: 'POST',
        data: {
            points: currentPoints + pointsPerClick
        },
        success: function() {
            currentPoints.textContent = incrementedPoints;
        },
        error: function(error) {
            console.error('Error:', error);
        }
    });
});
